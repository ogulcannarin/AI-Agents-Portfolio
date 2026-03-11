import streamlit as st
import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# 1. AYARLAR
load_dotenv()

# Sayfa Ayarları (Sekme adı, ikon)
st.set_page_config(page_title="Kod Fabrikası AI", page_icon="🏭")

st.title("🏭 Otonom Kod Fabrikası")
st.write("Yazılımcı ve Testçi ajanlar senin için çalışıyor...")

# API Anahtarı Kontrolü (Sidebar'da gösterelim)
if not os.environ.get("GOOGLE_API_KEY"):
    st.error("❌ HATA: .env dosyasında GOOGLE_API_KEY bulunamadı!")
    st.stop()

# Model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# --- AJAN MİMARİSİ (Aynı Kod) ---
class DevTeamState(TypedDict):
    gorev: str
    python_kodu: str
    inceleme_notu: str
    onay_durumu: str
    tur_sayisi: int
    logs: list # Ekrana basmak için log tutacağız

def yazilimci_node(state: DevTeamState):
    log = "👨‍💻 YAZILIMCI: Kod yazıyor..."
    logs = state.get("logs", [])
    logs.append(log)
    
    gorev = state["gorev"]
    inceleme = state.get("inceleme_notu", "")
    tur = state.get("tur_sayisi", 0)
    
    if inceleme:
        prompt = f"GÖREV: {gorev}\nMEVCUT KOD: {state['python_kodu']}\nRAPOR: {inceleme}\n\nHataları düzelt ve kodu tekrar yaz. Sadece kodu ver."
    else:
        prompt = f"GÖREV: {gorev}\nTemiz bir Python kodu yaz. Sadece kodu ver."
    
    cevap = llm.invoke(prompt).content
    temiz_kod = cevap.replace("```python", "").replace("```", "").strip()
    
    return {"python_kodu": temiz_kod, "tur_sayisi": tur + 1, "logs": logs}

def testci_node(state: DevTeamState):
    log = "🕵️‍♂️ TESTÇİ: İnceliyor..."
    logs = state["logs"]
    logs.append(log)
    
    kod = state["python_kodu"]
    prompt = f"KOD:\n{kod}\n\nAnaliz et. Hata varsa 'RET' de ve açıkla. Yoksa 'ONAY' yaz."
    cevap = llm.invoke(prompt).content
    
    if "ONAY" in cevap:
        logs.append("   -> ✅ ONAYLANDI!")
        return {"onay_durumu": "ONAY", "inceleme_notu": "", "logs": logs}
    else:
        logs.append(f"   -> ❌ HATA BULUNDU! Geri gönderiliyor.")
        return {"onay_durumu": "RET", "inceleme_notu": cevap, "logs": logs}

def karar_mekanizmasi(state: DevTeamState):
    if state.get("tur_sayisi", 0) > 3: return END
    if state.get("onay_durumu") == "ONAY": return END
    return "yazilimci"

# Graph İnşası
builder = StateGraph(DevTeamState)
builder.add_node("yazilimci", yazilimci_node)
builder.add_node("testci", testci_node)
builder.set_entry_point("yazilimci")
builder.add_edge("yazilimci", "testci")
builder.add_conditional_edges("testci", karar_mekanizmasi, {"yazilimci": "yazilimci", END: END})
app = builder.compile()

# --- ARAYÜZ (FRONTEND) ---

# Kullanıcıdan Görev İste
gorev = st.text_area("Ne kodu yazmamı istersin?", "1'den 100'e kadar asal sayıları bulan kod yaz.")

if st.button("🚀 Fabrikayı Başlat"):
    with st.spinner("Ekip çalışıyor... (Bu işlem 10-20 saniye sürebilir)"):
        try:
            # Ajanı çalıştır
            sonuc = app.invoke({"gorev": gorev, "logs": []})
            
            # 1. Süreci Göster (Expandable)
            with st.expander("🔍 İşlem Kayıtlarını Gör (Logs)"):
                for log in sonuc["logs"]:
                    st.write(log)
            
            # 2. Final Kodu Göster
            st.success("🏁 İşlem Tamamlandı! İşte Kodun:")
            st.code(sonuc["python_kodu"], language="python")
            
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")