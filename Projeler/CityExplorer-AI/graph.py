from langgraph.graph import StateGraph, END
from state import ExplorerState
from nodes import museum_agent, food_agent, map_node

# 1. Grafı Başlat (State yapımızı veriyoruz)
workflow = StateGraph(ExplorerState)

# 2. Düğümleri (Nodes) Grafa Ekle
workflow.add_node("museum_research", museum_agent)
workflow.add_node("food_research", food_agent)
workflow.add_node("generate_results", map_node)

# 3. Akış Çizgisini (Edges) Belirle
# Giriş noktası: Önce müzeleri bulalım
workflow.set_entry_point("museum_research")

# Müzeler bitince yemek yerlerine geç
workflow.add_edge("museum_research", "food_research")

# Yemekler bitince haritayı ve JSON'u oluştur
workflow.add_edge("food_research", "generate_results")

# Bitiş
workflow.add_edge("generate_results", END)

# 4. Grafı Derle (Compile)
app = workflow.compile()