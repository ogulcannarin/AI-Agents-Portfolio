# 🌍 AI Seyahat Asistanı & LangSmith Entegrasyonu

Bu proje, LangChain kullanılarak geliştirilmiş bir akıllı seyahat rehberi asistanıdır. Projenin temel amacı, sadece bir Büyük Dil Modeli (LLM) uygulaması geliştirmek değil; bu uygulamayı uçtan uca **LangSmith** ile izlemek, performansını ölçümlemek, hata ayıklamak (debug) ve optimize etmektir.

## 🚀 Öne Çıkan Özellikler

- **LangChain Expression Language (LCEL):** Modern LangChain mimarisi ile Prompt, Model ve Output Parser bileşenleri birbirine *pipe (`|`)* operatörü ile bağlanmış ve yüksek performanslı bir zincir (chain) oluşturulmuştur.
- **Dinamik ve Esnek Prompt Yönetimi:** Sistem, kullanıcıdan alınan şehir girdisine göre anlık olarak o şehre özel 1 günlük gezi planı ve mutlaka tadılması gereken yerel yemek önerileri üretir.
- **Gelişmiş İzleme (Tracing) ve Monitoring:** LangSmith entegrasyonu sayesinde, yapılan her bir LLM çağrısı detaylıca kayıt altına alınır.
  - *Maliyet (Cost) Analizi*
  - *Token Kullanım Takibi*
  - *Gecikme Süresi (Latency) Ölçümü*
- **Hata Yönetimi ve Debugging:** Model seviyesindeki hatalar, eksik parametreler veya API bağlantı sorunları LangSmith görsel arayüzü üzerinden anında tespit edilerek geliştirme süreci hızlandırılır.

## 🛠 Kullanılan Teknolojiler

- **Python (3.8+)** - Temel geliştirme dili
- **LangChain** - LLM uygulama iskeleti (Framework)
- **OpenAI GPT-4o-mini** - Maliyet-etkin, yüksek performanslı dil modeli
- **LangSmith** - LLM uygulamaları için gözlem, test ve değerlendirme (Monitoring & Evaluation) platformu
- **Python-dotenv** - Çevre değişkenlerinin (Environment variables) güvenli yönetimi

## 📂 Proje Yapısı

```text
├── main.py        # Uygulamanın ana başlangıç dosyası (LCEL Zinciri, Model tanımları)
├── .env           # API anahtarları ve yapılandırma ayarları (git'e eklenmez)
└── README.md      # Proje dokümantasyonu
```

## 📦 Kurulum ve Yapılandırma Adımları

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayınız:

### 1. Projeyi Klonlayın ve Klasöre Geçin
```bash
git clone <proje-repo-url>
cd LangSmith
```

### 2. Gerekli Kütüphaneleri Yükleyin
Projenin bağımlılıklarını kurmak için terminalinizde şu komutu çalıştırın:
```bash
pip install langchain langchain-openai python-dotenv
```

### 3. Çevre Değişkenlerini (Environment Variables) Ayarlayın
Proje ana dizininde `.env` adında bir dosya oluşturun ve OpenAI ile LangSmith API anahtarlarınızı bu dosyaya ekleyin:

```env
# OpenAI API Konfigürasyonu
OPENAI_API_KEY=sk-proj-sizin_openai_anahtariniz

# LangSmith Konfigürasyonu
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_pt_sizin_langsmith_anahtariniz
LANGCHAIN_PROJECT="SeyahatAsistani_Test"
```
*(Not: `LANGCHAIN_TRACING_V2=true` ayarı, uygulamanın çalışırken otomatik olarak LangSmith'e veri göndermesini sağlar.)*

### 4. Uygulamayı Çalıştırın
Tüm ayarları tamamladıktan sonra ana betiği çalıştırabilirsiniz:
```bash
python main.py
```
*(Varsayılan olarak "Floransa" şehri için plan hazırlanacaktır. İsterseniz `main.py` içerisindeki `sehir_input` değişkenini değiştirerek farklı şehirleri test edebilirsiniz.)*

---

## 🔍 LangSmith Analizleri ve Test Süreçleri

Bu projenin geliştirme aşamasında LangSmith üzerinden aşağıdaki test ve değerlendirme işlemleri uygulanmıştır:

1. **Performans Takibi:** "Floransa" şehri için atılan istek sonucunda, GPT-4o-mini modelinin yanıt süresi, toplam harcanan token miktarı ve sorgu maliyeti başarılı bir şekilde analiz edilmiştir.
2. **Hata Yakalama (Error Tracking):** Test aşamasında bilerek geçersiz model isimleri verilerek sistemin hata davranışları incelenmiş ve LangSmith'in sağladığı "Trace" kayıtları üzerinden problemler saniyeler içinde çözümlenmiştir.
3. **Playground Üzerinden Prompt Optimizasyonu:** Uygulama kodu değiştirilmeden, LangSmith Playground arayüzü kullanılarak farklı prompt denemeleri yapılmıştır (örneğin; *"Sadece 3 cümle ile özetle"*). Bu sayede maliyet ve kalite açısından en uygun prompt yapısına karar verilmiştir.

---

## 👨‍💻 Geliştirici

**Oğulcan Narin**  
*AI & Automation Engineer* vizyonuyla hazırlanmıştır.
