from tools.base_tool import BaseTool, AddTool, SubtractTool,  MultiplyTool, DivideTool, PowerTool
from core.models import AgentRecord


class SimpleAgent:
    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}

        self.history = []

    def get_tool_descriptions(self, action=None):
        if action is not None:
            tool = self.tools.get(action)

            if tool is None:
                return "No description available."

            return tool.description

        result = "Available tools and their descriptions:\n"

        for tool in self.tools.values():
            result += f"- {tool.name}: {tool.description}\n"

        return result

    def run(self, action: str, a: float, b: float) -> float:
        if action not in self.tools:
            raise ValueError(
                f"Invalid action: {action}."
                f"Available actions: {list(self.tools.keys())}")

        tool = self.tools[action]
        result = tool.execute(a, b)

        record = AgentRecord(
            action=action,
            a=a,
            b=b,
            result=result)

        if result != "Error: Division by zero is not allowed.":
            self.history.append(record)
        return result
