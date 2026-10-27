from core.agent import SimpleAgent


def main():
    agent = SimpleAgent()

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
            for record in agent.history:
                print(
                    f"- {record['action']}({record['a']}, {record['b']}) = {record['result']}")
            continue
        if action not in agent.tools:
            print(f"Error: Unknown tool '{action}'")
            continue
        try:

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = agent.run(action, a, b)
            print(f"Result: {result}")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
