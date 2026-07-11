"""
=========================================================
Modelos utilizados por el módulo LLM.
=========================================================
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class LLMRequest:
    """
    Representa una solicitud preparada para un proveedor LLM.

    Attributes
    ----------
    query:
        Consulta original realizada por el usuario.

    context:
        Contexto generado por el Context Builder.

    system_prompt:
        Prompt del sistema que acompañará la consulta.

    metadata:
        Información adicional asociada a la solicitud.
    """

    query: str
    context: str
    system_prompt: str | None = None
    metadata: dict[str, Any] | None = None