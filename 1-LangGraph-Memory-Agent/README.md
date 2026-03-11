# 🧠 LangGraph Hafıza Ajanı (Memory Agent)

Bu proje, **LangGraph** framework'ü kullanılarak geliştirilmiş, kalıcı hafıza (persistence) ve PDF doküman analizi yeteneklerine sahip akıllı bir yapay zeka asistanıdır.

## ✨ Özellikler

- **💾 Kalıcı Hafıza**: `SqliteSaver` kullanarak kullanıcı konuşmalarını veritabanında saklar. Uygulama kapansa bile `thread_id` üzerinden eski konuşmaları hatırlar.
- **📄 PDF Analizi**: Yüklenen PDF (Örn: CV) dosyalarını okur ve içeriği hakkında sorulan soruları cevaplar.
- **🌍 Dinamik Web Araması**: Eğer sorulan sorunun cevabı dokümanda yoksa, ajan otomatik olarak **Tavily AI** üzerinden internette araştırma yapar.
- **🤖 Akıllı Yönlendirme**: LangGraph `StateGraph` mimarisi ile kararlar alır (Doküman mı? Web mi? Sohbet mi?).
- **🚀 FastAPI Backend**: Modern ve hızlı asenkron API desteği.

## 🏗️ Mimari

Ajanın çalışma mantığı şu hiyerarşiyi takip eder:
1. **Giriş**: Kullanıcı sorusu alınır.
2. **CV Kontrol Düğümü (Node)**: PDF okunur, LLM içeriği analiz eder.
3. **Karar Mekanizması**: Eğer bilgi PDF'te varsa cevap döner, yoksa Web Arama düğümüne yönlendirir.
4. **Web Arama Düğümü**: Tavily API ile internetten güncel veri çeker.
5. **Çıkış**: Sonuç kullanıcıya iletilir ve hafızaya kaydedilir.

## 📂 Dosya Yapısı

- `main.py`: FastAPI backend ve LangGraph mantığı.
- `index.html`: Kullanıcı arayüzü (Frontend).
- `hafiza.sqlite`: Konuşma geçmişinin saklandığı veritabanı.
- `ornek_cv.pdf`: Ajanın analiz ettiği örnek doküman.

## 🚀 Başlangıç

### 1. Bağımlılıkları Yükleyin
```bash
pip install fastapi uvicorn langchain-google-genai langgraph tavily-python pypdf python-dotenv
```

### 2. API Anahtarlarını Ayarlayın
`.env` dosyası oluşturun:
```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 3. Uygulamayı Çalıştırın
```bash
python main.py
```
Uygulama başladıktan sonra `index.html` dosyasını tarayıcınızda açarak ajanla konuşmaya başlayabilirsiniz.

## 🛠️ Kullanılan Teknolojiler
- **LangGraph**: Durum yönetimi ve iş akışı.
- **Google Gemini 2.0 Flash**: Ana dil modeli.
- **SQLite**: Kalıcı hafıza deposu.
- **Tavily AI**: Gerçek zamanlı web arama motoru.

---
**Geliştirici:** Oğulcan Narin
