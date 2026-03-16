# Robust Auditor: Hata Toleranslı MCP Sunucusu

Bu proje, dış sistemlerden gelebilecek dosya odaklı isteklere karşı hata toleransı (error-handling) en üst düzeye çıkarılmış ve akademik loglama standartlarına uyarlanmış güvenli bir Model Context Protocol (MCP) sunucusudur. `FastMCP` üzerine inşa edilmiştir.

## 🛡️ Özellikler

- **Güvenli Dosya Analizi (`safe_file_analyzer`):** Gelen dosya yollarında boş içerik, eksik dosya veya okuma izinlerine dair kontroller barındırır.
- **Güçlü Hata Yönetimi `Try/Except`:**
  - `FileNotFoundError`: İstenen dosya yolda olmadığında kullanıcı dostu hata döndürür.
  - `PermissionError`: Sistemin erişim hakkı olmayan dosyalarda kritk uyarı mekanizmasını çalıştırır.
  - `Exception`: Beklenmedik tüm davranışlar kapsanmıştır.
- **Akademik Loglama:** Eylemler terminal ve host uygulamanıza standart `logging` hiyerarşisi (`INFO`, `WARNING`, `ERROR`, `CRITICAL`) eşliğinde bildirilir.

## 🚀 Nasıl Çalışır?

Sunucu, MCP protokolünü kullanarak Host (Claude vb.) ve bağımsız araçlar için "RobustAuditor" adıyla arayüz sunar. Sunucu içerisindeki ana araç:

- **Araç:** `safe_file_analyzer(file_path)`
- **Açıklama:** İstenilen dosyanın içini okuyup karakter boyutu üzerinden analiz sonucunu döndürür. Olası bütün teknik aksaklıklara düzgün yazılı yanıtlar verir.

## 🛠️ Kurulum ve Kullanım

`FastMCP` kütüphanesinin dev ortamınıza yüklü olduğundan emin olun:
```bash
pip install mcp
```

MCP Sunucusunu bağımsız olarak ayağa kaldırmak için:
```bash
python robust_auditor.py
```
*(MCP Client uygulamaları doğrudan bu script'i executable olarak ekleyecek şekilde çalışır).*
