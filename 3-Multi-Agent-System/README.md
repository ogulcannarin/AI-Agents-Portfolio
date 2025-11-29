# 🤖 Multi-Agent Kod Fabrikası

Bu proje, LangGraph kullanarak iki ajanın (Yazılımcı ve Testçi) işbirliği içinde Python kodu üretmesini sağlayan bir multi-agent sistemdir.

## 🎯 Özellikler

- **Yazılımcı Ajan**: Kullanıcının talebi doğrultusunda Python kodu üretir
- **Testçi Ajan**: Üretilen kodu inceler, hata ve eksiklikleri tespit eder
- **Otomatik İyileştirme**: Testçi hata bulursa, yazılımcı kodu otomatik düzeltir
- **İteratif Süreç**: Kod onaylanana kadar döngü devam eder (max 3 tur)

## 🏗️ Mimari

```
Kullanıcı Talebi
    ↓
Yazılımcı Ajan (Kod Üretir)
    ↓
Testçi Ajan (Kod İnceler)
    ↓
  ┌─────┴─────┐
  │           │
ONAY         RET
  │           │
BİTİŞ    ← ─ ─┘
       (Tekrar Yazılımcıya)
```

## 📦 Kurulum

1. Sanal ortam oluşturun:
```bash
python -m venv venv
```

2. Sanal ortamı aktifleştirin:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

4. `.env` dosyasını düzenleyin ve Google API anahtarınızı ekleyin:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

## 🚀 Kullanım

### Backend'i Başlatın

```bash
uvicorn main:app --reload --port 8000
```

### Frontend'i Açın

Tarayıcınızda `index.html` dosyasını açın veya:

```bash
# Python ile basit HTTP sunucusu
python -m http.server 8080
```

Ardından http://localhost:8080 adresine gidin.

## 🔧 API Endpoints

### POST /generate-code
Kod üretme talebi gönderir.

**Request:**
```json
{
  "gorev": "Fibonacci serisini hesaplayan bir fonksiyon yaz"
}
```

**Response:**
```json
{
  "kod": "def fibonacci(n):\n    ...",
  "durum": "ONAY",
  "tur_sayisi": 2
}
```

### GET /
Sistem durumunu kontrol eder.

### GET /health
Sağlık kontrolü yapar.

## 📁 Proje Yapısı

```
3-Multi-Agent-System/
├── main.py              # FastAPI backend
├── index.html           # Web arayüzü
├── ders9_multi_agent.py # Orijinal konsol versiyonu
├── requirements.txt     # Python bağımlılıkları
├── .env                 # Çevre değişkenleri
├── .gitignore          # Git ignore kuralları
└── README.md           # Bu dosya
```

## 🎨 Özellikler

- Modern ve responsive web arayüzü
- Gradient tasarım
- Gerçek zamanlı loading göstergesi
- Hata yönetimi
- Kod syntax highlighting
- İterasyon sayısı takibi

## 🔑 Gereksinimler

- Python 3.9+
- Google AI API anahtarı
- Modern web tarayıcısı

## 📝 Lisans

MIT License

## 👨‍💻 Geliştirici

Agentic AI Portfolio Projesi
