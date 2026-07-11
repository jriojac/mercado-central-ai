from src.llm.decision_engine import DecisionEngine
from src.llm.models import LLMRequest


def test_build_request_returns_llm_request() -> None:
    """
    Verifica que DecisionEngine construya un
    objeto LLMRequest correctamente.
    """

    engine = DecisionEngine()

    request = engine.build_request(
        query="¿Cuál es el horario?",
        context="El horario es de 24 horas.",
    )

    assert isinstance(request, LLMRequest)

    assert request.query == "¿Cuál es el horario?"
    assert request.context == "El horario es de 24 horas."

    assert request.system_prompt is None
    assert request.metadata is None