from typing import TypedDict


class AgentState(TypedDict):
    number1: int
    number2: int
    final_number: int
    operation: str