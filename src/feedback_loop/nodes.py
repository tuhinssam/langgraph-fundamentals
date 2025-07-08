import random

from src.feedback_loop.schemas import AgentState


def greeting_node(state: AgentState) -> AgentState:
    """
    greeting node to say hi to person
    """
    state['name'] = f"Hi there, {state['name']}"
    state['counter'] = 0
    return state

def random_node(state: AgentState) -> AgentState:
    """
    generates random number from 0 to 10
    """
    state['numbers'].append(random.randint(0, 10))
    state['counter'] = state['counter'] + 1
    return state

def should_continue(state: AgentState) -> str:
    """
    decides what to do next
    """
    if state['counter'] < 5:
        print(f"entering loop: {state['counter']}")
        return "loop"
    else:
        return "exit"