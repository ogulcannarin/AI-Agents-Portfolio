# 🤖 Mini Otonom Yapay Zeka Ajanı (Mini AutoGPT)

Bu proje, kendi kendine kararlar alabilen, internette araştırma yapabilen ve hedefine ulaşmak için adım adım ilerleyen **basit bir otonom yapay zeka ajanı** (Autonomous AI Agent) prototipidir. 

Projenin temel mimarisi, günümüzün popüler yapay zeka konseptlerinden biri olan **AutoGPT**'nin çalışma mantığından (ReAct - Reasoning and Acting) ilham alınarak, en sade ve anlaşılır haliyle inşa edilmiştir.

---

## 🏗️ Projenin Amacı ve AutoGPT Mantığı

**AutoGPT nedir?** Geleneksel ChatGPT gibi sistemler kullanıcının her sorusuna bir cevap verir ve durur. Kullanıcıdan yeni bir komut bekler. **AutoGPT** tarzı otonom ajanlar ise kendilerine verilen ana bir **"Hedef" (Goal)** doğrultusunda kendi görev listelerini oluşturur, kendi kendilerine sorular sorar, araçlar (tools) kullanarak (internette arama, kod çalıştırma vb.) bilgi toplar ve görevi tamamlayana kadar insan müdahalesi olmadan çalışmaya devam ederler.

### Bu Projede AutoGPT Mantığı Nasıl Kullanıldı?

Bu proje, AutoGPT'nin temel yapı taşlarını 5 farklı dosya üzerinden uygulamaktadır:

1. **Otonom Döngü (Autonomous Loop - `agent.py`):** 
   Ajan, insan komutu beklemeden kendi kendine `range(5)` döngüsü içerisinde 5 adım boyunca düşünür ve eyleme geçer. Gerçek AutoGPT sistemleri hedefe ulaşana kadar (while True) döner.
   
2. **Düşünme ve Planlama (Reasoning & Planning - `planner.py`):** 
   Ajanın beyni olan LLM (GPT-4o-mini), her adımda mevcut durumu ve geçmiş hafızayı analiz eder. "Şimdi ne yapmalıyım? Bilgi eksikse SEARCH demeliyim" şeklinde mantıksal bir çıkarım (Reasoning) yapar.

3. **Hafıza (Memory - `memory.py`):** 
   Ajanın geçmiş adımlarda bulduğu verileri ve aldığı kararları belleğinde tutmasını sağlar. Ajan, ilerleyen adımlarda eski hatalarını veya bulgularını hatırlayarak yeni eylemlerini (Action) buna göre belirler.

4. **Araç Kullanımı (Tool Use - `tools.py`):** 
   Ajan, internete bağlı olmadığını ve bilgiye ihtiyacı olduğunu fark ettiğinde (örneğin güncel startup'ları ararken), DuckDuckGo arama motoru aracını tetikleyerek dış dünyadan veri çeker.

---

## 🔄 Tam Sürüm AutoGPT'den Farkları Nelerdir?

Bu proje, öğrenme ve konsepti anlama (Proof of Concept) amacıyla yazıldığından, devasa AutoGPT projelerinden şu konularda ayrılır:

- **Sınırlandırılmış Döngü:** Sonsuz döngü (infinite loop) tehlikesinden kaçınmak için döngü 5 adım ile sınırlandırılmıştır (`for step in range(5)`).
- **Zengin Araç Seti Eksikliği:** Bu projede sadece internet arama aracı (`search_tool`) mevcuttur. Gerçek AutoGPT'ler; dosya okuyup yazabilir, terminal komutları çalıştırabilir, kod yazabilir ve e-posta gönderebilir.
- **Kısa Süreli Hafıza:** Projedeki hafıza sadece basit bir liste (array) yapısında tutulur. Çok uzun görevlerde GPT modeli token limitini doldurabilir. Gelişmiş sistemler; ChromaDB, Pinecone gibi **Vektör Veritabanları (Vector DB)** kullanarak uzun süreli anılar (Long-Term Memory) oluşturur.
- **Özeleştiri (Self-Criticism):** Tam sürüm AutoGPT'ler, plan yaparken "Bu planın zayıf yönü ne?" diye kendine özeleştiri yapar. Bu prototip ise doğrudan aksiyona odaklanır.

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.8 veya üzeri
- OpenAI API Anahtarı
- Gerekli Python kütüphaneleri (Langchain, OpenAI, DuckDuckGo Search, Dotenv)

### 1. Kütüphaneleri Yükleyin
Proje dizininde terminali açarak aşağıdaki kütüphaneleri yükleyin:
```bash
pip install langchain-openai langchain-core python-dotenv duckduckgo-search
```

### 2. Çevre Değişkenlerini (Env) Ayarlayın
Proje ana dizininde `.env` adında bir dosya oluşturun ve içine OpenAI API anahtarınızı ekleyin:
```env
OPENAI_API_KEY=sk-sizin-api-anahtariniz-buraya
```

### 3. Ajanı Başlatın
Ajanın hedefini `main.py` dosyası içindeki `goal` değişkeninden değiştirebilirsiniz. Ardından ana dosyayı çalıştırın:
```bash
python main.py
```

---

## 📂 Proje Yapısı

- `main.py` : Uygulamayı ayağa kaldıran, hedefi belirleyen ve ajanı başlatan ana dosya.
- `agent.py` : AutoGPT otonom döngüsünü, düşünme ve aksiyon (ReAct) süreçlerini yöneten orkestratör dosya.
- `planner.py` : OpenAI Language Model'ini barındıran ve mantıksal çıkarım yapan (prompt engineering) zeka modülü.
- `tools.py` : Ajanın dış dünya ile etkileşime girmesini sağlayan (DuckDuckGo Internet araması) araçların bulunduğu dosya.
- `memory.py` : Ajanın geçmiş eylemlerini ve edindiği bilgileri saklayan temel hafıza modülü.

---

*Bu proje, yapay zeka ajanlarının (AI Agents) nasıl çalıştığını, Düşünce-Eylem (Reasoning-Acting) döngüsünün kod üzerinde nasıl kurulduğunu anlamak isteyenler için harika bir temeldir. İstenirse yeni araçlar eklenerek çok daha yetenekli bir AutoGPT varyasyonuna dönüştürülebilir.*
