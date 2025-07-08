from langgraph.constants import END, START
from langgraph.graph import StateGraph

from src.feedback_loop.nodes import greeting_node, random_node, should_continue
from src.feedback_loop.schemas import AgentState

graph = StateGraph(AgentState)
graph.add_node("greeting", greeting_node)
graph.add_node("random", random_node)
graph.add_edge("greeting", "random")

graph.add_conditional_edges(
    "random",
    should_continue,
    {
        "loop": "random",
        "exit": END
    }
)

graph.set_entry_point("greeting")

app = graph.compile()