from core.agent import SimpleAgent
from tools.base_tool import DivideTool

agent = SimpleAgent([DivideTool()])

try:
    result = agent.run("divide", 10, 0)
    print(result)

except ZeroDivisionError as error:
    print(f"Caught error: {error}")

print("Agent is still running.")
print("History:", agent.history)
