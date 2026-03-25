from typing import Annotated
from typing_extensions import TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# STATE
class State(TypedDict):
    messages: Annotated[list, add_messages]

# LLM
llm = ChatOpenAI(model="gpt-4o")

# NODE
def call_model(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

# Graph
builder = StateGraph(State)

builder.add_node("assistant", call_model)
builder.add_edge(START, "assistant")

# Router
builder.add_conditional_edges(
    "assistant",
    lambda state: "END" if "tamam" in state["messages"][-1].content.lower() else "continue",
    {
        "continue": "assistant",
        "END": END
    }
)

# ✅ ÖNCE COMPILE
graph = builder.compile()

# ✅ SONRA ÇALIŞTIR
result = graph.invoke({
    "messages": ["Merhaba, kısa cevap ver ve sonunda tamam yaz"]
})

print(result["messages"][-1].content)