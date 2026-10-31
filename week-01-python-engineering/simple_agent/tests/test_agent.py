from core.agent import SimpleAgent
from tools.base_tool import AddTool, DivideTool, MultiplyTool
import pytest


def test_add_tool():
    agent = SimpleAgent([AddTool()])

    result = agent.run("add", 4, 6)

    assert result == 10


def test_multiply_tool():
    agent = SimpleAgent([MultiplyTool()])

    result = agent.run("multiply", 4, 6)

    assert result == 24


def test_division_by_zero():
    agent = SimpleAgent([DivideTool()])

    with pytest.raises(ZeroDivisionError):
        agent.run("divide", 10, 0)

    assert agent.history == []
