from core.agent import SimpleAgent
from tools.base_tool import AddTool, SubtractTool, MultiplyTool, DivideTool, PowerTool
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s"
)


def main():
    tools = [AddTool(), SubtractTool(), MultiplyTool(),
             DivideTool(), PowerTool()]
    agent = SimpleAgent(tools)

    print("Simple Agent Started")
    print("Type 'help' to see available tools.")
    print("Type 'exit' to stop the program.")
    print("Type 'history' to see the action history.")

    available_tools = ", ".join(agent.tools.keys())

    while True:
        action = input(
            f"\nEnter action {available_tools}, help, exit, history: "
        ).strip().lower()

        if action == "exit":
            print("Agent stopped.")
            break
        if action == "help":
            print(agent.get_tool_descriptions())
            continue
        if action == "history":
            if not agent.history:
                print("No history available.")
            else:
                for record in agent.history:
                    print(
                        f"- {record.action}({record.a}, {record.b}) = {record.result}"
                    )
            continue

        if action not in agent.tools:
            print(f"Error: Unknown tool '{action}'")
            continue
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        try:
            result = agent.run(action, a, b)
            print(f"Result: {result}")

        except ZeroDivisionError as error:
            logging.error("Calculation failed: %s", error)

            print(f"Division Error: {error}")
        except ValueError as error:
            logging.error("Invalid input: %s", error)
            print(f"Invalid Input Error: {error}")


if __name__ == "__main__":
    main()
