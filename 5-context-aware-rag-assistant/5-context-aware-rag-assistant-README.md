# 5-Context-Aware RAG Assistant

## 📖 Proje Açıklaması

Bu proje, **Retrieval-Augmented Generation (RAG)** teknolojisini kullanarak kullanıcıların yüklediği dokümanlara dayalı sorular sormasını sağlayan yapay zeka destekli bir asistanıdır. FastAPI ile geliştirilmiş bir REST API üzerinden çalışır ve OpenAI'ın GPT-4 modelini kullanır.

## ✨ Özellikler

- **📄 Doküman Yükleme**: PDF ve TXT formatında dosya yükleme
- **🔍 Akıllı Arama**: ChromaDB ile vektör tabanlı benzerlik araması
- **🤖 Bağlam Farkındalığı**: Yüklenen dokümanlara dayalı doğru ve güvenilir cevaplar
- **🚀 Hızlı API**: FastAPI ile yüksek performanslı REST API
- **🎯 Doğruluk Odaklı**: Tahmin yapmak yerine sadece verilen dokümanlara dayalı cevaplar

## 🏗️ Teknoloji Stack

- **Backend**: FastAPI
- **AI Model**: OpenAI GPT-4-mini
- **Vector Database**: ChromaDB
- **Embedding**: OpenAI text-embedding-3-small
- **PDF İşleme**: pypdf
- **Environment Management**: python-dotenv

## 📁 Proje Yapısı

```
ai-assistant/
├── app/
│   ├── __init__.py          # Paket başlatıcı
│   ├── main.py              # FastAPI uygulaması ve endpoint'ler
│   ├── rag.py               # RAG mantığı (embedding, retrieval)
│   └── context_builder.py   # Bağlam oluşturma fonksiyonları
├── .env                     # API anahtarları (git'e eklenmez)
├── .gitignore              # Git ignore kuralları
└── requirements.txt         # Python bağımlılıkları
```

## 🚀 Kurulum

### 1. Repoyu Klonlayın

```bash
git clone https://github.com/ogulcannarin/AI-Agents-Portfolio.git
cd AI-Agents-Portfolio
git checkout 5-context-aware-rag-assistant
```

### 2. Sanal Ortam Oluşturun (Opsiyonel ama Önerilir)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Environment Değişkenlerini Ayarlayın

`.env` dosyası oluşturun ve OpenAI API anahtarınızı ekleyin:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Uygulamayı Çalıştırın

```bash
uvicorn app.main:app --reload
```

Uygulama `http://localhost:8000` adresinde çalışacaktır.

## 📚 API Kullanımı

### 1. Doküman Yükleme

**Endpoint**: `POST /upload`

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_document.pdf"
```

**Desteklenen Formatlar**: PDF, TXT

**Yanıt**:
```json
{
  "status": "Doküman eklendi!"
}
```

### 2. Soru Sorma

**Endpoint**: `GET /ask?q=your_question`

```bash
curl "http://localhost:8000/ask?q=Bu%20dökümanda%20hangi%20konular%20var?"
```

**Yanıt**:
```json
{
  "answer": "Dokümanda şu konular bulunmaktadır: ..."
}
```

## 🔧 Nasıl Çalışır?

1. **Doküman Yükleme**:
   - Kullanıcı PDF veya TXT dosyası yükler
   - Metin 500 karakterlik parçalara bölünür (chunking)
   - Her parça OpenAI embedding modeli ile vektöre dönüştürülür
   - Vektörler ChromaDB'de saklanır

2. **Soru Sorma**:
   - Kullanıcı bir soru sorar
   - Soru aynı embedding modeli ile vektöre dönüştürülür
   - ChromaDB'de en benzer 3 doküman parçası bulunur
   - Bu parçalar ve soru, GPT-4'e bağlam olarak gönderilir
   - AI sadece verilen bağlama dayanarak cevap verir

## 🎯 Öne Çıkan Özellikler

### Doğruluk Odaklı Sistem Promptu

Sistem, tahmin yapmak yerine sadece verilen dokümanlara dayanır:

```python
Rol: Sen doğruluk odaklı bir AI asistanısın.

Kurallar:
- Sadece verilen dokümanlara dayan
- Tahmin yapma
- Emin değilsen "Bilmiyorum" de
- Maksimum 3 cümle
- Türkçe cevap ver
```

## 🔒 Güvenlik

- `.env` dosyası `.gitignore` ile korunur
- API anahtarları asla repository'e eklenmez
- Kullanıcı verilerini sadece yerel ChromaDB instance'ında saklar

## 🛠️ Geliştirme

### Test Etmek İçin

```bash
# FastAPI otomatik dokümantasyonu
http://localhost:8000/docs
```

### Değişiklik Yaparken

```bash
# Hot reload aktif - değişiklikler otomatik yansır
uvicorn app.main:app --reload
```

## 📝 Gereksinimler

- Python 3.7+
- OpenAI API anahtarı

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Branch'i push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📄 Lisans

Bu proje açık kaynaklıdır.

## 👤 Geliştirici

**Oğulcan Narin**

- GitHub: [@ogulcannarin](https://github.com/ogulcannarin)

## 🙏 Teşekkürler

Bu proje aşağıdaki harika teknolojileri kullanmaktadır:
- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://openai.com/)
- [ChromaDB](https://www.trychroma.com/)

---

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!
