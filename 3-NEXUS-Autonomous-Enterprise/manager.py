import os
from typing import List, Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# 1. AYARLAR
load_dotenv()
if not os.environ.get("GOOGLE_API_KEY"):
    print("❌ HATA: API Anahtarı bulunamadı! .env dosyasını kontrol et.")
    exit()

# Model (Planlama için akıllı bir model lazım, temperature=0 ile kararlı olmasını sağlıyoruz)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# ---------------------------------------------------------
# 2. ŞİRKET YAPISI (Departmanlar)
# Yönetici sadece bu işçilere görev atayabilir.
# ---------------------------------------------------------
DEPARTMANLAR = Literal["Arastirmaci", "Analist", "Yazar", "Yazilimci", "Reviewer"]

# ---------------------------------------------------------
# 3. PLANLAMA MİMARİSİ (Structured Output)
# Yöneticinin çıktısı rastgele metin olamaz. Kesin bir liste olmalı.
# ---------------------------------------------------------

class Gorev(BaseModel):
    adim_no: int = Field(description="Adım numarası (1, 2, 3...)")
    departman: str = Field(description="Bu işi yapacak departman (Örn: Arastirmaci, Yazilimci)")
    talimat: str = Field(description="O departmana verilecek net emir.")
    cikti_beklentisi: str = Field(description="Bu adımdan beklenen sonuç nedir?")

class ProjePlani(BaseModel):
    proje_adi: str = Field(description="Projeye havalı bir isim ver")
    adimlar: List[Gorev] = Field(description="Yapılacak işlerin sıralı listesi")
    ozet: str = Field(description="Planın kısa bir özeti")

# Modeli bu kalıba zorluyoruz (Structured Output)
# Bu sayede model bize her zaman JSON formatında, python objesi olarak veri dönecek.
planlayici_llm = llm.with_structured_output(ProjePlani)

# ---------------------------------------------------------
# 4. YÖNETİCİ FONKSİYONU
# ---------------------------------------------------------
def proje_planla(kullanici_istegi: str):
    print(f"\n👔 YÖNETİCİ: '{kullanici_istegi}' için toplantı yapılıyor...")
    
    prompt = f"""
    Sen NEXUS şirketinin Genel Müdürüsün.
    Aşağıdaki kullanıcı isteğini gerçekleştirmek için detaylı bir iş planı oluştur.
    
    MEVCUT DEPARTMANLAR VE YETENEKLERİ:
    - Arastirmaci: İnternette arama yapar, veri toplar (Tavily kullanır).
    - Analist: Verileri okur, mantıksal çıkarım yapar (RAG kullanır).
    - Yazar: Blog yazısı, rapor veya metin yazar.
    - Yazilimci: Python, HTML, CSS kodu yazar.
    - Reviewer: Yazılan kodu veya metni kontrol eder.
    
    KULLANICI İSTEĞİ:
    {kullanici_istegi}
    
    Görevi mantıklı, sıralı adımlara böl. Her adıma en uygun departmanı ata.
    Birbirine bağımlı adımları sıraya koy (Önce araştırma, sonra yazma gibi).
    """
    
    # LLM'i çalıştır ve sonucu ProjePlani objesi olarak al
    try:
        plan = planlayici_llm.invoke(prompt)
        return plan
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

# ---------------------------------------------------------
# 5. TEST (YÖNETİM KURULU TOPLANTISI)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Senaryo: Çok karmaşık bir istek
    istek = "Yapay zeka trendleri hakkında bir araştırma yap, bununla ilgili bir blog yazısı yaz ve bu yazıyı gösterecek basit bir HTML sayfası kodla."
    
    final_plan = proje_planla(istek)
    
    if final_plan:
        print("\n" + "="*50)
        print(f"📁 PROJE: {final_plan.proje_adi}")
        print(f"📝 ÖZET: {final_plan.ozet}")
        print("="*50 + "\n")
        
        print("--- İŞ AKIŞ PLANI ---")
        for adim in final_plan.adimlar:
            print(f"[{adim.adim_no}] {adim.departman.upper()}")
            print(f"   Emir: {adim.talimat}")
            print(f"   Hedef: {adim.cikti_beklentisi}")
            print("-" * 30)