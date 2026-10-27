from tools.calculator import add, subtract, multiply, divide, power


class SimpleAgent:
    def __init__(self):
        self.tools = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
            "power": power,

        }

        self.descriptions = {
            "add": "Adds two numbers.",
            "subtract": "Subtracts the second number from the first.",
            "multiply": "Multiplies two numbers.",
            "divide": "Divides the first number by the second.",
            "power": "Raises the first number to the power of the second.",
        }

        self.history = []

    def run(self, action, a, b):
        if action not in self.tools:
            raise ValueError(
                f"Invalid action: {action}."
                f"Available actions: {list(self.tools.keys())}")

        tool = self.tools[action]
        result = tool(a, b)

        record = {
            "action": action,
            "a": a,
            "b": b,
            "result": result
        }

        if result != "Error: Division by zero is not allowed.":
            self.history.append(record)
        return tool(a, b)

    def get_tool_descriptions(self, action=None):
        if action is not None:
            return self.descriptions.get(action, "No description available.")

        result = "Available tools and their descriptions:\n"

        for tool_name in self.tools:
            description = self.descriptions.get(
                tool_name, "No description available.")
            print(f"{tool_name}: {self.descriptions[tool_name]}")
            result += f"- {tool_name}: {description}\n"
        return result
