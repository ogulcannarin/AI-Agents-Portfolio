# ResourceTemplates

Bu klasör, MCP (Model Context Protocol) mantığına benzer bir **Kaynak Şablonu (Resource Template)** kurgusunu simüle eden bir futbol ligi projesi içermektedir. 

## Dosyalar ve Görevleri

- **`data_simulation.py`**: Projenin veri kaynağıdır. 38 haftalık (her haftada 10 maç olacak şekilde) sahte bir futbol ligi fikstürü ve rastgele atılmış gol sayılarını üretir.
- **`mcp_resource.py`**: Model Context Protocol'ün "Resource" (Kaynak) yapısını simüle eder. Bir URI şablonunu (`football://match/{week}/{match_id}`) ve parametreleri alarak `data_simulation` üzerinden ilgili maç verisini bulup döndürür. (Not: URI template mantığını tasvir etmek amacıyla parametrelerini almaktadır).
- **`process_match.py`**: `mcp_resource`'dan gelen veriyi alıp işleyerek ekrana okunabilir bir formatta (Hafta, Maç No, Ev Sahibi vs Deplasman skoru) yazdıran yardımcı bir fonksiyondur.
- **`weekly_top_scorer.py`**: Belirli bir haftadaki maçları tarayıp, takımların attığı golleri toplayarak o hafta en çok gol atan takımı hesaplar.
- **`main.py`**: Tüm sistemin entegre edilip çalıştırıldığı dosya. 1'den 38'e kadar tüm haftaları döner, `mcp_resource` üzerinden URI şablonu ile veriyi çeker (`football://match/{week}/{match_id}`), `process_match` ile yazdırır ve her haftanın sonunda `weekly_top_scorer` ile o haftanın en golcü takımını anons eder.

## Nasıl Çalıştırılır?

Projenin kök dizininde veya klasör içerisindeyken aşağıdaki komutla senaryoyu çalıştırıp çıktıyı inceleyebilirsiniz:

```bash
python main.py
```

## Mimari İnceleme ve Yorum

Kod yapısı "**Single Responsibility Principle (Tek Sorumluluk Prensibi)**" kavramına uygun bir şekilde parçalanmış:
1. Veri üretimi ayrı dosyada (Veri Tabanı similasyonu).
2. Veriye erişim / bağdaştırıcı yapı ayrı dosyada (MCP Resource similasyonu).
3. Veriyi işleme ve görselleştirme ayrı dosyalarda.
4. Karmaşık iş mantığı ayrı bir serviste (Haftanın golcüsü).

Bu mimari, Agent sistemlerinde (özellikle LangChain veya doğrudan MCP implementasyonlarında) kendi araçlarımızı (tools) ve kaynak şablonlarımızı modüler olarak nasıl projelendirebileceğimize harika bir örnek olmuş.
