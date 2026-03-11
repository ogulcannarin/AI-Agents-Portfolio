# 🤖 AI Agent — ReAct & Reflection Sistemi

> Yapay zeka ajanlarının **ReAct** (Reason + Act) ve **Reflection** mimarisini gösteren, dış bağımlılık gerektirmeyen saf Python simülasyonu.

<br>

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![No Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Educational-yellow?style=flat-square)]()

---

## 📖 İçindekiler

- [Kavramlar](#-kavramlar)
  - [ReAct Nedir?](#react-nedir)
  - [Reflection Nedir?](#reflection-nedir)
  - [Birlikte Nasıl Çalışırlar?](#birlikte-nasıl-çalışırlar)
- [Mimari](#-mimari)
- [Proje Yapısı](#-proje-yapısı)
- [Kurulum & Çalıştırma](#-kurulum--çalıştırma)
- [Örnek Çıktılar](#-örnek-çıktılar)
- [Senaryo Analizi](#-senaryo-analizi)
- [ReAct vs Reflection — Karşılaştırma](#-react-vs-reflection--karşılaştırma)
- [Gerçek Dünya Kullanımı](#-gerçek-dünya-kullanımı)
- [Akademik Kaynaklar](#-akademik-kaynaklar)
- [Sonraki Adımlar](#-sonraki-adımlar)

---

## 🧠 Kavramlar

### ReAct Nedir?

**ReAct**, _Reasoning + Acting_ kelimelerinin birleşimidir. 2023 yılında Yao ve arkadaşları tarafından önerilen bu mimari, bir dil modelinin sadece bilgi üretmek yerine **dış araçlarla etkileşime girerek** döngüsel bir şekilde çalışmasını sağlar.

Döngü üç adımdan oluşur:

```
┌──────────┐    ┌──────────┐    ┌─────────────┐
│  THOUGHT │ -> │  ACTION  │ -> │ OBSERVATION │ --┐
│ (Düşün)  │    │ (Harekete│    │  (Gözlemle) │   │
│          │    │  geç)    │    │             │   │
└──────────┘    └──────────┘    └─────────────┘   │
      ^                                            │
      └────────────────────────────────────────────┘
                   (yeterli cevap bulunana kadar)
```

| Adım | Açıklama | Örnek |
|------|----------|-------|
| **Thought** | Model hedef için plan yapar | _"Hava durumunu öğrenmek için API çağırmalıyım"_ |
| **Action** | İlgili araç veya API çağrılır | `weather_api.get(city="İstanbul")` |
| **Observation** | Gelen yanıt sisteme alınır | `{"temp": 18, "desc": "Bulutlu"}` |

<br>

### Reflection Nedir?

**Reflection**, ajanın elde ettiği gözlemi veya hazırladığı cevabı **kullanıcıya sunmadan önce** kendi iç kalite kontrolünden geçirme sürecidir.

```
OBSERVATION alındı
      │
      ▼
┌─────────────────────────────┐
│         REFLECTION          │
│                             │
│  ✓ Fiziksel mantık kontrolü │  ← 250°C hava sıcaklığı imkansız!
│  ✓ Bağlamsal uygunluk       │  ← Cevap soruyla örtüşüyor mu?
│  ✓ Bütünlük kontrolü        │  ← Eksik bilgi var mı?
│  ✓ Güvenilirlik değerlendirme│  ← Kaynak tutarlı mı?
└─────────────────────────────┘
      │                │
   GEÇERLİ          GEÇERSİZ
      │                │
   Yanıtla         Yeniden dene / Düzelt
```

<br>

### Birlikte Nasıl Çalışırlar?

ReAct, ajanın **dış dünyayla konuşmasını** sağlar. Reflection ise bu konuşmadan gelen **verinin kalitesini denetler**. İkisi birleşince:

- Hatalı API yanıtları otomatik olarak ayıklanır
- Ajan kendi kendini düzeltebilir
- Kullanıcıya sadece doğrulanmış bilgi ulaşır
- Halüsinasyon riski önemli ölçüde azalır

---

## 🏗 Mimari

```
 Kullanıcı
    │  "İstanbul hava durumu nedir?"
    ▼
┌───────────────────────────────────────────────┐
│              ReAct + Reflection Ajan          │
│                                               │
│  ┌─────────┐  ┌────────┐  ┌─────────────┐    │
│  │ THOUGHT │→ │ ACTION │→ │ OBSERVATION │    │
│  └─────────┘  └────────┘  └──────┬──────┘    │
│       ↑                          │            │
│       │                   ┌──────▼──────┐     │
│       └───── YENİDEN ─────│ REFLECTION  │     │
│             DENE           └──────┬──────┘     │
│                                   │            │
│                              GEÇERLİ?          │
└───────────────────────────────────────────────┘
    │  Evet
    ▼
 Doğrulanmış Yanıt
```

**Bileşenler:**

- **Araçlar / Tools** — Hava durumu API, hesap makinesi, web arama, veritabanı
- **Bellek / Memory** — Kısa süreli (mevcut konuşma) ve uzun süreli (vektör DB)
- **Ajan Durumu** — Döngü sayacı, hata logu, güven skoru

---

## 📁 Proje Yapısı

```
react-reflection-agent/
├── README.md                  # Bu dosya
├── Makale.md                  # Kavramları açıklayan blog yazısı
└── react_reflection_agent.py  # Python simülasyonu
```

---

## 🚀 Kurulum & Çalıştırma

### Gereksinimler

- **Python 3.x** (herhangi bir sürüm yeterlidir)
- Üçüncü parti kütüphane **gerektirmez** — yalnızca standart kütüphane kullanılır

### Çalıştırma

```bash
# Repoyu klonla
git clone https://github.com/kullanici-adi/react-reflection-agent.git
cd react-reflection-agent

# Simülasyonu çalıştır
python react_reflection_agent.py
```

---

## 📊 Örnek Çıktılar

Simülasyon her çalıştığında farklı API yanıtları üretir. İki olası senaryo:

**✅ Senaryo 1 — Başarılı (Geçerli Veri)**

```
[THOUGHT]  Hava durumu API'sini çağırıyorum: İstanbul
[ACTION]   fake_weather_api('İstanbul') → çağrılıyor...
[OBS]      Sıcaklık=18°C, Parçalı bulutlu
[REFLECT]  18°C makul aralıkta (-60 ile +60 arası). Veri geçerli ✓

[FINAL]    ✓ İstanbul: 18°C, Parçalı bulutlu
```

**⚠️ Senaryo 2 — Hata Tespiti + Otomatik Düzeltme**

```
[THOUGHT]  Hava durumu API'sini çağırıyorum: İstanbul
[ACTION]   fake_weather_api('İstanbul') → çağrılıyor...
[OBS]      Sıcaklık=250°C, Güneşli
[REFLECT]  Fiziksel olarak imkansız: 250°C ← HATA TESPİT EDİLDİ
[RETRY]    Deneme 1/3 — yeniden sorgulanıyor...
[ACTION]   fake_weather_api('İstanbul') → yeniden çağrılıyor...
[OBS]      Sıcaklık=22°C, Açık
[REFLECT]  22°C makul aralıkta. Veri geçerli ✓

[FINAL]    ✓ İstanbul: 22°C, Açık
```

---

## 🔬 Senaryo Analizi

| Senaryo | API Yanıtı | Reflection Kararı | Sonuç |
|---------|-----------|-------------------|-------|
| Normal | `temp=18°C` | Geçerli ✓ | İlk denemede yanıt |
| Hatalı veri | `temp=250°C` | Geçersiz ✗ | Yeniden deneme |
| Tekrar hata | `temp=250°C` → `temp=22°C` | Geçersiz → Geçerli | 2. denemede yanıt |
| Tüm denemeler hatalı | `temp=999°C` (3 kez) | Geçersiz ✗✗✗ | Hata mesajıyla sonlandı |

> 💡 **Not:** Maksimum yeniden deneme sayısı `max_retries = 3` ile sınırlandırılmıştır. Bu parametre artırılabilir veya azaltılabilir.

---

## ⚖️ ReAct vs Reflection — Karşılaştırma

| Özellik | ReAct | Reflection |
|---------|-------|-----------|
| **Temel amacı** | Dış dünyayla etkileşim döngüsü | İç kalite kontrolü |
| **Ne zaman çalışır** | Her araç/API çağrısında | Observation sonrası |
| **Dış kaynak kullanımı** | ✅ Evet (API, DB, arama) | ❌ Hayır (tamamen içsel) |
| **Hata durumunda** | Farklı araç dener | Adımı düzeltir/tekrarlar |
| **Analogisi** | Dedektifin ipucu araştırması | Editörün makaleyi incelemesi |
| **Framework karşılığı** | LangChain Agent / Tool Use | Reflexion (Shinn et al. 2023) |
| **Güçlü olduğu alan** | Gerçek zamanlı veri, çok adımlı görevler | Halüsinasyon azaltma |

---

## 🌍 Gerçek Dünya Kullanımı

Bu proje temel mantığı simüle eder. Üretim ortamında aynı mimarinin framework karşılıkları:

```python
# LangChain ile gerçek ReAct agent
from langchain.agents import create_react_agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")
agent = create_react_agent(llm, tools=[weather_tool, search_tool])
agent.invoke({"input": "İstanbul hava durumu nedir?"})
```

| İhtiyaç | Araç / Framework |
|---------|-----------------|
| Temel ReAct döngüsü | [LangChain Agents](https://python.langchain.com/docs/modules/agents/) |
| Stateful ajan + bellek | [LangGraph](https://langchain-ai.github.io/langgraph/) |
| Reflection / self-critique | [Reflexion](https://github.com/noahshinn/reflexion) |
| Çok ajanlı sistemler | [AutoGen](https://github.com/microsoft/autogen) / [CrewAI](https://github.com/joaomdmoura/crewAI) |
| RAG + bellek | [LlamaIndex](https://www.llamaindex.ai/) |

---

## 📚 Akademik Kaynaklar

- **ReAct (2023)** — Yao et al., Princeton & Google Brain  
  [_ReAct: Synergizing Reasoning and Acting in Language Models_](https://arxiv.org/abs/2210.03629)

- **Reflexion (2023)** — Shinn et al.  
  [_Reflexion: Language Agents with Verbal Reinforcement Learning_](https://arxiv.org/abs/2303.11366)

- **Chain-of-Thought (2022)** — Wei et al., Google  
  [_Chain-of-Thought Prompting Elicits Reasoning in Large Language Models_](https://arxiv.org/abs/2201.11903)

---

## 🔭 Sonraki Adımlar

Bu projeyi daha ileri taşımak için önerilen yol haritası:

- [ ] **OpenAI API entegrasyonu** — Gerçek LLM ile thought üretimi
- [ ] **Birden fazla araç** — Arama, hesaplama, hava durumu bir arada
- [ ] **Bellek (Memory) katmanı** — Geçmiş konuşmaları hatırlama
- [ ] **LangGraph ile stateful agent** — Döngü kontrolü ve paralel adımlar
- [ ] **Multi-agent sistem** — Birden fazla ajan, ortak görev yönetimi
- [ ] **Evaluation & benchmarking** — Reflection kalite ölçümü

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır. Eğitim amaçlı serbestçe kullanılabilir.

---

> _Not: Bu proje konsept anlatımı için tasarlanmıştır. Gerçek otonom ajanlara dönüştürmek için OpenAI, LangChain veya LlamaIndex gibi framework'ler entegre edilebilir._
