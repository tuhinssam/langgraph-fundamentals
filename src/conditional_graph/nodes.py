from src.conditional_graph.schemas import AgentState


def adder(state: AgentState) -> AgentState:
    """
    node to add two numbers together
    """
    state["final_number"] = state["number1"] + state["number2"]
    return state

def subtractor(state: AgentState) -> AgentState:
    """
    node to subtracts two numbers
    """
    state["final_number"] = state["number1"] - state["number2"]
    return state

def multiplier(state: AgentState) -> AgentState:
    """
    node to subtracts two numbers
    """
    state["final_number"] = state["number1"] * state["number2"]
    return state

def decide_next_node(state: AgentState) -> str:
    """
    node to decide next node
    """
    if state['operation'] == '+':
        return "addition_operation"
    elif state['operation'] == '-':
        return "subtraction_operation"
    else:
        return "multiplication_operation"
