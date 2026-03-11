import os
import sqlite3
from typing import TypedDict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver # <--- YENİ: VERİTABANI YÖNETİCİSİ
from tavily import TavilyClient
from pypdf import PdfReader
from dotenv import load_dotenv

# 1. AYARLAR
load_dotenv()

if not os.environ.get("GOOGLE_API_KEY"): print("❌ HATA: GOOGLE_API_KEY eksik!")
if not os.environ.get("TAVILY_API_KEY"): print("❌ HATA: TAVILY_API_KEY eksik!")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# 2. VERİTABANI BAĞLANTISI (Kalıcı Hafıza)
# Bu kod klasörde 'hafiza.sqlite' diye bir dosya oluşturacak.
db_path = "hafiza.sqlite"
conn = sqlite3.connect(db_path, check_same_thread=False)
memory = SqliteSaver(conn)

# 3. UYGULAMA BAŞLAT
app = FastAPI(title="Memory Agent Backend", version="3.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. STATE
class AgentState(TypedDict):
    soru: str
    dosya_adi: str
    bulunan_bilgi: str
    kaynak: str

# 5. YARDIMCI FONKSİYONLAR
def pdf_oku(dosya_yolu):
    if not os.path.exists(dosya_yolu): return None
    try:
        reader = PdfReader(dosya_yolu)
        text = ""
        for page in reader.pages: text += page.extract_text() + "\n"
        return text
    except: return None

# 6. NODES
def cv_kontrol_node(state: AgentState):
    dosya = state.get("dosya_adi", "ornek_cv.pdf")
    print(f"📄 CV KONTROL: {dosya} okunuyor...")
    
    cv_metni = pdf_oku(dosya)
    if not cv_metni: return {"bulunan_bilgi": "DOSYA_YOK", "kaynak": "Sistem"}

    # PROMPT GÜNCELLEMESİ: İnternete gitmeye zorluyoruz
    prompt = f"""
    Metin: {cv_metni}
    Soru: {state["soru"]}
    
    KURALLAR:
    1. Kullanıcı sohbet ediyorsa ("Selam", "Nasılsın") -> Sohbet et.
    2. Sorunun cevabı metinde varsa -> Cevabı yaz.
    3. Cevap metinde yoksa VE dışarıdan bulunması gerekiyorsa (Örn: Güncel bilgi, Github yıldız sayısı, Hava durumu) -> SADECE 'YOK' yaz.
    """
    
    sonuc = llm.invoke(prompt).content.strip()
    
    # DEBUG: Modelin ne dediğini terminalde görelim
    print(f"   👀 Modelin İç Sesi: {sonuc}") 
    
    # MANTIK GÜNCELLEMESİ: İçinde "YOK" geçiyorsa Web'e git (Daha esnek)
    if "YOK" in sonuc: 
        print("   -> 🚀 Karar Verildi: Web'e gidiliyor...")
        return {"bulunan_bilgi": "YOK", "kaynak": "Yok"}
    else:
        return {"bulunan_bilgi": sonuc, "kaynak": "PDF/Hafıza"}
    

def web_arama_node(state: AgentState):
    print("🌍 WEB ARAMA: Tavily çalışıyor...")
    try:
        tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
        response = tavily.search(query=state["soru"], max_results=2)
        arama_metni = "\n".join([f"- {r['title']}: {r['content']}" for r in response['results']])
        
        ozet = llm.invoke(f"Soru: {state['soru']}\n\nİnternet Verisi:\n{arama_metni}\n\nCevapla:")
        return {"bulunan_bilgi": ozet.content, "kaynak": "Tavily"}
    except Exception as e:
        return {"bulunan_bilgi": f"Hata: {e}", "kaynak": "Hata"}

def rota_belirle(state: AgentState):
    if state["bulunan_bilgi"] == "YOK": return "web_ara"
    else: return END

# 7. GRAPH
builder = StateGraph(AgentState)
builder.add_node("cv_kontrol", cv_kontrol_node)
builder.add_node("web_arama", web_arama_node)
builder.set_entry_point("cv_kontrol")
builder.add_conditional_edges("cv_kontrol", rota_belirle, {"web_ara": "web_arama", END: END})
builder.add_edge("web_arama", END)

# DİKKAT: checkpointer parametresini ekledik!
super_agent = builder.compile(checkpointer=memory)

# 8. API ENDPOINT
class SoruIstegi(BaseModel):
    soru: str
    dosya_adi: str = "ornek_cv.pdf"
    session_id: str = "kullanici_1" # Varsayılan bir ID

@app.post("/chat")
async def chat_endpoint(istek: SoruIstegi):
    print(f"\n📨 ({istek.session_id}) İSTEK: {istek.soru}")
    
    # LangGraph Config: Hangi hafızayı kullanacağını session_id belirler
    config = {"configurable": {"thread_id": istek.session_id}}
    
    try:
        sonuc = super_agent.invoke(
            {"soru": istek.soru, "dosya_adi": istek.dosya_adi},
            config=config # Hafıza ayarını gönderiyoruz
        )
        return {"cevap": sonuc["bulunan_bilgi"], "kaynak": sonuc["kaynak"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))