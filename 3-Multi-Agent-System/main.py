import os
from typing import TypedDict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# 1. AYARLAR
load_dotenv()

if not os.environ.get("GOOGLE_API_KEY"):
    print("❌ HATA: .env dosyasında GOOGLE_API_KEY bulunamadı!")
    exit()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# 2. UYGULAMA BAŞLAT
app = FastAPI(title="Multi-Agent System API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. STATE (ORTAK ÇALIŞMA MASASI)
class DevTeamState(TypedDict):
    gorev: str          # Kullanıcının isteği
    python_kodu: str    # Yazılımcının yazdığı kod
    inceleme_notu: str  # Testçinin yorumu
    onay_durumu: str    # "ONAY" veya "RET"
    tur_sayisi: int     # Sonsuz döngüye girmesin diye sayaç

# 4. NODES (ÇALIŞANLAR)
def yazilimci_node(state: DevTeamState):
    """Görevi alır, kod yazar. Eğer hata varsa düzeltir."""
    print("\n👨‍💻 YAZILIMCI: Kod üzerinde çalışıyorum...")
    
    gorev = state["gorev"]
    inceleme = state.get("inceleme_notu", "")
    tur = state.get("tur_sayisi", 0)
    
    # Prompt: Eğer inceleme notu varsa "Düzelt", yoksa "Sıfırdan Yaz"
    if inceleme:
        prompt = f"""
        GÖREV: {gorev}
        MEVCUT KOD: {state['python_kodu']}
        TESTÇİ RAPORU: {inceleme}
        
        Lütfen testçinin raporuna göre koddaki hataları düzelt ve kodu tekrar yaz.
        Sadece Python kodunu ver, açıklama yapma.
        """
    else:
        prompt = f"""
        GÖREV: {gorev}
        Lütfen bu görev için temiz, çalışır bir Python kodu yaz.
        Sadece Python kodunu ver, açıklama yapma.
        """
    
    # Kodu yazdır
    cevap = llm.invoke(prompt).content
    
    # Temizlik (Markdown işaretlerini kaldır)
    temiz_kod = cevap.replace("```python", "").replace("```", "").strip()
    
    return {
        "python_kodu": temiz_kod, 
        "tur_sayisi": tur + 1
    }

def testci_node(state: DevTeamState):
    """Kodu okur, hata arar."""
    print("\n🕵️‍♂️ TESTÇİ: Kodu inceliyorum...")
    
    kod = state["python_kodu"]
    
    # LLM'e soruyoruz: Bu kodda hata var mı?
    prompt = f"""
    Sen kıdemli bir kod inceleme uzmanısın (QA).
    Aşağıdaki Python kodunu analiz et.
    
    KOD:
    {kod}
    
    KURALLAR:
    1. Eğer kodda mantık hatası, eksik import veya güvenlik açığı varsa: "RET" de ve hatayı açıkla.
    2. Eğer kod kusursuzsa ve çalışacak gibiyse: Sadece "ONAY" yaz.
    """
    
    cevap = llm.invoke(prompt).content
    
    if "ONAY" in cevap:
        print("   -> ✅ Testçi: Mükemmel, onaylıyorum.")
        return {"onay_durumu": "ONAY", "inceleme_notu": ""}
    else:
        print(f"   -> ❌ Testçi: Hata buldum! Geri gönderiyorum.\n   Not: {cevap[:100]}...")
        return {"onay_durumu": "RET", "inceleme_notu": cevap}

# 5. ROUTER (TRAFİK POLİSİ)
def karar_mekanizmasi(state: DevTeamState):
    durum = state.get("onay_durumu")
    tur = state.get("tur_sayisi", 0)
    
    # Güvenlik Kilidi: 3 turdan fazla dönerse zorla bitir
    if tur > 3:
        print("\n⚠️ UYARI: Çok fazla deneme yapıldı, işlem sonlandırılıyor.")
        return END
    
    if durum == "ONAY":
        return END           # Bitiş
    else:
        return "yazilimci"   # Başa dön (Loop)

# 6. GRAPH İNŞASI
builder = StateGraph(DevTeamState)

builder.add_node("yazilimci", yazilimci_node)
builder.add_node("testci", testci_node)

builder.set_entry_point("yazilimci")

# Yazılımcı bitince -> Testçiye git
builder.add_edge("yazilimci", "testci")

# Testçi bitince -> Karar ver (Dönelim mi bitirelim mi?)
builder.add_conditional_edges(
    "testci",
    karar_mekanizmasi,
    {
        "yazilimci": "yazilimci",
        END: END
    }
)

# Graph'ı derle
multi_agent = builder.compile()

# 7. API ENDPOINTS
class GorevIstegi(BaseModel):
    gorev: str

class GorevCevap(BaseModel):
    kod: str
    durum: str
    tur_sayisi: int

@app.post("/generate-code", response_model=GorevCevap)
async def generate_code(istek: GorevIstegi):
    print(f"\n🚀 GÖREV ALINDI: {istek.gorev}")
    
    try:
        sonuc = multi_agent.invoke({"gorev": istek.gorev})
        
        return {
            "kod": sonuc["python_kodu"],
            "durum": sonuc.get("onay_durumu", "TAMAMLANDI"),
            "tur_sayisi": sonuc.get("tur_sayisi", 0)
        }
    except Exception as e:
        print(f"❌ HATA: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {
        "durum": "aktif", 
        "mesaj": "Multi-Agent Kod Fabrikası Çalışıyor!",
        "ajanlar": ["Yazılımcı", "Testçi"]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "agents": 2}
