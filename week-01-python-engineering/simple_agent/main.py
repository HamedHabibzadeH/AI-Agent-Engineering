from core.agent import SimpleAgent


def main():
    agent = SimpleAgent()

    print("Simple Agent Started")

    while True:
        action = input(
            "\nEnter action (add, subtract, multiply, divide, exit): "
        ).strip().lower()

        if action == "exit":
            print("Agent stopped.")
            break

        try:
            if action not in agent.tools:
                raise ValueError("Unknown tool")

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = agent.run(action, a, b)
            print(f"Result: {result}")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
