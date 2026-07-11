from src.llm.decision_engine_factory import DecisionEngineFactory
from src.llm.interfaces import DecisionEngineInterface

def test_create_returns_interface() -> None:
    """
    Verifica que el objeto retornado implemente
    la interfaz pública.
    """

    engine = DecisionEngineFactory.create()

    assert isinstance(
        engine,
        DecisionEngineInterface,
    )