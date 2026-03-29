from langgraph.graph import END, StateGraph
from state import GraphState
from nodes import retrieve, grade_documents, generate, web_search

# 1. Grafı Başlat
workflow = StateGraph(GraphState)

# 2. Düğümleri (Nodes) Tanımla
workflow.add_node("retrieve", retrieve)        # Bilgi getir
workflow.add_node("grade_docs", grade_documents) # Bilgiyi puanla
workflow.add_node("generate", generate)        # Cevap üret
workflow.add_node("web_search", web_search)    # İnternette ara

# 3. Akışı Bağla (Edges)
workflow.set_entry_point("retrieve")

workflow.add_edge("retrieve", "grade_docs")

# 4. Koşullu Geçiş (Conditional Edge)
# Eğer dokümanlar kötüyse 'web_search'e, iyiyse 'generate'e git.
workflow.add_conditional_edges(
    "grade_docs",
    lambda state: "web_search" if state["search_needed"] == "yes" else "generate",
    {
        "web_search": "web_search",
        "generate": "generate"
    }
)

# 5. Döngüyü Tamamla
workflow.add_edge("web_search", "generate")
workflow.add_edge("generate", END)

# 6. Grafı Derle
app = workflow.compile()