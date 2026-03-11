# 🏛️ PROJECT NEXUS: Autonomous Multi-Agent Enterprise

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Latest-00ADD8?style=for-the-badge&logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_AI-Gemini_2.0-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

**Tek bir komutla karmaşık görevleri planlayan ve yürüten, hiyerarşik yapıya sahip otonom bir Yapay Zeka Şirketi simülasyonu.**

</div>

---

## 📖 Proje Hakkında

**Project NEXUS**, modern agentic AI prensiplerini kullanarak karmaşık iş süreçlerini otonomize eden bir sistemdir. Bir "Yönetici Ajan" (Manager), kullanıcıdan gelen yüksek seviyeli istekleri mantıksal alt görevlere böler ve bu görevleri uzman departmanlara dağıtır.

## 🧠 Mimari ve Çalışma Mantığı

Bu proje, **"Hierarchical Planning & Execution"** (Hiyerarşik Planlama ve Yürütme) mimarisini kullanır.

### 👔 1. Yönetim Paneli (Manager)
- **Analiz:** Kullanıcı isteğini (Örn: "Pazar araştırması yap ve rapor yaz") analiz eder.
- **Planlama:** `Pydantic Structured Output` kullanarak isteği adımlara böler ve JSON iş planı oluşturur.
- **Delegasyon:** Her adımı en uygun uzman ajana atar.

### 👥 2. Uzman Departmanlar
- **🌍 Araştırmacı (Researcher):** Tavily API ile internette gerçek zamanlı veri toplar.
- **📊 Analist (Analyst):** Toplanan verilerden stratejik içgörü çıkarır.
- **✍️ Yazar (Writer):** Analizlere dayanarak profesyonel rapor/blog hazırlar.
- **💻 Yazılımcı (Coder):** İlgili görev için Python/HTML/CSS kodu geliştirir.

### 🔄 3. Orkestrasyon (LangGraph)
Ajanlar arasındaki veri akışı ve sıra yönetimi, LangGraph tabanlı bir durum makinesi (State Machine) tarafından dinamik olarak yönetilir.

---

## 🛠️ Teknoloji Yığını

| Bileşen | Teknoloji | Görevi |
| :--- | :--- | :--- |
| **Orkestrasyon** | LangGraph | Ajanlar arası durum (State) yönetimi. |
| **Zeka (LLM)** | Gemini 2.0 Flash | Akıl yürütme ve içerik üretimi. |
| **Arama** | Tavily AI | İnternet etkileşimi ve veri toplama. |
| **Doğrulama** | Pydantic | Plan çıktılarının yapısal doğruluğu. |

---

## 🚀 Kurulum ve Çalıştırma

### 1. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 2. API Anahtarlarını Ayarlayın
`.env` dosyası oluşturun:
```env
GOOGLE_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

### 3. Şirketi Başlatın
```bash
python main.py
```

### 📝 Örnek Görev Talebi
> "Elon Musk'ın xAI şirketi ve Grok modeli hakkında araştırma yap, bunun önemini anlatan kısa bir yazı yaz ve bu yazıyı gösterecek dark mode bir HTML sayfası kodla."

---

## 📂 Proje Yapısı
```
3-NEXUS-Autonomous-Enterprise/
├── main.py              # Ana Orkestrasyon (LangGraph Döngüsü)
├── manager.py           # Yönetici Ajan (Planlama Mantığı)
├── requirements.txt     # Bağımlılıklar
└── README.md            # Dokümantasyon
```

---
**Geliştirici:** Oğulcan Narin | **Project NEXUS**
| [GitHub](https://github.com/ogulcannarin) |