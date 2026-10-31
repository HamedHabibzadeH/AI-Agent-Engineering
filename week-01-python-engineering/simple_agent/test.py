from core.agent import SimpleAgent
from tools.base_tool import AddTool, MultiplyTool

agent = SimpleAgent([AddTool(), MultiplyTool()])

print(agent.get_tool_descriptions("add"))
print(agent.get_tool_descriptions("unknown"))
print(agent.get_tool_descriptions())
