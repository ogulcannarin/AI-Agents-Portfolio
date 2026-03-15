# 🧠 PromptServer: Gelişmiş Kod Analiz Ajani (MyLocalAgent)

Bu klasördeki `promt.py` scripti, yapay zeka entegrasyonlarını en üst seviyeye taşıyan özelliklere sahip gelişmiş bir **Model Context Protocol (MCP)** sunucusudur. Araçlara (Tools), kaynaklara (Resources) ve en önemlisi spesifik **Prompt Şablonlarına (Prompt Templates)** ev sahipliği yapar.

> ⚠️ **Uyarı:** Sunucu adı "MyLocalAgent" olarak belirlenmiştir. Eğer `MyServer` klasöründeki proje ile aynanda çalıştırılırsa çakışma yaşanabilir; izole çalıştırmanız önerilir.

## 📖 Projenin Amacı
Modelin sadece sizin emirlerinizi yerine getiren bir aracı değil; bir **"Uzman Yazılım Mimarı"** gibi inisiyatif alarak kodları analiz etmesini, klasör okumasını, dosya içlerine temas edip denetim işlemlerini (Audit) yapmasını sağlamaktır.

## ✨ Öne Çıkan Özellikler

### 1. Etkileşimli Araçlar (Interactive Tools)
Sadece listeleme yapmakla kalmaz, aynı zamanda kod içeriklerini okur:
- `list_files(path=".")`: Belirtilen dizin içerisindeki varlıkları listeler.
- `read_file(path)`: **(Yeni!)** Belirtilen bir dosyanın veya kod betiğinin UTF-8 formatında içeriklerini tamamen okuyup, modelin analiz edebileceği dizgesel (string) bir yapıya dönüştürür.

### 2. Özelleştirilmiş Komut Şablonu (Prompt Template)
Bu projenin amiral gemisi olan özelliktir. Yapay zekanın yeteneklerini çerçeveleyip spesifik durumlarda ona karakter kazandırır:
- **`analyze-code` Prompt'u**: LLM'in kendisine verilen kodu şu 3 temel endüstriyel standartta denetlemesi için özel bir yönlendirme içerir:
  1. **Güvenlik Açıkları (Security):** Olası veri sızdırma, Injection veya güvenlik problemlerini taratır.
  2. **Performans İyileştirmeleri:** Kodun bellekte veya CPU'da yaratabileceği darboğazları çözümler.
  3. **Pythonic Kurallar (PEP8):** Sadece çalışan değil, "temiz ve endüstri standartlarında okunabilir" kod yapısını analiz etmeye zorlar.

### 3. Sistem Kaynakları (Resources)
Modelin durumsal farkındalığı için:
- `system://info`: İşletim Sistemi platformu ve versiyon bilgisini sunarak doğru çıktı formatı (örn. işletim sistemine özel dosya yolu ayırıcıları) oluşturulmasına zemin hazırlar.

## ⚙️ Nasıl Çalıştırılır?
```bash
python promt.py
```
Sunucu çalışırken, istemci (Claude, yapay zeka asistanı vs.) bu sunucudaki `analyze-code` prompt şablonunu tetikleyerek herhangi bir kod parçasını mimari bir denetimden (Code Review) geçirebilir.
