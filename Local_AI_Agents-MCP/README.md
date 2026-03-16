<div align="center">
  <h1>🤖 Local AI Agents & Model Context Protocol (MCP)</h1>
  <p><i>Building the Future of Autonomous AI with Standardized Context Protocols</i></p>
  
  [![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
  [![MCP](https://img.shields.io/badge/Architecture-MCP-purple?logo=anthropic&logoColor=white)](https://www.anthropic.com/news/model-context-protocol)
  [![AI Agents](https://img.shields.io/badge/AI-Agents-green?logo=openai&logoColor=white)]()
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

<hr/>

Bu proje, modern yapay zeka uygulamalarında devrim yaratan **Model Context Protocol (MCP)** standartlarını, **Ajan (Agent)** mimarilerini ve bu sistemlerin nasıl entegre edilebileceğini derinlemesine inceleyen kapsamlı bir referans deposudur.

İçerisindeki her bir klasör, hem teorik MCP prensiplerini pratik olarak simüle etmekte hem de gelişmiş yapay zeka ajanlarının (AI Agents) araç kullanımı (tool use), veri yönetimi ve otonom karar verme süreçlerine ışık tutmaktadır.

## 📑 İçindekiler
- [🌟 Model Context Protocol (MCP) Nedir?](#-model-context-protocol-mcp-nedir)
- [🏗️ Temel Yapıtaşları](#️-temel-yapıtaşları)
- [📂 Mimari Analiz ve Klasörler](#-mimari-analiz-ve-klasörler)
- [🚀 Kurulum ve Çalıştırma](#-kurulum-ve-çalıştırma)
- [🤝 Katkıda Bulunma (Contributing)](#-katkıda-bulunma-contributing)
- [📄 Lisans](#-lisans)

---

## 🌟 Model Context Protocol (MCP) Nedir?

**Model Context Protocol (MCP)**, [Anthropic](https://www.anthropic.com) tarafından öncülüğü yapılan ve yapay zeka modelleri (Büyük Dil Modelleri - LLM'ler) ile dış sistemler (veritabanları, harici API'ler, şirket içi yazılımlar, dosyalar vb.) arasında **standart, güvenli ve ortak bir iletişim köprüsü** kurmayı hedefleyen açık kaynaklı bir protokoldür.

Geçmişte her bir veri kaynağı veya dış servis için yapay zekaya özel bağlantılar (hard-coded API entegrasyonları) yazmak gerekirken; MCP tamamen modüler bir **İstemci-Sunucu (Client-Server)** mimarisi getirir. 

### 🏗️ Temel Yapıtaşları:
1. **Resources (Kaynaklar):** Modelin okuması gereken bağlamsal verilerdir (Loglar, veritabanı kayıtları, kod dökümleri, API yanıtları vs.). Protokol içerisinde URI (örn: `postgresql://db/users`) şablonları ile erişilirler.
2. **Prompts (İstemler):** Model için hazırlanmış standart ve dinamik görev şablonlarıdır. Her kullanım durumu için modelin nasıl davranmasını gerektiğini belirler.
3. **Tools (Araçlar):** Modelin sistemde **aktif eylem** (veri tabanına yazma, e-posta atma, bir script çalıştırma vs.) gerçekleştirmesini sağlayan fonksiyonlardır. Model bu araçların parametrelerini otonom olarak doldurur.

---

## 📂 Mimari Analiz ve Klasörler

Bu depo, MCP mantığını ve *Agentic Workflow* konseptlerini pratik örneklere dökmektedir:

| Modül | Açıklama |
| :--- | :--- |
| **`AdvancedToolPatterns`** | Ajanların dış dünya ile etkileşime girerken kullandıkları Araçlar (Tools) mimarisinin gelişmiş versiyonlarını ve mantık zincirlerini (Chain-of-Thought) içerir. |
| **`Multi-modal_MCP`** | Sadece metin bağlamı sunmakla kalmayıp, **Görsel (Heatmap vb.)** gibi çoklu modalitelere (Base64) sahip kaynakları Ajanlara nasıl aktarabileceğini gösterir. |
| **`MyServer`** | Ajanların dış dünyadaki verileri çekmek için iletişim kurduğu asıl veri servislerinin bağlandığı MCP "Server" simülasyonudur. |
| **`Observer`** | Ajanların kararlarını ve çalışmalarını dışarıdan izleyen (Monitoring) ve sonsuz döngüleri (hallucination loop) engelleyen denetleyici yapıdır. |
| **`PromptServer`** | Ajanların bağlama göre alması gereken "Kişiliği", "Görevi" veya "Talimat setini" yöneten İstem (Prompt) sunucusudur. |
| **`ResourceTemplates`** | Spesifik URI yapılarını (`football://match/{week}`) işleyerek, veritabanından dinamik ve noktasal veri çekimini ("Resources") sağlar. |
| **`RobustAuditor`** | Veri hatalarına veya Ajanın ürettiği yanlış JSON çıktılarına karşı sistemin güvenliğini sağlayan denetim (Audit) katmanıdır. |
| **`SamplingLogic`** | Ajanların veriler arasında kararsız kaldığı durumlarda istatistiksel ve mantıksal karar örneklemesi (Sampling) mekanizmasıdır. |

---

## 🚀 Kurulum ve Çalıştırma

Projenin her bir modülü kendi içerisinde bağımsız çalışabilen Python scriptleri barındırır. İhtiyacınız olan modüle girip ilgili simülasyonu test edebilirsiniz.

```bash
# Repoyu bilgisayarınıza klonlayın
git clone https://github.com/KULLANICI_ADINIZ/Local_AI_Agents-MCP.git
cd Local_AI_Agents-MCP

# 1. Metinsel kaynak kullanimi (ResourceTemplates)
cd ResourceTemplates
python main.py

# 2. Görsel ve Çoklu-modalite simülasyonu (Multi-modal_MCP)
cd ../Multi-modal_MCP
pip install Pillow
python main.py
```

> **Not:** İlgili klasörlerin içerisindeki alt `README.md` dosyalarını okuyarak o modül hakkında mimari detaylara ve özel komutlara erişebilirsiniz.

---

## 🎯 Neden MCP ve AI Agents?

Bu projenin sunduğu mimariler, geleceğin yazılım mühendisliğini temsil etmektedir. **Model Context Protocol**, mevcut şirket verileriniz (SQL, Slack, Dosyalar vs.) ile AI Ajanları arasındaki entegrasyon uçurumunu standartlaştırarak yok eder. 

Bu sayede, tek bir protokol aracılığıyla tüm yapay zeka modelleri, organizasyonunuzun tüm verilerini güvenle okuyabilir, analiz edebilir ve gerektiğinde inisiyatif alıp aksiyon gerçekleştirebilen dijital çalışma arkadaşlarına dönüşebilirler.

---

## 🤝 Katkıda Bulunma (Contributing)

Bu proje geliştirmeye açıktır. Repoyu `fork`'layıp yeni özellikler ekleyerek Pull Request (PR) gönderebilirsiniz:

1. Bu depoyu Fork'layın (`Fork`)
2. Yeni bir özellik dalı oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi kaydedin (`git commit -m 'Yeni bir araç simülasyonu eklendi'`)
4. Dalınızı gönderin (`git push origin feature/YeniOzellik`)
5. Bir Pull Request açın

##  📄 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. Herkesin kullanımına, dağıtımına ve geliştirmesine açıktır. İlgili dokümantasyon referans alınarak özgürce kopyalanabilir ve ticari projelerde entegre edilebilir.
