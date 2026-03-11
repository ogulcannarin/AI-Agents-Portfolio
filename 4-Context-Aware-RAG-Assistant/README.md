# 🤖 Context-Aware RAG Assistant

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-black?style=for-the-badge&logo=chroma&logoColor=white)

**Dokümanlarınıza duyarlı, vektör veritabanı destekli gelişmiş soru-cevap asistanı.**

</div>

---

## 📖 Proje Açıklaması

Bu proje, **Retrieval-Augmented Generation (RAG)** teknolojisini kullanarak kullanıcıların yüklediği PDF ve TXT dosyalarına dayalı sorular sormasını sağlar. Tahmin yapmak yerine sadece verilen bağlama (context) sadık kalarak güvenilir cevaplar üretir.

## ✨ Özellikler

- **📄 Doküman Yükleme**: PDF ve TXT formatlarında dosya desteği.
- **🔍 Akıllı Arama**: ChromaDB ile vektör tabanlı semantik arama.
- **🤖 Bağlam Farkındalığı**: AI sadece yüklenen dokümanlardaki verileri kullanarak cevap verir (Hallucination önleme).
- **🚀 Yüksek Performans**: FastAPI ile geliştirilmiş asenkron REST API.
- **🎯 Doğruluk Odaklı**: Belge dışı bilgi vermemeye programlanmış sistem promptu.

## 🏗️ Teknoloji Stack

- **Backend**: FastAPI
- **AI Model**: OpenAI GPT-4o-mini
- **Vector Database**: ChromaDB
- **Embedding**: OpenAI text-embedding-3-small
- **PDF İşleme**: pypdf

## 📂 Proje Yapısı

```
4-Context-Aware-RAG-Assistant/
├── app/
│   ├── main.py              # FastAPI endpoint'leri
│   ├── rag.py               # RAG mantığı (embedding, retrieval)
│   └── context_builder.py   # Bağlam yapılandırma
├── requirements.txt         # Bağımlılıklar
└── README.md                # Dokümantasyon
```

## 🚀 Kurulum

### 1. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 2. API Anahtarını Ayarlayın
`.env` dosyası oluşturun:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Uygulamayı Çalıştırın
```bash
uvicorn app.main:app --reload
```
Uygulama `http://localhost:8000` adresinde aktif olacaktır.

## 📚 API Kullanımı

### 📤 Doküman Yükleme
**Endpoint**: `POST /upload`
```bash
curl -X POST "http://localhost:8000/upload" -F "file=@dosya.pdf"
```

### ❓ Soru Sorma
**Endpoint**: `GET /ask?q=SoruMetni`
```bash
curl "http://localhost:8000/ask?q=Dokumanda%20nelerden%20bahsediliyor?"
```

---

## 🔒 Güvenlik ve Doğruluk
Sistem, tahmin yapmayı reddedecek şekilde yapılandırılmış bir sistem promptu kullanır:
> "Sadece verilen dokümanlara dayan. Emin değilsen 'Bilmiyorum' de. Tahmin yapma."

---
**Geliştirici:** Oğulcan Narin
| [GitHub](https://github.com/ogulcannarin) |
