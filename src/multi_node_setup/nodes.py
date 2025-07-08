from src.multi_node_setup.schemas import AgentState


def first_node(state: AgentState) -> AgentState:
    """
    first node for processing name
    """
    state['final'] = f"Hello {state['name']}!"
    return state

def second_node(state: AgentState) -> AgentState:
    """
    first node for processing age
    """
    state['final'] = state['final'] + f" Your age is {state['name']}. "
    return state

def third_node(state: AgentState) -> AgentState:
    """
    first node for processing skills
    """
    state['final'] = state['final'] + f"Your skills are {", ".join(state['skills'])}"
    return state