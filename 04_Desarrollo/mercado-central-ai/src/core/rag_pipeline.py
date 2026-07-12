"""
=========================================================
RAG Pipeline.

Responsable de orquestar el flujo completo del pipeline
RAG.

Sprint 13 - Hito 11
Release v1.1.0
=========================================================
"""

from src.context_builder.interfaces import (
    ContextBuilderInterface,
)

from src.llm.interfaces import (
    DecisionEngineInterface,
    LLMProviderInterface,
)

from src.prompts.prompt_builder import (
    PromptBuilder,
)

from src.retriever.interfaces import (
    IRetriever,
)


class RAGPipeline:
    """
    Orquestador principal del pipeline RAG.
    """

    def __init__(
        self,
        retriever: IRetriever,
        context_builder: ContextBuilderInterface,
        decision_engine: DecisionEngineInterface,
        prompt_builder: PromptBuilder,
        llm_provider: LLMProviderInterface,
    ) -> None:
        """
        Inicializa el pipeline.
        """

        self._retriever = retriever
        self._context_builder = context_builder
        self._decision_engine = decision_engine
        self._prompt_builder = prompt_builder
        self._llm_provider = llm_provider

    def answer(
        self,
        question: str,
    ) -> str:
        """
        Ejecuta el flujo completo del pipeline RAG.

        Parameters
        ----------
        question : str
            Consulta realizada por el usuario.

        Returns
        -------
        str
            Respuesta generada por el proveedor LLM.
        """

        question = question.strip()

        if not question:
            raise ValueError(
                "La consulta no puede estar vacía."
            )

        documents = self._retriever.retrieve(
            question
        )

        context = self._context_builder.build_context(
            documents
        )

        request = self._decision_engine.build_request(
            question,
            context,
        )

        prompt = self._prompt_builder.build(
            request
        )

        response = self._llm_provider.generate_response(
            prompt
        )

        return response