from state import GraphState
from tools import web_search_tool
from langchain_core.messages import HumanMessage

def retrieve(state: GraphState):
    """
    Vektör veritabanından bilgi getirir (Şu anlık simülasyon/mock).
    """
    print("---RETRIEVE---")
    # Gerçek projede retriever çağırılır: docs = retriever.invoke(state["question"])
    return {"documents": ["LangGraph, döngüsel ve durum tabanlı Agent'lar oluşturmak için geliştirilen bir kütüphanedir."]}

def grade_documents(state: GraphState):
    """
    Gelen dokümanların alakalı olup olmadığını kontrol eder.
    """
    print("---CHECK RELEVANCE---")
    from chains import doc_grader_chain
    question = state["question"]
    documents = state["documents"]
    
    search_needed = "no"
    for doc in documents:
        # Puanlama Chain üzerinden yapılır
        grade = doc_grader_chain.invoke({"document": doc, "question": question})
        if grade.binary_score == "no":
            search_needed = "yes"
            break
            
    return {"search_needed": search_needed}

def web_search(state: GraphState):
    """
    Vektör DB'de bulunamayan bilgiyi internette arar.
    """
    print("---WEB SEARCHING---")
    question = state["question"]
    documents = state["documents"] # Mevcut (belki eksik) dokümanlar

    # Tavily araması yap
    docs = web_search_tool.invoke({"query": question})
    
    # Gelen sonuçları formatla ve mevcut dokümanlara ekle
    web_results = "\n".join([d["content"] for d in docs])
    documents.append(web_results)
    
    return {"documents": documents}

def generate(state: GraphState):
    """
    Tüm dokümanları kullanarak nihai cevabı üretir.
    """
    print("---GENERATING ANSWER---")
    question = state["question"]
    documents = state["documents"]
    
    # Basit bir RAG prompt'u ile LLM çağrısı
    from chains import rag_chain # (Aşağıda tanımlayacağız)
    
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {"generation": generation}