# 👁️ Observer: Durum ve Log Yönetimi (ProjectObserver)

Bu modül, uygulamalardaki "Gözlemci" (Observer) tasarım deseninden ilham alarak geliştirilmiş, durum yönetimi (State Management) ve loglama odaklı bir **FastMCP** sunucusudur.

## 📖 Projenin Amacı
Yapay zeka modellerinin yalnızca statik birer cevaplayıcı olmaktan çıkıp, o anki proje ortamının **sağlığını**, **yaşam döngüsünü (lifecycle)** ve **aktif çalışma süresini** gözlemleyen "Akademik/Analitik" ajanlara dönüşmesini sağlamaktır.

## ✨ Öne Çıkan Özellikler

### 1. Yaşam Döngüsü ve Durum Yönetimi (State Management)
Sunucu başlatıldığı andaki zamanı (`start_time`) belleğe alır ve bu değişkeni aktif olduğu sürece korur.
- **Kaynak (Resource) `observer://uptime`**: Sunucunun ne kadar süredir ayakta olduğunu bir `TimeDelta` objesi aracılığıyla anlık olarak hesaplar ve modele bu süreyi bildirir.

### 2. Akademik Loglama Mekanizması
Terminal üzerinden süreçleri kolayca izleyebilmek için standart `print` yerine Python'ın yerleşik `logging` modülü kullanılmıştır. 
- *INFO, WARNING, ERROR* bazlı sistem çıktıları terminalde süreçlerin çok daha elit ve kurumsal bir biçimde takip edilmesini sağlar.

### 3. Proje Sağlık Denetimi (Health Check Tool)
- **Araç (Tool) `check_project_health(path=".")`**: Modelin proje içerisindeki analizlerini güçlendirir. Belirtilen klasördeki dosyaları sayarak, özellikle `.py` uzantılı Python dosyalarının sayısını hesaplar ve bu analizin sonucunu loglara yazarken modele detaylı bir sistem raporu döner.

## ⚙️ Nasıl Çalıştırılır?
Sunucuyu çalıştırıp izlemesini başlatmak için:
```bash
python observer_server.py
```
Çalıştığında *"Observer sunucusu el sıkışma (handshake) için hazır."* log mesajını alırsınız ve gözlemci devreye girer.
