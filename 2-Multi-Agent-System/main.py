import os
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# 1. AYARLAR
load_dotenv()

# Şifre Kontrolü (Hata varsa baştan söyleyelim)
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("❌ HATA: GOOGLE_API_KEY bulunamadı! .env dosyasını kontrol et.")
    exit()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)

# 2. STATE (Hafıza)
class DevTeamState(TypedDict):
    gorev: str
    python_kodu: str
    inceleme_notu: str
    onay_durumu: str
    tur_sayisi: int

# 3. NODES (Ajanlar)
def yazilimci_node(state: DevTeamState):
    print("\n👨‍💻 YAZILIMCI: Kod üzerinde çalışıyorum...")
    gorev = state["gorev"]
    inceleme = state.get("inceleme_notu", "")
    tur = state.get("tur_sayisi", 0)
    
    if inceleme:
        prompt = f"GÖREV: {gorev}\nMEVCUT KOD: {state['python_kodu']}\nTESTÇİ RAPORU: {inceleme}\n\nHataları düzelt ve kodu tekrar yaz. Sadece kodu ver."
    else:
        prompt = f"GÖREV: {gorev}\nTemiz bir Python kodu yaz. Sadece kodu ver."
    
    cevap = llm.invoke(prompt).content
    temiz_kod = cevap.replace("```python", "").replace("```", "").strip()
    return {"python_kodu": temiz_kod, "tur_sayisi": tur + 1}

def testci_node(state: DevTeamState):
    print("\n🕵️‍♂️ TESTÇİ: Kodu inceliyorum...")
    kod = state["python_kodu"]
    prompt = f"KOD:\n{kod}\n\nAnaliz et. Hata varsa 'RET' de ve açıkla. Yoksa 'ONAY' yaz."
    cevap = llm.invoke(prompt).content
    
    if "ONAY" in cevap:
        print("   -> ✅ Testçi: Onaylıyorum.")
        return {"onay_durumu": "ONAY", "inceleme_notu": ""}
    else:
        print(f"   -> ❌ Testçi: Hata buldum! Geri gönderiyorum.")
        return {"onay_durumu": "RET", "inceleme_notu": cevap}

# 4. ROUTER
def karar_mekanizmasi(state: DevTeamState):
    if state.get("tur_sayisi", 0) > 3: 
        print("⚠️ Çok fazla tur, durduruluyor.")
        return END
    if state.get("onay_durumu") == "ONAY": 
        return END
    return "yazilimci"

# 5. GRAPH
builder = StateGraph(DevTeamState)
builder.add_node("yazilimci", yazilimci_node)
builder.add_node("testci", testci_node)
builder.set_entry_point("yazilimci")
builder.add_edge("yazilimci", "testci")
builder.add_conditional_edges("testci", karar_mekanizmasi, {"yazilimci": "yazilimci", END: END})

app = builder.compile()

# 6. BAŞLATMA KOMUTU
if __name__ == "__main__":
    print("🚀 KOD FABRİKASI (Docker) BAŞLATILIYOR...")
    
    # Kullanıcıdan görev iste
    try:
        gorev = input("👉 Hangi kodu yazayım?: ")
        if gorev:
            sonuc = app.invoke({"gorev": gorev})
            print("\n" + "="*40)
            print("🏁 FİNAL KOD:")
            print("="*40)
            print(sonuc["python_kodu"])
    except Exception as e:
        print(f"Bir hata oluştu: {e}")