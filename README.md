# 🤖 Yapay Zeka Ajanları Portföyü (AI Agents Portfolio)

Yapay Zeka Ajanları Portföyüme hoş geldiniz! Bu depo, detaylı analitik düşünebilen, kendi kendine plan yapabilen, çeşitli araçlar (tools) kullanabilen ve karmaşık görevleri otonom olarak yürütebilen **Yeni Nesil Yapay Zeka Ajanlarının (AI Agents)** pratik uygulamalarını sergilemektedir. 

Projelerde **LangChain**, **LangGraph**, **Model Context Protocol (MCP)**, **ReAct Mimarisi** ve **RAG (Retrieval-Augmented Generation)** gibi endüstri standardı framework ve mimariler kullanılmıştır.

---

## 📋 İçindekiler

- [🎯 Genel Bakış](#-genel-bakış)
- [📂 Projeler ve Klasör Yapısı](#-projeler-ve-klasör-yapısı)
- [🛠️ Kullanılan Teknolojiler (Teknoloji Yığını)](#️-kullanılan-teknolojiler-teknoloji-yığını)
- [🎬 Başlangıç ve Kurulum](#-başlangıç-ve-kurulum)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)
- [📝 Lisans](#-lisans)

---

## 🎯 Genel Bakış

Yapay zeka asistanlarının sadece metin ürettiği günlerden, hedeflere ulaşmak için eyleme geçtiği günlere geçiş yapıyoruz. Bu portföy, tekil ajan mantıklarından (Single-Agent) karmaşık iş gücü hiyerarşilerine (Multi-Agent Systems) kadar geniş bir yelpazede geliştirilmiş sistemleri barındırmaktadır. Her bir klasör, farklı bir yeteneği (Hafıza, Planlama, Araç Kullanımı, Dış Dünya İletişimi) ön plana çıkarmaktadır.

---

## 📂 Projeler ve Klasör Yapısı

Depo içerisindeki tüm projeler aşağıda numaralandırılarak veya isimlendirilerek listelenmiştir. Her projenin kendi klasörü içerisinde detaylı bir `README.md` dosyası bulunmaktadır.

### 1. [LangGraph Hafıza Ajanı](./1-LangGraph-Memory-Agent) 🧠
Kalıcı hafızaya (persistence) ve gelişmiş analiz yeteneklerine sahip LangGraph tabanlı akıllı asistan.
- **Odak Noktası:** Geçmiş diyalogları unutmayan (SQLite tabanlı State Management) yapı.
- **Kabiliyetleri:** PDF doküman mimarilerini anlama, Tavily API ile gerçek zamanlı web araştırması.

### 2. [Çok Ajanlı Kod Fabrikası](./2-Multi-Agent-System) 🏭
Geliştirici ve test uzmanı ajanların işbirliği içinde yazılım ürettiği simülasyon.
- **Odak Noktası:** Farklı görevlere sahip ajanların birbirini denetlemesi (Actor-Critic).
- **Kabiliyetleri:** Otomatik kod inceleme, otonom refactoring süreçleri, Docker orkestrasyonu.

### 3. [NEXUS: Otonom Kurumsal Sistem](./3-NEXUS-Autonomous-Enterprise) 🏢
Hiyerarşik planlama yapabilen, yönetici sıfatlı bir ajanın diğer uzman ajanları koordine ettiği sistem.
- **Odak Noktası:** Pydantic Structured Outputs ile kesin kuralcı görev dağılımı.
- **Kabiliyetleri:** Kompleks hedefleri alt görevlere bölme, araştırma ve analiz süreçlerinin otomasyonu.

### 4. [Context-Aware RAG Asistanı](./4-Context-Aware-RAG-Assistant) 📚
Kendi verileriniz üzerinde bağlamı kaybetmeden gezinmeyi sağlayan LLM entegrasyonu.
- **Odak Noktası:** Vektör arama tabanlı, halüsinasyonları önleyen Retrieval Augmented Generation mimarisi.
- **Kabiliyetleri:** ChromaDB ile yüksek hızlı metin aramaları, karmaşık PDF analizleri.

### 5. [AWS Çoklu Ajan Haber Ajansı](./5-AWS-Multi-Agent-News) 📰 *(Geliştirme Aşamasında)*
Gerçek zamanlı haber üreten ve AWS ortamında yayına hazır olacak şekilde tasarlanan mimari.
- **Odak Noktası:** Cloud Native, mikroservis odaklı yapı.
- **Planlanan:** Haber kazıma (web scraping), PostgreSQL medya arşivi.

### 6. [Mini Otonom Yapay Zeka Ajanı (AutoGPT Mantığı)](./6-AutoGen) ⚙️
Tam otonom olarak `ReAct` (Düşünce ve Eylem) felsefesiyle döngüsel çalışan Mini AutoGPT.
- **Odak Noktası:** Bir hedefe ulaşana kadar dış dünyadan veri çekme ve kendi kendine plan yapma.
- **Kabiliyetleri:** Dinamik araç kullanımı (DuckDuckGo Search) ve Reasoning süreçleri.

### 7. [Model Context Protocol (MCP) Uygulamaları](./7-MCP) 🔌
MCP standardı kullanılarak dış dünya veritabanları (SQLite) ve API'lerinin yapay zekaya açıldığı asistanlar.
- **Odak Noktası:** Anthropic'in tanıttığı MCP protokolünün pratik, saf Python uygulamaları.
- **Kabiliyetleri:** Asenkron veri çekme, SQLite gömülü veritabanı ile uzun dönemli (Long-term) etkileşim.

### 8. [ReAct ve Reflection Ajanı](./8-ReAct-Reflection) 🪞
Bir dil modelinin ürettiği sonucu dış dünyaya sunmadan önce kendi kendine "iç kalite kontrolünden" (Reflection) geçirdiği simülasyon.
- **Odak Noktası:** Hata payını sıfıra indirmeyi amaçlayan, modelin kendi çıktısını eleştiriye tutma mantığı.
- **Kabiliyetleri:** Halüsinasyon azaltma, hatalı API dönüşlerini yakalama ve otonom retry (yeniden deneme) mekanizmaları.

---

## 🛠️ Kullanılan Teknolojiler (Teknoloji Yığını)

Projelerin geneline yayılan teknolojik altyapı:

- **Orkestrasyon & Frameworks:** LangChain, LangGraph, FastAPI, FastMCP, Flask
- **Büyük Dil Modelleri (LLM):** Google Gemini 2.0 Serisi, OpenAI GPT-4o & GPT-4o-mini
- **Hafıza & Veritabanı:** 
  - Vektör Veritabanı: ChromaDB
  - İlişkisel Veritabanı: PostgreSQL, SQLite
- **Özel Araçlar (Tools):** Tavily AI (İnternet Arama), BeautifulSoup4, DuckDuckGo Search
- **DevOps & Dağıtım:** Docker, Docker Compose, AWS Servisleri (Hazırlık)
- **Ana Diller:** Python 3.9+, Minimal JavaScript ve HTML/CSS

---

## 🎬 Başlangıç ve Kurulum

Her alt proje özerk bir yapıya sahiptir. Seçtiğiniz projenin klasörüne giderek o projeye ait `README.md` dosyasını okuyunuz. 

Genel geçerli adımlar aşağıda belirtilmiştir:

1. **Repoyu Klonlayın:**
   ```bash
   git clone https://github.com/ogulcannarin/AI-Agents-Portfolio.git
   cd AI-Agents-Portfolio
   ```

2. **Gereksinimleri Yükleyin:**
   İncelemek istediğiniz projenin klasörüne girin (Örn: `cd MCP`) ve bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
   *(Eğer sadece tek bir betik varsa örnek bir sanal ortam oluşturup dosyada istenen kütüphaneleri `pip install` ile manuel kurabilirsiniz.)*

3. **Çevre Değişkenleri (`.env`):**
   Uygulamalar büyük oranda OpenAI veya Gemini API anahtarlarına ihtiyaç duyar. Klasörde bir `.env` oluşturup anahtarlarınızı girin:
   ```env
   OPENAI_API_KEY=sk-...
   GEMINI_API_KEY=AIza...
   ```

4. **Uygulamayı Başlatın:**
   `python app.py` veya `python main.py` ile sistemi başlatabilirsiniz.

---

## 🤝 Katkıda Bulunma

Bu repo, Yapay Zeka Ajanları mimarilerinde yeni teknikler keşfetmeyi amaçlayan eğitim odaklı bir portföydür. Hata bildirimleriniz (Issues), yeni araç (Tool) fikirleriniz ve doğrudan katkılarınız (Pull Requests) son derece değerlidir!

## 📝 Lisans

Bu proje, açık kaynak topluluğuna katkı sağlamak amacıyla [MIT Lisansı](LICENSE) altında sunulmaktadır.

---
**Oğulcan Narin** | [GitHub](https://github.com/ogulcannarin) | [LinkedIn](https://linkedin.com/in/ogulcannarin)

⭐ *Eğer projeler yapay zeka serüveninizde ufkunuzu açtıysa github üzerinden yıldız vermeyi unutmayın!* 
