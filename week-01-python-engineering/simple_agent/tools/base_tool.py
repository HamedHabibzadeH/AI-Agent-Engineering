class BaseTool:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def execute(self, *args: float, **kwargs) -> float:
        raise NotImplementedError(
            "Subclasses must implement execute()"
        )


class AddTool(BaseTool):
    def __init__(self):
        super().__init__("add", "A tool that adds two numbers")

    def execute(self, a, b):
        return a + b


class SubtractTool(BaseTool):
    def __init__(self):
        super().__init__("subtract", "A tool that subtracts two numbers")

    def execute(self, a, b):
        return a - b


class MultiplyTool(BaseTool):
    def __init__(self):
        super().__init__("multiply", "A tool that multiplies two numbers")

    def execute(self, a, b):
        return a * b


class DivideTool(BaseTool):
    def __init__(self):
        super().__init__("divide", "A tool that divides two numbers")

    def execute(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


class PowerTool(BaseTool):
    def __init__(self):
        super().__init__("power", "A tool that raises a number to a power")

    def execute(self, a, b):
        return a ** b
