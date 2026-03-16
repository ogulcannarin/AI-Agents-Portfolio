# Sampling Logic: Data Analyst AI ile MCP Entegrasyonu

Bu proje, sunucuların LLM gücünü kullanarak kendi inisiyatifleriyle veri üretebilmesine veya analiz yapabilmesine olanak tanıyan **Model Sampling** özelliğini gösteren referans bir FastMCP uygulamasıdır.

## 🧠 Özellikler

- **LLM Sampling İsteği (`ctx.session.create_message`):** MCP Protokolü ile Host üzerinden bir metin üretim / analiz isteği yapılmasını sağlar.
- **Model Tercihleri (`ModelPreferences`):** Araca gelen istek üzerine ayağa kaldırılacak LLM'in performans dengesi sağlanır.
  - `speed_priority=True`: Hızlı yanıt üretebilme.
  - `intelligence_priority=True`: Gelişmiş nedensellik ve doğruluk payı.
- **Dinamik Rol Ataması:** FastMCP aracı olan `DataAnalyst`, gelen tanımlamalar üzerinden verinin çıkarım yapılmaya uygun "en önemli 3" analiz sonucunu anında özetler.

## 🚀 Teknik Yapı

- Uygulama, kullanıcının doğrudan veri analizi talep edebileceği `analyze_data_with_ai` adlı bir MCP Tool barındırmaktadır. 
- Bu araç tetiklendiğinde MCP Context (`ctx`) vasıtasıyla LLM Host'una mesaj geri fırlatılarak yeni bir LLM isteği (Sampling) yapılır. 

## 🛠️ Kurulum ve Kullanım

Test edebilmek için MCP protokolü bağımlılıklarının kurulu olduğundan emin olun:

```bash
pip install mcp
```

Uygulamayı çalıştırarak sunucuyu dinlemeye almak için:
```bash
python sampling_logic.py
```
*(Sunucu ile etkileşime girilebilmesi için Inspector veya herhangi bir MCP istemcisi kullanılmalıdır).*
