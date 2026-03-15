# 🚀 MyServer: Temel MCP Yetenekleri (MyLocalAgent)

Bu klasör, AI asistanlarına dış dünyayla ("Local Environment") etkileşime geçme becerisi kazandıran temel **Model Context Protocol (MCP)** sunucusunu barındırmaktadır.

## 📖 Projenin Amacı
Büyük Dil Modelleri (LLM) varsayılan olarak cihazınızın dosyalarına veya sistem durumuna erişemezler. `my_server.py`, modern **FastMCP** mimarisini kullanarak modelinize özel erişim yetkileri veren bir köprü (Agent) oluşturur.

## ✨ Öne Çıkan Özellikler

### 1. Sistem Kaynakları (Resources)
Modeller için bir "Salt Okunur (Read-Only)" veri akışı sağlar:
- `system://info`: Kod, bu kaynak aracılığıyla asistanın üzerinde çalıştığı ana makinenin (host) İşletim Sistemi ve Versiyon bilgilerini okumasına olanak tanır.
  *Kullanım Senaryosu:* "Bana bir PowerShell veya Bash scripti oluştur" dendiğinde, Model bu kaynağa bakarak Windows'ta mı yoksa Linux/Mac'te mi olduğuna karar verebilir.

### 2. Araçlar (Tools)
Modele aksiyon alabilme veya dışarıdan bilgi sorgulayabilme gücü verir:
- `list_files(path=".")`: Modelin, cihazınızdaki klasör hiyerarşisini listelemesini sağlar. Böylece model klasör içeriklerini analiz edebilir ve size detaylı bir döküm sunabilir. Güvenlik önlemi olarak hata yönetimi (try-except) dahil edilmiştir.

## ⚙️ Nasıl Çalıştırılır?
Sunucuyu başlatmak için aşağıdaki komutu kullanabilirsiniz:
```bash
python my_server.py
```
Sunucu ayağa kalktığında "MyLocalAgent" adıyla Client (örneğin bir Claude veya Gemini istemcisi) yönünden ulaşılabilir olacaktır.
