# YKS-AI-Platform - Otomatik Kalite Kontrol Sistemi

Bu proje, yapay zeka tabanlı sistemimizin (YKS-AI-Platform) verdiği yanıtların doğruluğunu ve kalitesini ölçmek için **DeepEval** kullanılarak hazırlanan otomatik bir test altyapısıdır.

## Sistem Nasıl Çalışıyor?

### 1. Test Senaryosunu Tanımlama (Girdileri Hazırlama)
Kodun içinde bir `LLMTestCase` oluşturulur. Bu, aslında bir deneyi kurmak gibidir. Şu üç bileşen belirlenir:
- **Input (Soru):** Kullanıcı ne sordu? (Örn: "İade politikası nedir?")
- **Actual Output (Yanıt):** Yapay zeka bu soruya ne cevap verdi? (Gerçek projede bu cevap sistemin çıktısı olacaktır).
- **Retrieval Context (Bilgi Kaynağı):** Modelin bu cevabı verirken referans alması gereken dökümanlar nelerdir?

### 2. "Hakim" (Evaluator) Modeli Devreye Sokma
DeepEval kütüphanesi, hazırlanan bu üçlüyü (Soru, Yanıt, Kaynak) alır ve değerlendirme yapacak başka bir yapay zekaya (denetçi model) gönderir.
*Temel Mantık:* "Bir yapay zekayı, ondan daha yetenekli veya tarafsız bir başka yapay zeka ile denetle."

### 3. Metrikleri (Kriterleri) Uygulama
Değerlendirme iki ana kriter üzerinden yapılır:
- **Faithfulness (Sadakat):**
  - *Süreç:* Denetçi model, yanıtı ve bilgi kaynağını karşılaştırır.
  - *Soru:* "Bu cevap, tamamen bu kaynağa mı dayanıyor yoksa model bir şeyler mi uydurmuş (halüsinasyon)?"
  - *Sonuç:* 1.0 (Tam puan), modelin kaynakta olmayan hiçbir bilgiyi uydurmadığını gösterir.
- **Answer Relevancy (Yanıt Alakası):**
  - *Süreç:* Denetçi model, soru ile yanıtı karşılaştırır.
  - *Soru:* "Bu cevap, sorulan soruya gerçekten bir çözüm sunuyor mu, yoksa lafı dolandırıyor mu?"
  - *Sonuç:* 1.0 (Tam puan), modelin konuyu dağıtmadan direkt istenilen cevabı verdiğini gösterir.

### 4. Threshold (Eşik Değer) Kontrolü
Testlerde `threshold=0.7` gibi bir eşik değer belirlenir.
- DeepEval arka planda puanı hesaplar.
- Eğer bu puan belirlenen eşiğin altında kalırsa, test `FAILED` (Başarısız) olarak sonuçlanır ve sistemdeki bir sorunu (halüsinasyon veya alakasız cevap) haber verir. Eşiğin üstü ise `PASSED` (Başarılı) döner.

### 5. Raporlama ve Analiz
Test sonucunda detaylı bir rapor sunulur:
- **Reason (Gerekçe):** DeepEval sadece puan vermez, neden o puanı verdiğini de açıklar (Örn: *"The score is 1.0 because there are no contradictions..."*).
- **Token Cost:** Analiz yapılırken arka planda kullanılan modelin maliyetini gösterir.

## YKS-AI-Platform İçin Neden Önemli?
Binlerce öğrencinin soru çözeceği ve cevap alacağı bir platformda, her bir cevabı tek tek manuel olarak kontrol etmek imkansızdır. Bu sistem sayesinde:
1. Sisteme yüzlerce örnek soru ve cevap anahtarı yüklenebilir.
2. Yazılım her güncellendiğinde tek bir komutla (`deepeval test run`) tüm sorular otomatik olarak test edilebilir.
3. Eğer model bir soruda yanlış bir formül uydurursa (Faithfulness düşerse), sistem anında uyarı verir.

**Özetle:** Bu yapı, yapay zekanın "doğru ve kaynağa bağlı konuşup konuşmadığını" denetleyen hayati bir otomatik kalite kontrol mekanizmasıdır.
