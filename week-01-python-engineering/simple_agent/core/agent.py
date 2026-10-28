from tools.base_tool import BaseTool, AddTool, SubtractTool,  MultiplyTool, DivideTool, PowerTool


class SimpleAgent:
    def __init__(self, tools):
        self.tools = {}

        for tool in tools:
            self.tools[tool.name] = tool

        self.history = []

    def get_tool_descriptions(self, action=None):
        if action is not None:
            tool = self.tools.get(action)

        if tool is None:
            return "No description available."

        result = "Available tools and their descriptions:\n"
        for tool in self.tools.values():
            result += f"- {tool.name}: {tool.description}\n"

        return result

    def run(self, action, a, b):
        if action not in self.tools:
            raise ValueError(
                f"Invalid action: {action}."
                f"Available actions: {list(self.tools.keys())}")

        tool = self.tools[action]
        result = tool.execute(a, b)

        record = {
            "action": action,
            "a": a,
            "b": b,
            "result": result
        }
        if result != "Error: Division by zero is not allowed.":
            self.history.append(record)
        return result
