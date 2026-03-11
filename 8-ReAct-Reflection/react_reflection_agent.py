import time
import random

def weather_api(location):
    """
    Simüle edilmiş bir hava durumu API'si.
    Ajanın aracı (tool) kullanıp veri toplayabilmesi için yapılmıştır.
    """
    print(f"\n[Tool Execution] {location} için hava durumu API'si çağrılıyor...")
    time.sleep(1.5)
    
    # Bilerek bazen mantıksız değerler döndüren bir API yapalım ki
    # Agent'ın Reflection (İç denetim) yapma yeteneğini gözlemleyelim.
    if random.random() > 0.4:
        # %60 İhtimalle Normal Değer
        return random.randint(-5, 35) 
    else:
        # %40 İhtimalle Mantıksız Değer (API Hatası)
        return random.randint(150, 500) 

def simple_agent(user_prompt):
    print(f"\n👤 [Kullanıcı Sorusu]: {user_prompt}")
    print("=" * 60)
    
    # -------------------------------------------------------------------
    # ReAct (Reason + Act) AŞAMASI
    # -------------------------------------------------------------------
    # Thought: Ajanın ne yapması gerektiğini anladığı kısım.
    print("🧐 [Thought / Düşünce]:")
    print("Kullanıcı benden bir hava durumu bilgisi istiyor. Bunu öğrenebilmek için 'weather_api' aracını kullanmalıyım. Hedef konum 'Elazığ'.")
    time.sleep(1.5)
    
    # Action: Ajanın aracı kullandığı kısım.
    print("\n🛠️ [Action / Aksiyon]:")
    print("Çalıştırılıyor: weather_api('Elazığ')")
    observation = weather_api('Elazığ')
    
    # Observation: Aracı kullandıktan sonra dönen sonucu gözlemleme.
    print(f"👀 [Observation / Gözlem]:")
    print(f"API'den dönen raw (ham) veri: {observation}")
    time.sleep(1.5)
    
    # -------------------------------------------------------------------
    # Reflection (İç Kalite Kontrolü) AŞAMASI
    # -------------------------------------------------------------------
    print("\n🧠 [Reflection / Refleksiyon]:")
    print("Aldığım bu sonucu kullanıcıya sunmadan önce değerlendiriyorum... Mantıklı mı?")
    time.sleep(2)
    
    if observation > 50 or observation < -50:
        # Agent verinin mantıksız olduğunu fark eder. (Dünya'da 500 derece olması imkansız)
        print(f"↳ Uyarı: {observation}°C Dünya şartlarında mantıksız bir değer!")
        print("↳ Sorun Tespiti: Muhtemelen API'de, sensörde veya birimde (Fahrenheit-Kelvin karışıklığı) bir hata oldu.")
        print("↳ Düzeltme: Kullanıcıya hatalı veri vermek yerine, teknik bir aksaklık olduğunu bildireceğim.")
        final_answer = (f"Elazığ'ın hava durumunu kontrol ettim ancak servisten çok beklenmedik bir "
                        f"sıcaklık değeri ({observation}°C) döndü. Sistemsel bir aksaklık olduğu için "
                        f"şu an size kesin bir sonuç veremiyorum. Lütfen daha sonra tekrar deneyin.")
    else:
        # Agent verinin mantıklı olduğunu anlar ve devam eder.
        print(f"↳ Onay: {observation}°C gayet mantıklı bir Dünya sıcaklığı. Kullanıcıya bunu sunabilirim.")
        final_answer = f"Elazığ şu an {observation}°C."
        
    print("=" * 60)
    
    # -------------------------------------------------------------------
    # Final Answer (Kullanıcıya Sunulan Sonuç)
    # -------------------------------------------------------------------
    print(f"🤖 [Final Answer / Ajan Cevabı]:\n{final_answer}\n")

if __name__ == "__main__":
    print("\n🚀 ReAct + Reflection AI Agent Simülasyonuna Hoş Geldiniz! 🚀")
    soru = "Elazığ'ın şu anki hava durumu kaç derece?"
    simple_agent(soru)
