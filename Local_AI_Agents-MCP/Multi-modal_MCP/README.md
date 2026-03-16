# Multi-modal MCP (Model Context Protocol)

Bu klasör, standart metin tabanlı Model Context Protocol (MCP) mimarisine ek olarak **Çoklu Modalite (Multi-modal)** konseptini simüle eder. Yani bir AI Ajanının yalnızca metin (skor, istatistik) değil, sistem dışından gelen farklı türdeki medyaları (Örneğin: Isı haritası, Görsel vb.) veri kaynaklarından nasıl talep edip işleyebileceğine dair harika bir referans kodudur.

## İçerik ve Dosyaların Görevi

- **`data_simulation.py`**: Sistemi test edebilmek için dış servis simülasyonu yapar. *Pillow (PIL)* kütüphanesini kullanarak sahada oynayan oyuncuların örnek bir **Isı Haritası (Heatmap)** görselini (kırmızı noktalar şeklinde) çizer ve bu görseli ajanların (LLM) doğrudan tüketebileceği formata, yani `Base64`'e çevirir.
- **`mcp_resource.py`**: "Resource (Kaynak)" şablonu katmanıdır. `football://match/{week}/{match_id}` üzerinden kendisine gelen talepler sonucunda içeriğe skor/metin bilgisine ek olarak **Base64 formatındaki görsel verisini de** dahil ederek yanıt döner.
- **`process_multimodal.py`**: Tıpkı bir "Multimodal Agent" gibi davranır. `mcp_resource` üzerinden aldığı metinsel verilere ek olarak, gelen payload içerisinde çok boyutlu verinin (görselin) de bulunduğunu başarılı bir şekilde tespit edip işler.
- **`main.py`**: Bu mikro sistemi uçtan uca çalıştıran ana entegrasyon dosyasıdır. Isı haritasını oluşturur, veriyi kaynağa (Resource) paslar ve Ajanı (Process) simüle ederek sonucu ekrana yansıtır.

## Gereksinimler

Proje görsel üretmek için `Pillow` paketi kullanmaktadır. Kurulu değilse indirmek için:

```bash
pip install Pillow
```

## Nasıl Çalıştırılır?

Aşağıdaki komutla sistemi ayağa kaldırıp, base64 verisinin (Heatmap) nasıl model bağlamına iletildiğini görebilirsiniz:

```bash
python main.py
```

## Örnek Çıktı

Sistem başarıyla çalıştığında konsolda şuna benzer bir çıktı ile karşılaşacaksınız:

```
Maç URI: football://match/3/105
Skor: 5-2
Heatmap görseli base64 formatında gönderildi (XXX karakter)
```
Tıpkı Anthropic'in Multi-modal yapısı veya GPT-4v gibi veri akışlarını yerel fonksiyonlarla simüle etmek için son derece modern ve modüler bir mimari altyapısı sunmaktadır.
