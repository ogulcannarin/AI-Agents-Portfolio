# Advanced Tool Patterns: Project Repository Analyzer

Bu proje, yerel dosya analiz yöntemlerini Büyük Dil Modelleri (LLM'ler) ile birleştirerek bir kod deposunu (repository) otomatik olarak tarayan, analiz eden ve hakkında rapor çıkartan bir araç kümesi sunar.

## 🚀 Özellikler

- **Dosya Tarama (`tools.py`):** Belirtilen bir dizindeki dosyaları tarar, dosya boyutlarını (KB cinsinden) ve uzantılarını listeler.
- **Temel Metrik Analizi (`analyzer.py`):** Taranan dosyalar üzerinden toplam dosya sayısı, Python ve veri dosyalarının sayısı ve en büyük dosya gibi temel istatistikleri çıkarır.
- **LLM Entegrasyonu (`llm_analyzer.py`):** Çıkartılan raporu `OpenAI` API'sine göndererek GPT modelinden projenin ne tür bir amaca hizmet ettiğine dair profesyonel bir yorum alır.
- **Modüler Yapı (`main.py`):** Tüm bileşenleri bir araya getirerek uçtan uca çalıştırılabilir ve okunabilir bir süreç oluşturur.

## 📁 Kod Dizini

- `main.py`: Uygulamanın giriş noktasıdır. Diğer modülleri çağırarak analizi başlatır ve sonuçları yazdırır.
- `tools.py`: Yerel dosya sistemini okumak ve taramakla ilgilenir (`scan_repository`).
- `analyzer.py`: Dosya metriklerinden istatistiksel rapor (`analyze_project`) elde eder.
- `llm_analyzer.py`: OpenAI modeline dinamik prompt göndererek projeyle ilgili uzman yorumu üretir.
- `test_repo/`: (Varsa) Araçların test edilmesi için oluşturulmuş örnek depo.

## 🛠️ Kurulum ve Kullanım

1. Gerekli kütüphanelerin yüklü olduğundan emin olun (Örn: `openai`, `python-dotenv`).
2. Kök dizinde (veya klasör içinde) bir `.env` dosyası oluşturun ve OpenAI API anahtarınızı ekleyin:
   ```env
   OPENAI_API_KEY=sk-...
   ```
3. Uygulamayı çalıştırın:
   ```bash
   python main.py
   ```
