# Model Context Protocol (MCP) Örnekleri 🚀

Bu klasör, **Model Context Protocol (MCP)** kullanılarak geliştirilmiş, farklı işlevlere sahip üç farklı akıllı asistan (Tool/Araç) örneğini içermektedir. Projeler `mcp` (FastMCP) kütüphanesi üzerine inşa edilmiş olup dış bağlantı (API iletişimleri) ve yerel veritabanı (SQLite) entegrasyonlarını pratik senaryolar üzerinden göstermektedir.

## 📂 Dosya Yapısı ve İçerik

Klasör içerisinde üç ana Python senaryosu ve onlara hizmet eden bir veritabanı dosyası bulunmaktadır:

### 1. 🌦️ `api.py` (Akıllı Hava Durumu Asistanı)
Dış dünya verilerini (API aracılığıyla) yapay zeka araçlarına bağlayan temel bir örnektir. 
- Yüksek performanslı `httpx` kütüphanesini kullanarak asenkron HTTP istekleri atar.
- **Araç (Tool):** `hava_durumu_getir(sehir)`
- **İşlevi:** Ücretsiz bir servis olan `wttr.in` kullanarak belirtilen şehrin güncel hava durumunu detaylı metin modeli olarak döndürür.

### 2. 🗄️ `database.py` (Veritabanı Asistanı)
Dil modelleri ve yapay zeka sistemlerine kalıcı bellek kazandıran veri katmanı örneğidir. Gömülü olarak oluşturulan `hafiza.db` (SQLite) veritabanı ile çalışır.
- `init_db()` fonksiyonu ile ilk çalıştırılmada otomatik tablo (`notlar`) kurulumunu yapar.
- **Araç 1:** `not_ekle(icerik)` - Kullanıcıdan veya yapay zekadan gelen bilgileri kalıcı bellek veritabanına kaydeder.
- **Araç 2:** `notlari_listele()` - Veritabanındaki daha önceden kayıt edilmiş tüm notları listeleyip yapay zekanın bağlamına (context) sunar.

### 3. 🤔 `kod.py` (Stratejik Planlayıcı)
Birden fazla aracın tek bir asistan çatısı altında birleşik şekilde çalışmasını gösteren gelişmiş örnektir. Yapay zekanın "Tool Calling" ile araçları zincirleme (Agentic Workflow) kullanmasına imkan tanır.
- **Araç 1:** `hava_durumu_analizi(sehir)` -> *Dış Veri Simülasyonu* (Sıcaklık ve yağış bilgisi).
- **Araç 2:** `planlari_kontrol_et()` -> *Kişisel Bağlam* (Kullanıcı takvimindeki mevcut planlar).
- **Araç 3:** `tavsiye_olustur(durum)` -> *Mantıksal Sentez* (Gelen verileri harmanlayarak bağlama özel nihai bir çıktı hazırlar).

### 4. 🗃️ `hafiza.db`
`database.py` dosyasındaki "Veritabanı Asistanı" araçlarının veri okuma/yazma işlemleri için kullandığı yerel SQLite ilişkisel veritabanı dosyasıdır.

---

## 🛠️ Kurulum Alanı

Uygulamaların sorunsuz çalışabilmesi için projede kullanılan bağımlılıkları yüklemeniz gereklidir:

```bash
# Kütüphaneleri kurmak için:
pip install mcp httpx
# Not: sqlite3 standart Python kütüphanesidir, harici kurulum gerektirmez.
```

## 🚀 Çalıştırma

Modüllerin her biri kendi başına çalıştırılabilir birer FastMCP sunucusudur. Terminal üzerinden dilediğinizi ayağa kaldırabilirsiniz:

```bash
python api.py
# veya
python database.py
# veya
python kod.py
```

## 🧠 Öğrenme Çıktısı
Bu klasördeki örnekler sayesinde; 
1. **Dış Sistemlerle İletişim:** LLM'lerin sadece bildikleriyle değil, API'lerden anlık çektikleri veriyle çalışmasını sağlamayı,
2. **Kalıcı Hafıza (Long-term Memory):** Bir defalık sohbetlerin ötesine geçerek kullanıcı tarihlerine ve girdilerine göre durum bilgilerini (SQLite kullanılarak) kaydetmeyi ve getirmeyi,
3. **Senaryo ve Araç Zincirleme:** Çeşitli küçük araçları bir araya getirerek yapay zekanın bu yapı taşlarını birleştirerek büyük resmi inşa etmesi prensiplerini deneyimlemiş olursunuz.
