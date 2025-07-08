from typing import TypedDict, List


class AgentState(TypedDict):
    name: str
    numbers: List[int]
    counter: int