🏛️ PROJECT NEXUS: Autonomous Multi-Agent Enterprise

Project NEXUS, tek bir komutla karmaşık görevleri yerine getirebilen, hiyerarşik yapıya sahip otonom bir Yapay Zeka Şirketi simülasyonudur.

Bu sistemde tek bir "Yönetici Ajan" (Manager) bulunur. Kullanıcıdan gelen isteği analiz eder, alt görevlere böler ve bu görevleri Araştırmacı, Yazılımcı, Yazar ve Analist ajanlarına dinamik olarak dağıtır.

🧠 Mimari ve Çalışma Mantığı

Bu proje, "Hierarchical Planning & Execution" (Hiyerarşik Planlama ve Yürütme) mimarisini kullanır.

1. Yönetim Kurulu (The Brain)

Manager Agent: Kullanıcının karmaşık isteğini (Örn: "Pazar araştırması yap ve rapor yaz") alır.

Structured Output (Pydantic): İsteği mantıksal adımlara böler ve bir JSON iş planı oluşturur.

Delegasyon: Her adımı en uygun departmana atar.

2. Departmanlar (The Workers)

🌍 Araştırmacı (Researcher): Tavily API kullanarak internette gerçek zamanlı veri toplar.

📊 Analist (Analyst): Toplanan verileri analiz eder ve içgörü çıkarır.

✍️ Yazar (Writer): Analizlere dayanarak blog yazısı veya rapor hazırlar.

💻 Yazılımcı (Coder): İstenen proje için Python/HTML/CSS kodu yazar.

3. Orkestrasyon (LangGraph)

Ajanlar arasındaki veri akışını ve sıra yönetimini LangGraph StateMachine yönetir.

İş akışı doğrusaldır ancak dinamik yönlendirme (Router) içerir.

🛠️ Teknoloji Yığını

Bileşen

Teknoloji

Görevi

Orkestrasyon

LangGraph

Ajanlar arası durum (State) yönetimi ve yönlendirme.

LLM

Google Gemini 2.0 Flash

Akıl yürütme, planlama ve içerik üretimi.

Arama Motoru

Tavily AI

Ajanların internete erişmesi ve güncel veri toplaması.

Veri Doğrulama

Pydantic

Yöneticinin çıktısının bozuk olmamasını sağlar.

Dil

Python 3.10+

Ana geliştirme dili.

📂 Proje Yapısı

03-NEXUS-Autonomous-Enterprise/
├── main.py              # 🧠 Ana Orkestrasyon (LangGraph Döngüsü)
├── manager.py           # 👔 Yönetici Ajan (Planlama Mantığı)
├── requirements.txt     # 📦 Gerekli kütüphaneler
├── .env                 # 🔒 API Anahtarları (Git'e yüklenmez!)
└── README.md            # 📄 Proje dokümantasyonu


🚀 Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için:

1. Gereksinimleri Yükleyin

pip install -r requirements.txt


2. API Anahtarlarını Ayarlayın

Proje klasöründe .env adında bir dosya oluşturun ve içine şunları ekleyin:

GOOGLE_API_KEY=AIzaSy... (Google AI Studio Anahtarınız)
TAVILY_API_KEY=tvly-... (Tavily Search Anahtarınız)


3. Şirketi Başlatın

python main.py


4. Örnek Senaryo

Terminal açıldığında sizden bir görev isteyecektir. Şunu deneyebilirsiniz:

"Elon Musk'ın xAI şirketi ve Grok modeli hakkında araştırma yap, bunun önemini anlatan kısa bir yazı yaz ve bu yazıyı gösterecek dark mode bir HTML sayfası kodla."

📸 Örnek Çıktı (Loglar)

👔 YÖNETİCİ: Toplantı başladı, plan yapılıyor...
🌍 ARAŞTIRMACI: 'xAI Grok özellikleri' üzerinde çalışıyor...
📊 ANALİST: 'Verileri analiz et' üzerinde çalışıyor...
✍️ YAZAR: 'Blog yazısı yazılıyor'...
💻 YAZILIMCI: 'HTML sayfası kodlanıyor'...

✅ TÜM GÖREVLER TAMAMLANDI! İŞTE RAPOR:
[Burada final blog yazısı ve HTML kodu görünür]


🔮 Gelecek Planları

[ ] Human-in-the-Loop: Yöneticinin planını insan onayına sunmak.

[ ] Streamlit UI: Terminal yerine web tabanlı bir "Mission Control" paneli.

[ ] Dosya Çıktısı: Yazılımcı ajanının kodları direkt .html veya .py dosyası olarak kaydetmesi.

Geliştirici: Oğulcan Narin