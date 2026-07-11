"""
Pruebas para la interfaz ToolInterface.
"""

import pytest

from src.tools.interfaces import ToolInterface


class DummyTool(ToolInterface):
    """Implementación mínima para pruebas."""

    @property
    def name(self) -> str:
        return "dummy"

    @property
    def description(self) -> str:
        return "Dummy tool"

    def can_handle(self, query: str) -> bool:
        return query == "dummy"

    def execute(self, query: str) -> str:
        return f"Executed: {query}"


@pytest.fixture
def tool() -> DummyTool:
    """Fixture de DummyTool."""
    return DummyTool()


def test_tool_name(tool: DummyTool):
    assert tool.name == "dummy"


def test_tool_description(tool: DummyTool):
    assert tool.description == "Dummy tool"


def test_can_handle_true(tool: DummyTool):
    assert tool.can_handle("dummy") is True


def test_can_handle_false(tool: DummyTool):
    assert tool.can_handle("otro") is False


def test_execute(tool: DummyTool):
    assert tool.execute("dummy") == "Executed: dummy"