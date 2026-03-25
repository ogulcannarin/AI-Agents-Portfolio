from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import Graph  # Graph sınıfı genellikle burada olur

# Hafıza ünitesini oluştur
memory = MemorySaver()

# Graph nesnesini oluştur
graph = Graph()  # Buraya kendi düğüm ve logic yapılandırmanızı eklemeniz gerekebilir

# Graph'ı derle
app = graph.compile(checkpointer=memory, interrupt_before=["tools"])

config = {"configurable": {"thread_id": "kullanici_123"}}

# İlk mesaj
input_1 = {"messages": [("user", "Adım Ahmet, İstanbul'da yaşıyorum.")]}
app.invoke(input_1, config)

# İkinci mesaj: hafızadan bilgiyi hatırlayacak mı?
input_2 = {"messages": [("user", "Benim adım ne ve nerede yaşıyorum?")]}
response = app.invoke(input_2, config)

print(response["messages"][-1].content)