from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1. Model ve Prompt Yapılandırması
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Sen uzman bir seyahat rehberisin. Kullanıcının belirttiği şehir için 1 günlük kısa bir plan ve mutlaka tadılması gereken bir yemek öner."),
    ("user", "{sehir} şehri için bana öneride bulun.")
])

# 2. Zinciri (Chain) Oluşturma
# LangChain Expression Language (LCEL) kullanarak adımları birleştiriyoruz
chain = prompt | model | StrOutputParser()

# 3. Uygulamayı Çalıştırma
if __name__ == "__main__":
    sehir_input = "Floransa"
    print(f"--- {sehir_input} için plan hazırlanıyor... ---")
    
    # Bu invoke işlemi gerçekleştiği anda veriler otomatik olarak LangSmith'e akar
    response = chain.invoke({"sehir": sehir_input})
    
    print("\nAI Rehberin Önerisi:")
    print(response)