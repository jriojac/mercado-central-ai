from src.llm.models import LLMRequest


def test_llm_request_creation() -> None:
    """
    Verifica que LLMRequest almacene correctamente
    los datos recibidos.
    """

    request = LLMRequest(
        query="¿Cuál es el horario?",
        context="El horario es de 24 horas."
    )

    assert request.query == "¿Cuál es el horario?"
    assert request.context == "El horario es de 24 horas."



from src.llm.models import LLMRequest


def test_llm_request_default_values() -> None:
    """
    Verifica los valores opcionales por defecto.
    """

    request = LLMRequest(
        query="Consulta",
        context="Contexto"
    )

    assert request.system_prompt is None
    assert request.metadata is None