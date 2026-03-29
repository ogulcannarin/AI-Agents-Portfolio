# Self-Corrective RAG Agent 🤖🔍

Bu proje, **LangGraph** ve **LangChain** kullanılarak oluşturulmuş, kendi kendine hatalarını düzeltebilen (Self-Corrective) bir RAG (Retrieval-Augmented Generation) temsilcisidir (Agent). 

Ajanın temel çalışma prensibi, bir veritabanından doküman getirdikten sonra bir LLM ("kalite kontrol" aşaması) vasıtasıyla dokümanın soruyla alakasını kontrol etmesidir. Bilgiler yetersizse doğrudan halüsinasyon (uydurma) üretmek yerine devreye bir "Web Arama" aracı (Tavily) girer ve güncel bilgileri internetten çekerek mükemmel cevaba ulaşır.

## 🌟 Özellikler
- **Durum (State) Yönetimi:** LangGraph TypedDict üzerinden (question, documents, search_needed vb.) tüm bilgi akışı yönetimi.
- **Dış Araç Kullanımı:** Tavily API'si ile vektör veritabanından bulunamayan bilgiler için yedek arama akışı.
- **Koşullu Akışlar (Graph Edges):** LangGraph'in yönlendirme (routing) yeteneği sayesinde dokümanların kalitesine göre dinamik olarak üretici (generate) veya arayıcı (search) düğüme geçiş.
- **Özel Yönlendirmeli Promptlar:** Zincirleme (Chains) ile kalite değerlendiriciler ve LLM destekli yapısal çıktılar (`pydantic` destekli GradeDocuments vb.).

## 📂 Proje Yapısı

- `main.py` : Uygulamayı ayağa kaldıran ana dosya ve test senaryoları.
- `graph.py` : LangGraph ağının (StateGraph) kurulup düğümlerle birbirine bağlandığı dosya.
- `state.py` : Sistemin hafızasını temsil eden `GraphState` yapısının tanımı.
- `nodes.py` : LangGraph üzerindeki tüm aşamaların (retrieve, grade_documents, web_search, generate) yürütüldüğü düğümler (fonksiyonlar).
- `chains.py` : OpenAI Chat modeli vasıtasıyla belgeleri sınıflandıran/puanlayan (GradeDocuments) propmtlar ve LLM zincirleri.
- `tools.py` : İnternet araması için kullanılan Tavily entegrasyon ayarları.

## 🚀 Kurulum

### 1- Repoyu İndirin
```bash
git clone <repo-url>
cd self-corrective-rag-agent
```

### 2- Gerekli Kütüphaneleri Yükleyin
Bir sanal ortam (virtual environment) oluşturmanız önerilir. Daha sonra gerekli kütüphaneleri yükleyin:
```bash
pip install langchain langchain-openai langgraph langchain-community tavily-python python-dotenv pydantic
```

### 3- Çevre Değişkenlerini (API Keys) Ekleyin
Ana dizinde gizli bir `.env` dosyası oluşturun ve içerisine aşağıdaki API anahtarlarınızı ekleyin (Bu dosya `.gitignore` vasıtasıyla GitHub'a gönderilmeyecektir):

```env
OPENAI_API_KEY="sk-proj-...."
TAVILY_API_KEY="tvly-...."
LANGSMITH_API_KEY="lsv2-..." # Opsiyonel
LANGSMITH_TRACING="true"     # Opsiyonel
```

## 🎯 Kullanım

Uygulamayı çalıştırmak için sadece `main.py` dosyasını çalıştırın:
```bash
python main.py
```
Terminal üzerinden RAG temsilcisinin her adımını (Örn: retrieve > grade_docs > web_search > generate) günlüğünü görüntüleyebilir ve final cevabını kontrol edebilirsiniz.
