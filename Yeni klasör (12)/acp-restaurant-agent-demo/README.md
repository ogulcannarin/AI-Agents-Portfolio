# ACP Örneği: Restoran Analizi

Agentic AI ve ajanlar-arası mesajlaşma (ACP tarzı JSON-RPC protokolü) kavramlarını öğrenmek için yazılmış küçük bir örnek proje. Senaryo: "Ankara'daki en iyi kahveleri bul" görevini birden fazla ajanın iş birliğiyle çözmek.

## Mimari

```
orchestrator.py (planner + client)
   │  JSON-RPC 2.0 / TCP
   ├──▶ search_agent_server.py     (:8901)  Foursquare Places API'den gerçek kahveci verisi çeker
   ├──▶ evaluator_agent_server.py  (:8902)  OpenAI API ile sonuçları değerlendirip sıralar
   └──▶ final_agent_server.py      (:8903)  En iyi 3'ü seçip kullanıcıya sunar
```

Her ajan kendi process'inde çalışan bağımsız bir JSON-RPC sunucusudur (`transport.py` içindeki `serve()` fonksiyonu ile). `orchestrator.py` bu üç process'i başlatır, planner rolünü üstlenir ve ajanlara sırayla `{"jsonrpc": "2.0", "method": ..., "params": ..., "id": ...}` formatında istek gönderip cevaplarını bir sonraki ajana aktarır.

Bu yapı, Zed'in editör-ajan protokolü olan **Agent Client Protocol (ACP)**'nin temel prensibini gösterir: ayrı process'ler arasında standart bir mesaj formatı (JSON-RPC) ile haberleşme. Farkı: gerçek ACP stdio üzerinden çalışır, bu örnekte öğretim amaçlı TCP soket kullanıldı.

## Dosyalar

| Dosya | Görev |
|---|---|
| `transport.py` | JSON-RPC istemci (`send_request`) ve sunucu (`serve`) yardımcı fonksiyonları |
| `search_agent_server.py` | Foursquare Places API'den kahveci arar |
| `evaluator_agent_server.py` | OpenAI ile sonuçları değerlendirir, gerekçeli sıralama üretir |
| `final_agent_server.py` | Sıralanmış listeden ilk 3'ü seçer |
| `orchestrator.py` | Ajanları başlatır, planner olarak görevi tetikler, akışı yönetir |
| `restoran_acp.py` | Aynı senaryonun tek process'te, ağ katmanı olmadan çalışan basit/başlangıç versiyonu |

## Kurulum

```bash
pip install openai
```

Ortam değişkenleri gerekli:

```powershell
$env:OPENAI_API_KEY = "..."
$env:FOURSQUARE_API_KEY = "..."
```

## Çalıştırma

```bash
python orchestrator.py
```

Basit (tek process, ağ katmanı olmayan) versiyonu denemek için:

```bash
python restoran_acp.py
```

## Bilinen sınırlamalar

- Foursquare'in ücretsiz katmanı `rating` ve `review_count` alanlarını "Premium" kabul ediyor; kredi olmadan bu alanlar `null` döner. Bu durumda Evaluator ajanı mekanları elemeden listeler ama gerçek puanlara göre sıralama yapamaz.
- LLM tabanlı Evaluator ajanının çıktısı deterministik değildir; aynı girdiyle her çalıştırmada birebir aynı sıralama/gerekçe garanti edilmez.
- Her JSON-RPC bağlantısı tek istek/cevap için açılıp kapanır (kalıcı stream yoktur) — basitlik için tercih edilmiş bir tasarım kararıdır.
