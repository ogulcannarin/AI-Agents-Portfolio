# 🤖 Yapay Zeka Ajanları Portföyü

Yapay Zeka Ajanları Portföyüme hoş geldiniz! Bu repo, **LangChain**, **LangGraph** ve **Multi-Agent Sistemler** gibi en güncel framework'ler kullanılarak geliştirilmiş akıllı ajanların pratik uygulamalarını sergiliyor.

## 📋 İçindekiler

- [Genel Bakış](#genel-bakış)
- [Projeler](#projeler)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Başlangıç](#başlangıç)
- [Proje Yapısı](#proje-yapısı)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## 🎯 Genel Bakış

Bu portföy, düşünebilen, planlayabilen ve görevleri yürütebilen akıllı ve otonom yapay zeka ajanları oluşturma konusundaki uzmanlığımı göstermektedir. Her proje, basit ReAct kalıplarından karmaşık çok ajanlı orkestrasyonlara kadar ajansal yapay zeka sistemlerinin farklı yönlerini sergiliyor.

## 🚀 Projeler

### 1. LangChain ReAct Ajanı
LangChain'in ReAct (Akıl Yürütme + Eylem) kalıbıyla oluşturulmuş sofistike bir ajan. Bu ajan:
- Problemler hakkında adım adım akıl yürütebilir
- Bilgi toplamak için harici araçları kullanabilir
- Gözlemlere dayalı kararlar alabilir
- Otonom olarak eylemler gerçekleştirebilir

**Temel Özellikler:**
- Araç entegrasyonu (web araması, hesaplamalar vb.)
- Adım adım akıl yürütme şeffaflığı
- Hata işleme ve kurtarma

### 2. LangGraph Hafıza Ajanı
Kalıcı hafıza ile durum bilgisi içeren konuşmalar için LangGraph kullanan gelişmiş bir ajan. Bu ajan:
- Birden fazla etkileşim boyunca bağlamı korur
- Graf tabanlı iş akışı yönetimi kullanır
- Karmaşık karar ağaçları uygular
- Tutarlı, bağlama duyarlı yanıtlar sağlar

**Temel Özellikler:**
- Oturumlar arası kalıcı hafıza
- Graf tabanlı durum yönetimi
- Çok turlu konuşma işleme
- Dinamik iş akışı adaptasyonu

### 3. Çoklu Ajan Sistemi
Karmaşık problemleri çözmek için birlikte çalışan birden fazla uzmanlaşmış ajanın olduğu işbirlikçi bir sistem. Özellikler:
- **Orkestratör Ajan**: Uzmanlaşmış ajanlar arasında görevleri koordine eder
- **Araştırma Ajanı**: Bilgi toplar ve analiz eder
- **Planlama Ajanı**: Yapılandırılmış planlar ve stratejiler oluşturur
- **Yürütme Ajanı**: Planlara dayalı çözümleri uygular

**Temel Özellikler:**
- Ajanlar arası iletişim
- Görev ayrıştırma ve delegasyonu
- İşbirlikçi problem çözme
- Gerçek zamanlı etkileşim için web arayüzü

## 🛠️ Kullanılan Teknolojiler

- **Python 3.8+**: Temel programlama dili
- **LangChain**: LLM uygulamaları oluşturmak için framework
- **LangGraph**: Ajansal iş akışları için durum yönetimi
- **Groq API**: Hızlı LLM çıkarımı
- **Tavily API**: Web arama yetenekleri
- **Flask**: Çoklu ajan sistemi için web framework'ü
- **HTML/CSS/JavaScript**: Frontend arayüzleri

## 🎬 Başlangıç

### Gereksinimler

- Python 3.8 veya üzeri
- API Anahtarları:
  - [Groq API Anahtarı](https://console.groq.com/)
  - [Tavily API Anahtarı](https://tavily.com/)

### Kurulum

1. **Repository'yi klonlayın**
   ```bash
   git clone https://github.com/ogulcannarin/AI-Agents-Portfolio.git
   cd AI-Agents-Portfolio
   ```

2. **Bağımlılıkları yükleyin**
   
   Her projenin kendi bağımlılıkları vardır. İlgili proje klasörüne gidin ve yükleyin:
   
   ```bash
   # Herhangi bir proje için
   cd 1-LangChain-ReAct-Agent  # veya 2-LangGraph-Memory-Agent veya 3-Multi-Agent-System
   pip install -r requirements.txt
   ```

3. **Ortam değişkenlerini ayarlayın**
   
   Her proje dizininde bir `.env` dosyası oluşturun:
   
   ```env
   GROQ_API_KEY=buraya_groq_api_anahtarınız
   TAVILY_API_KEY=buraya_tavily_api_anahtarınız
   ```

4. **Projeyi çalıştırın**
   
   ```bash
   # Python tabanlı ajanlar için
   python main.py
   
   # Web arayüzlü Çoklu Ajan Sistemi için
   cd 3-Multi-Agent-System
   python main.py
   # Ardından tarayıcınızda http://localhost:5000 adresini açın
   ```

## 📁 Proje Yapısı

```
AI-Agents-Portfolio/
│
├── 1-LangChain-ReAct-Agent/
│   ├── main.py              # Ana ajan implementasyonu
│   ├── requirements.txt     # Python bağımlılıkları
│   └── README.md           # Projeye özel dokümantasyon
│
├── 2-LangGraph-Memory-Agent/
│   ├── main.py              # Hafıza özellikli ajan
│   ├── requirements.txt     # Python bağımlılıkları
│   └── README.md           # Projeye özel dokümantasyon
│
├── 3-Multi-Agent-System/
│   ├── main.py              # Çoklu ajan orkestrasyonu ile Flask backend
│   ├── index.html           # Web arayüzü
│   ├── requirements.txt     # Python bağımlılıkları
│   └── README.md           # Projeye özel dokümantasyon
│
├── .gitignore              # Git ignore kuralları
└── README.md               # Bu dosya
```

## 💡 Kullanım Senaryoları

- **Otomatik Araştırma**: Bilgi arayabilen, analiz edebilen ve özetleyebilen ajanlar
- **Görev Planlama**: Karmaşık görevleri eyleme dönüştürülebilir adımlara ayıran yapay zeka sistemleri
- **Karar Verme**: Problemler üzerinde akıl yürüten akıllı ajanlar
- **İşbirlikçi Yapay Zeka**: Karmaşık problemler üzerinde birlikte çalışan birden fazla ajan

## 🤝 Katkıda Bulunma

Katkılar, sorunlar ve özellik istekleri memnuniyetle karşılanır! [Issues sayfasını](https://github.com/ogulcannarin/AI-Agents-Portfolio/issues) kontrol etmekten çekinmeyin.

## 📝 Lisans

Bu proje [MIT](LICENSE) lisansı altındadır.

## 📧 İletişim

**Oğulcan Narin**
- GitHub: [@ogulcannarin](https://github.com/ogulcannarin)
- LinkedIn: [LinkedIn Profiliniz](https://linkedin.com/in/yourprofile)

---

⭐ Bu repository'yi yararlı buluyorsanız, lütfen yıldız vermeyi düşünün!

**LangChain, LangGraph ve en güncel yapay zeka teknolojileri ile ❤️ ile geliştirildi**
