"""
=========================================================
RAG Pipeline Factory.

Responsable de ensamblar el pipeline RAG utilizando
las factories de los módulos existentes.

Sprint 13 - Hito 11
Release v1.1.0
=========================================================
"""

from src.context_builder.context_builder_factory import (
    ContextBuilderFactory,
)

from src.llm.decision_engine_factory import (
    DecisionEngineFactory,
)

from src.llm.llm_factory import (
    LLMProviderFactory,
)

from src.prompts.prompt_builder import (
    PromptBuilder,
)

from src.retriever.retriever_factory import (
    RetrieverFactory,
)

from .rag_pipeline import RAGPipeline


class RAGPipelineFactory:
    """
    Factory responsable de crear instancias del
    pipeline RAG completamente configuradas.
    """

    @staticmethod
    def create() -> RAGPipeline:
        """
        Construye un pipeline RAG listo para utilizarse.

        Returns
        -------
        RAGPipeline
            Pipeline completamente configurado.
        """

        return RAGPipeline(
            retriever=RetrieverFactory.create(),
            context_builder=ContextBuilderFactory.create(),
            decision_engine=DecisionEngineFactory.create(),
            prompt_builder=PromptBuilder(),
            llm_provider=LLMProviderFactory.create(),
        )