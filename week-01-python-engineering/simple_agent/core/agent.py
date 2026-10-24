from tools.calculator import add, subtract, multiply, divide


class SimpleAgent:
    def __init__(self):
        self.tools = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide

        }

    def run(self, action, a, b):
        if action not in self.tools:
            raise ValueError(
                f"Invalid action: {action}. Available actions: {list(self.tools.keys())}")

        tool = self.tools[action]
        return tool(a, b)
