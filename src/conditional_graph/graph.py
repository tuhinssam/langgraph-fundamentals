from langgraph.constants import START, END
from langgraph.graph import StateGraph

from src.conditional_graph.nodes import adder, subtractor, decide_next_node, multiplier
from src.conditional_graph.schemas import AgentState

graph = StateGraph(AgentState)

graph.add_node("add_node", adder)
graph.add_node("subtract_node", subtractor)
graph.add_node("multiply_node", multiplier)
graph.add_node("router", lambda state:state)

graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router",
    decide_next_node,
    {
        #edge: node
        "addition_operation": "add_node",
        "subtraction_operation": "subtract_node",
        "multiplication_operation": "multiply_node"
    }
)

graph.add_edge("add_node", END)
graph.add_edge("subtract_node", END)
graph.add_edge("multiply_node", END)

app = graph.compile()

