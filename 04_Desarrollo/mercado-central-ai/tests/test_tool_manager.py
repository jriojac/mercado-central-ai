"""
Pruebas unitarias para ToolManager.
"""

import pytest

from src.core.exceptions import DuplicateToolError
from src.tools.interfaces import ToolInterface
from src.tools.tool_manager import ToolManager


class DummyTool(ToolInterface):
    """
    Implementación mínima de ToolInterface para pruebas.
    """

    @property
    def name(self) -> str:
        return "dummy"

    @property
    def description(self) -> str:
        return "Dummy Tool"

    def can_handle(self, query: str) -> bool:
        return query == "dummy"

    def execute(self, query: str) -> str:
        return f"Executed: {query}"


@pytest.fixture
def manager() -> ToolManager:
    """
    Crea una instancia de ToolManager.
    """
    return ToolManager()


@pytest.fixture
def tool() -> DummyTool:
    """
    Crea una herramienta Dummy.
    """
    return DummyTool()


def test_register_tool(
    manager: ToolManager,
    tool: DummyTool,
) -> None:
    """
    Debe registrar correctamente una herramienta.
    """

    manager.register(tool)

    assert manager.has_tool("dummy")

def test_register_invalid_type(
    manager: ToolManager,
) -> None:
    """
    Debe rechazar objetos que no implementen ToolInterface.
    """

    with pytest.raises(TypeError):
        manager.register("dummy")   # type: ignore[arg-type]


def test_register_duplicate_tool(
    manager: ToolManager,
    tool: DummyTool,
) -> None:
    """
    Debe impedir registrar dos herramientas
    con el mismo nombre.
    """

    manager.register(tool)

    with pytest.raises(DuplicateToolError):
        manager.register(tool)


def test_execute_matching_tool(
    manager: ToolManager,
    tool: DummyTool,
) -> None:
    """
    Debe ejecutar la herramienta correcta.
    """

    manager.register(tool)

    response = manager.execute("dummy")

    assert response == "Executed: dummy"


def test_execute_without_matching_tool(
    manager: ToolManager,
    tool: DummyTool,
) -> None:
    """
    Debe devolver None cuando ninguna herramienta
    pueda atender la consulta.
    """

    manager.register(tool)

    response = manager.execute("otra consulta")

    assert response is None