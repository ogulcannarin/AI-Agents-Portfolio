from typing import Annotated
from typing_extensions import TypedDict

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

# ✅ STATE
class State(TypedDict):
    messages: Annotated[list, add_messages]

# ✅ TOOL
@tool
def get_weather(city: str):
    """Belirtilen şehrin hava durumunu getirir."""
    if "istanbul" in city.lower():
        return "22 derece, güneşli."
    return "15 derece, bulutlu."

tools = [get_weather]

# ✅ LLM + TOOL BIND
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)

# ✅ TOOL NODE
tool_node = ToolNode(tools)

# ✅ MODEL NODE
def call_model(state: State):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

# ✅ ROUTER (karar fonksiyonu)
def should_continue(state: State):
    last_message = state["messages"][-1]

    # tool çağrısı varsa → tools node
    if last_message.tool_calls:
        return "tools"

    # yoksa → bitir
    return "end"

# ✅ GRAPH
workflow = StateGraph(State)

workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "agent")

# 🔥 DÜZELTİLDİ: conditional mapping EKLENDİ
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)

# 🔁 tool çalıştıktan sonra tekrar agent'a dön
workflow.add_edge("tools", "agent")

# ✅ COMPILE
app = workflow.compile()

# ✅ TEST
result = app.invoke({
    "messages": ["İstanbul'un hava durumu nasıl?"]
})

# çıktıyı yazdır
for msg in result["messages"]:
    print(msg)