from dataclasses import dataclass


@dataclass
class AgentRecord:
    action: str
    a: float
    b: float
    result: float
