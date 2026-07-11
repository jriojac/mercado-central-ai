"""
Pruebas unitarias para ToolFactory.
"""

from src.tools.interfaces import ToolManagerInterface
from src.tools.tool_factory import ToolFactory


def test_create_returns_tool_manager_interface() -> None:
    """
    Debe crear un ToolManager listo para utilizar.
    """

    manager = ToolFactory.create()

    assert isinstance(
        manager,
        ToolManagerInterface,
    )