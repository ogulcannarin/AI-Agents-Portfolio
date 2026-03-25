# Kod ve Mimari Detayları 🐍

Bu klasör, LangGraph kütüphanesinin üç temel felsefesinin öğrenilmesi adına yazılmış kaynak dosyalardan oluşur. Bütün dosyalar tamamen çalışan birer LangGraph grafiği (StateGraph) örneğidir. 

Aşağıda her bir dosyanın kod bazlı **adım adım (satır satır) açıklaması** yer almaktadır.

---

## 1. Hafıza ve Oturumlar: `memory.py`

**Ana Problem**: Doğal yapıdaki LLM modelleri "durumsuz"dur (stateless); yani her mesajı sanki ilk defa konuşuyormuş gibi ele alırlar.
**Çözüm**: `MemorySaver`, gönderilen her iş akışını hafızaya kaydederek aynı kişinin sohbetlerini birbiriyle ilişkilendirir.

### 🔍 Kod İncelemesi:
- **`MemorySaver()`**: Sistemin hafıza kontrol sistemidir; önceki mesaj kayıtlarını tutar.
- **`checkpointer=memory`**: `Graph` derlenirken (compile), sisteme state verilerinin bu memory değişkeni içerisinde yedekleneceği deklare edilir. Böylece sistem durduğundan veya kapandığından itibaren devam edebilir.
- **`config` (Configuración)**: Hafızanın kimi takip edeceğini belirtmek için zorunludur. `{"configurable": {"thread_id": "kullanici_123"}}` şeklinde verilir. Sisteme girdiğiniz an, *kullanici_123* numaralı id'deki eski mesajlar modelin `State`'ine eklenir.

**Deneme Senaryosu**: 
Sisteme ilk olarak *"Adım Ahmet"* bilgisini sunarsınız. İkinci komutta *"Adım ne?"* diye sorduğunuzda *thread_id* aynı olduğu (`kullanici_123`)  için model son mesajından önceki konuşma bloklarını hafızadan çeker ve cevabınızın `"Sizin adınız Ahmet"` olduğunu kolayca geri çağırır.

---

## 2. Temel Graf Akışı: `orn.py`

**Amaç**: Ajana LangChain zincirlerinden farklı olarak bir akış haritası ve **"karar verebilme"** mekanizması kazandırmak. LLM ile bir soru/cevap işlemi yaparken akışın nereye gideceğine dinamik olarak karar verilir.

### 🔍 Kod İncelemesi:
- **`State (TypedDict)`**: Bütün grafiğin kendi içindeki yegane paylaşımlı veri tabanıdır. Tüm düğümler bu `State` türünü teslim alır, içini günceller ve sonrakine devredir. İçerisindeki `add_messages` parametresi, yeni mesajlar geldiğinde eski listenin üstüne yazılmayıp otomatik olarak diziye eklenmesini (append) sağlar.
- **`StateGraph(State)`**: İş akışının kurulduğu ilk alandır. `builder.add_node("assistant", call_model)` gibi komutlarla LLM çağrımız bir düğüm olarak haritaya oturtulur.
- **`add_conditional_edges` (Koşullu Rota)**: LangGraph'ın en can alıcı noktalarından birisidir. LLM asistanından cevap çıktıktan sonra bir `lambda` fonksiyonuna (Router) girilir. Burada ajanımız "Eğer son gelen cevabın içeriğinde *'tamam'* geçiyorsa akışı `END` (Bitiş) düğümüne yolla, aksi takdirde akışa devam et" emriyle çalışır.

---

## 3. Akıllı Ajan ve Tool (Araç) Kullanımı: `tools.py`

**Amaç**: Yalnızca bilgi üreten bir chat bot yerine, dış dünyanın bilgilerini (örneğin hava durumu) veya veritabanı komutlarını çalıştırma yetkisi alan, kendisi için **harici tool (araç) tetikleme yeteneğine sahip Ajanlar** (AI Agents) geliştirmek.

### 🔍 Kod İncelemesi:
- **`@tool Dekoratörü`**: `get_weather` adındaki basit bir Python fonksiyonumuzun modelin anlayabileceği bir JSON şemasına sahip araca dönüşmesini sağlar. Belgelendirme/docstring yazısı (`"""Belirtilen şehrin hava durumunu getirir."""`) çok kritiktir; LLM sadece bu yazıyı okuyarak aracın ne işe yarayabileceğini, nezaman başvurulması gerektiğini tespit eder.
- **`llm.bind_tools(tools)`**: Seçtiğimiz GPT modeline "Senin elinde bu yetenekler/araçlar var, eğer kullanıcı hava durumunu sorarsa kendin sallama, parametreyi verip bu aracı kullanmaya çalış" mesajının iletildiği kısımdır.
- **`ToolNode`**: `@tool` ile üretilen fonksiyonların LangGraph içerisinde düğüm grafiği olarak (Node) barınmasını sağlar. Sorumluluğu sadece veriyi alıp gerçek Python fonksiyonunu çalıştırmak ve sonucunu State'in "messages" değişkenine eklemektir.
- **`should_continue` Fonksiyonu (Router)**: Modelin son ürettiği cevabı okur. Eğer mesajın içerisinde `tool_calls` özelliği doluysa (Yani AI "Ben Tool'u çağırmaya karar verdim" şeklinde parametre ürettiyse), durumu `tools` düğümüne kaydırır. Eğer call yoksa grafiği bitirir (`end`).
- **Akışın Döngüsü (Geri Çağırım)**: Projedeki en kritik satırdır: `workflow.add_edge("tools", "agent")`. Model tool'u istedikten sonra tool çalışır, ardından elde edilen hava durumu verisi TEKRAR model (ajan) düğümüne yollanır ki model gelen 22 derece bilgisini birleştirip "Hava şu anda güneşli ve 22 derece" şeklinde insancıl ve düzgün bir cevap üretebilsin.

---

## 💡 Nasıl Test Edilir?
Dosyaları aşağıda gösterildiği gibi ayrı ayrı komut istemcisinden çalıştırarak fonksiyonların terminal pencerelerinde nasıl sonuç ürettiğini gözlemleyebilirsiniz:

```bash
# Sadece hafıza mekanizmasını test etmek için
python memory.py

# Router ve koşullu yapı testini görmek için
python orn.py

# Ajanın aracı kullanarak ürettiği cevabı doğrulamak için
python tools.py
```
