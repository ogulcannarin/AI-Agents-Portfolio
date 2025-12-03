import os
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient # <--- DEĞİŞİKLİK: Orijinal kütüphane (Hatasız)
from dotenv import load_dotenv

# Manager.py dosyasından fonksiyonu ve sınıfları çekiyoruz
# (Bu dosyanın aynı klasörde olduğundan emin ol)
from manager import proje_planla, ProjePlani, Gorev 

# 1. AYARLAR
load_dotenv()
if not os.environ.get("TAVILY_API_KEY"):
    # Eğer .env dosyasında yoksa manuel olarak buraya ekle (Hata almamak için)
    os.environ["TAVILY_API_KEY"] = "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"

if not os.environ.get("GOOGLE_API_KEY"):
    print("❌ HATA: GOOGLE_API_KEY bulunamadı!")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# ---------------------------------------------------------
# 2. STATE (NEXUS HAFIZASI)
# ---------------------------------------------------------
class NexusState(TypedDict):
    kullanici_istegi: str
    plan: ProjePlani
    su_anki_adim_index: int
    tamamlanan_isler: List[str]

# ---------------------------------------------------------
# 3. İŞÇİLER (WORKERS)
# ---------------------------------------------------------

def yonetici_node(state: NexusState):
    """1. Aşama: Planı Oluşturur"""
    print("\n👔 YÖNETİCİ: Toplantı başladı, plan yapılıyor...")
    istek = state["kullanici_istegi"]
    # Manager.py'den gelen fonksiyonu kullan
    plan = proje_planla(istek)
    
    if not plan:
        print("❌ HATA: Yönetici plan yapamadı!")
        return None

    return {
        "plan": plan, 
        "su_anki_adim_index": 0, 
        "tamamlanan_isler": []
    }

def arastirmaci_node(state: NexusState):
    """İnternetten veri toplar"""
    adim = state["plan"].adimlar[state["su_anki_adim_index"]]
    print(f"\n🌍 ARAŞTIRMACI: '{adim.talimat}' üzerinde çalışıyor...")
    
    try:
        # Doğrudan Tavily Client kullanıyoruz (Hatasız yöntem)
        tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
        response = tavily.search(query=adim.talimat, max_results=3)
        
        # Sonuçları metne dök
        sonuclar = "\n".join([f"- {r['title']}: {r['content']}" for r in response['results']])
        rapor = f"ARAŞTIRMA SONUCU ({adim.talimat}):\n{sonuclar}"
        
    except Exception as e:
        rapor = f"Araştırma hatası: {e}"
        
    return {"tamamlanan_isler": [rapor], "su_anki_adim_index": state["su_anki_adim_index"] + 1}

def yazar_node(state: NexusState):
    """Metin yazar"""
    adim = state["plan"].adimlar[state["su_anki_adim_index"]]
    gecmis_isler = "\n---\n".join(state["tamamlanan_isler"])
    print(f"\n✍️ YAZAR: '{adim.talimat}' yazılıyor...")
    
    prompt = f"""
    GÖREV: {adim.talimat}
    BEKLENEN ÇIKTI: {adim.cikti_beklentisi}
    
    KAYNAK BİLGİLER (Önceki departmanlardan gelen):
    {gecmis_isler}
    
    Lütfen profesyonel bir içerik yaz.
    """
    cevap = llm.invoke(prompt).content
    return {"tamamlanan_isler": [f"YAZI ÇIKTISI:\n{cevap}"], "su_anki_adim_index": state["su_anki_adim_index"] + 1}

def yazilimci_node(state: NexusState):
    """Kod yazar"""
    adim = state["plan"].adimlar[state["su_anki_adim_index"]]
    gecmis_isler = "\n---\n".join(state["tamamlanan_isler"])
    print(f"\n💻 YAZILIMCI: '{adim.talimat}' kodlanıyor...")
    
    prompt = f"""
    GÖREV: {adim.talimat}
    
    KAYNAK BİLGİLER:
    {gecmis_isler}
    
    Sadece temiz, çalışır kod bloğu ver. Markdown kullanma.
    """
    cevap = llm.invoke(prompt).content
    temiz_kod = cevap.replace("```html", "").replace("```python", "").replace("```", "")
    
    return {"tamamlanan_isler": [f"KOD ÇIKTISI:\n{temiz_kod}"], "su_anki_adim_index": state["su_anki_adim_index"] + 1}

def analist_node(state: NexusState):
    """Veri analizi yapar"""
    adim = state["plan"].adimlar[state["su_anki_adim_index"]]
    print(f"\n📊 ANALİST: '{adim.talimat}' analiz ediliyor...")
    
    prompt = f"GÖREV: {adim.talimat}\nAnalizini yap."
    cevap = llm.invoke(prompt).content
    return {"tamamlanan_isler": [f"ANALİZ:\n{cevap}"], "su_anki_adim_index": state["su_anki_adim_index"] + 1}

# ---------------------------------------------------------
# 4. ROUTER (TRAFİK POLİSİ)
# ---------------------------------------------------------
def router(state: NexusState):
    plan = state["plan"]
    index = state["su_anki_adim_index"]
    
    # Tüm adımlar bitti mi?
    if index >= len(plan.adimlar):
        return END
    
    # Sıradaki adımı al ve departmana yönlendir
    siradaki_gorev = plan.adimlar[index]
    departman = siradaki_gorev.departman
    
    if "Arastirmaci" in departman: return "arastirmaci"
    if "Yazar" in departman: return "yazar"
    if "Yazilimci" in departman: return "yazilimci"
    if "Analist" in departman: return "analist"
    return "analist" # Varsayılan

# ---------------------------------------------------------
# 5. GRAPH İNŞASI
# ---------------------------------------------------------
builder = StateGraph(NexusState)

builder.add_node("yonetici", yonetici_node)
builder.add_node("arastirmaci", arastirmaci_node)
builder.add_node("yazar", yazar_node)
builder.add_node("yazilimci", yazilimci_node)
builder.add_node("analist", analist_node)

builder.set_entry_point("yonetici")

# Yöneticiden sonra Router'a sor
builder.add_conditional_edges("yonetici", router)

# Her işçiden sonra tekrar Router'a sor (Sıradaki iş için)
builder.add_conditional_edges("arastirmaci", router)
builder.add_conditional_edges("yazar", router)
builder.add_conditional_edges("yazilimci", router)
builder.add_conditional_edges("analist", router)

nexus_app = builder.compile()

# ---------------------------------------------------------
# 6. ÇALIŞTIR
# ---------------------------------------------------------
if __name__ == "__main__":
    print("🏛️ PROJECT NEXUS BAŞLATILIYOR...")
    istek = input("👉 Patron, ne yapmamızı istersin?: ")
    
    try:
        sonuc = nexus_app.invoke({"kullanici_istegi": istek})
        
        print("\n" + "="*50)
        print("✅ TÜM GÖREVLER TAMAMLANDI! İŞTE RAPOR:")
        print("="*50 + "\n")
        
        for is_parcasi in sonuc["tamamlanan_isler"]:
            print(is_parcasi)
            print("\n" + "-"*30 + "\n")
            
    except Exception as e:
        print(f"Bir hata oluştu: {e}")