# LangGraph ile Human-in-the-Loop (İnsan Onaylı) Ajan 🤖🧑‍💻

Bu depo (repository), **LangGraph** kütüphanesi kullanılarak oluşturulmuş, içerisine insan onayı (Human-in-the-Loop / HITL) mekanizması entegre edilmiş yapay zeka ajanı örneklerini barındırmaktadır.

## 📂 Klasör Yapısı ve Değerlendirme

Klasör yapısı şu anda oldukça sade ve doğrudan amaca yönelik. İçerisinde konuyu temelden alarak pratik bir şekilde ileriye taşıyan iki adet Jupyter Notebook bulunuyor:

*   `LangGraph_HITL0.ipynb`: Kurulum, temel yapılandırma ve insan onaylı (HITL) bir sistemin temel mantığını anlatan statik örnek.
*   `LangGraphHITL1.ipynb`: Gerçek bir LLM (OpenAI) entegrasyonu ile dinamik içerik üretiminin yapıldığı ve insan onay sürecinin işlendiği daha gelişmiş bir örnek.

Sade ve karmaşadan uzak olması, spesifik olarak **"Human-in-the-Loop"** konseptini öğrenmek isteyenler için harika bir avantaj sağlıyor. Gelecekte projeyi genişletmek isterseniz (`requirements.txt`, veri klasörleri, Python modülleri vs.) yeni klasörler ekleyebilirsiniz ancak mevcut eğitim/örnek senaryosu için yapı son derece yeterli.

---

## 🎯 Projenin Amacı

Yapay zeka modellerinin kendi başına karar verip aksiyon alabilmesi (örneğin e-posta göndermek, veritabanı silmek) bazen riskli olabilir. Bu projenin amacı; otonom süreçleri belirli kontrol noktalarında (checkpoint) durdurarak kullanıcıdan (insandan) **onay, yönlendirme veya geri bildirim** aldıktan sonra sürecin devam etmesini veya iptal olmasını sağlamaktır.

## 🚀 İçerikte Neler Var?

Bu klasör sistemin gelişim sürecine göre sıralanmış defterler (notebooks) içerir:

### 1- `LangGraph_HITL0.ipynb` (Temel Mantık)
*   Durum Grafiği (StateGraph) ve Ajan Durumu (AgentState) tanımlamalarının nasıl yapıldığını gösterir.
*   **Aşama 1:** Ajanın taslak bir mail oluşturduğu düğüm (node).
*   **Aşama 2:** Sürecin durdurulup insan incelemesine (Human Review) sunulduğu, konsoldan `yes`/`no` girdisi ile kararın alındığı düğüm.
*   **Aşama 3:** Duruma göre (Koşullu Geçişler - Conditional Edges) mailin gönderilmesi ya da sürecin sonlandırılması (`END`).

### 2- `LangGraphHITL1.ipynb` (LLM Entegrasyonu)
*   Sisteme **OpenAI** LLM (`gpt-4o-mini`) modülünün dahil edildiği daha gelişmiş versiyondur.
*   Ajan sadece statik metinler değil, kullanıcı tarafından sağlanan konu ('yapay zeka toplantısı' vb.) parametrelerine uygun gerçek taslaklar üretir.
*   Oluşturulan metin ekrana basılır ve kullanıcıya sunulur. Karar sonrası süreç (yine state bazlı) ilerler veya sonlanır.
*   LangChain ve LangGraph'ın entegre edilişinin ve API anahtarı ayarlarının nasıl yapıldığının pratik örneğidir.

## 🛠 Kullanılan Teknolojiler

*   **Python 3.x**
*   **LangGraph & LangChain:** Akış senaryoları ve durum yönetimi.
*   **LangChain OpenAI:** Dinamik yapay zeka metin üretimi.
*   **Jupyter Notebook:** Etkileşimli geliştirme alanı.

## 💡 Nasıl Çalıştırılır?

1. Notebook dosyalarını Jupyter veya Google Colab üzerinden açın.
2. `!pip install langgraph langchain langchain-openai` hücresini çalıştırarak bağımlılıkları indirin.
3. İkinci notebook (`LangGraphHITL1.ipynb`) için çevresel değişkenlerde (Environment Variables) kendi **`OPENAI_API_KEY`** bilginizi tanımlamanız gerekmektedir.
4. Hücreleri sırayla çalıştırın ve konsol çıktı ekranından `yes` veya `no` diyerek insan denetimi sürecini (HITL) bizzat test edin!
