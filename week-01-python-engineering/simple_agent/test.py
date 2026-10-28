from tools.base_tool import AddTool, MultiplyTool, SubtractTool, DivideTool, PowerTool
from core.agent import SimpleAgent

tools = [AddTool(), MultiplyTool(), SubtractTool(), DivideTool(), PowerTool()]

# for tool in tool:
#     print(tool.name, tool.execute(10, 5))


agent1 = SimpleAgent(tools)
agent2 = SimpleAgent(tools)

agent1.run("add", 2, 3)
agent2.run("multiply", 4, 5)

print("Agent 1:", agent1.history)
print("Agent 2:", agent2.history)
