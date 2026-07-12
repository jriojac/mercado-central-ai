"""
=========================================================
Prompt Builder.

Responsable de construir el prompt final que será enviado
al proveedor LLM.

Sprint 13 - Hito 11
Release v1.1.0
=========================================================
"""

from src.config.settings import PROMPT_SYSTEM_INSTRUCTIONS
from src.llm.models import LLMRequest


class PromptBuilder:
    """
    Construye el prompt final para el proveedor LLM.
    """

    def build(
        self,
        request: LLMRequest,
    ) -> str:
        """
        Construye el prompt final utilizando la configuración
        del sistema y la información contenida en un LLMRequest.

        Parameters
        ----------
        request : LLMRequest
            Solicitud preparada por el Decision Engine.

        Returns
        -------
        str
            Prompt listo para enviarse al proveedor LLM.
        """

        return (
            f"{PROMPT_SYSTEM_INSTRUCTIONS}\n\n"
            f"--------------------------------------------------\n"
            f"CONTEXTO\n\n"
            f"{request.context}\n\n"
            f"--------------------------------------------------\n"
            f"PREGUNTA\n\n"
            f"{request.query}\n\n"
            f"--------------------------------------------------\n\n"
            f"Respuesta:"
        )