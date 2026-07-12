"""
Interfaz Streamlit para Mercado Central AI.

Responsabilidad:
- Configurar la interfaz.
- Capturar la consulta del usuario.
- Mostrar resultados.

La integración con el pipeline RAG será incorporada
en la siguiente microentrega.
"""

from __future__ import annotations

import streamlit as st

from src.config.settings import (
    STREAMLIT_TITLE,
    STREAMLIT_DESCRIPTION,
    STREAMLIT_ICON,
    STREAMLIT_LAYOUT,
    STREAMLIT_PLACEHOLDER,
    STREAMLIT_BUTTON_LABEL,
)

from src.core.rag_pipeline import RAGPipeline

from src.core.rag_pipeline_factory import (
    RAGPipelineFactory,
)

class StreamlitApp:
    """
    Aplicación principal basada en Streamlit.
    """

    @staticmethod
    @st.cache_resource
    def _get_pipeline() -> RAGPipeline:
        """
        Obtiene una instancia reutilizable del pipeline RAG.

        Returns
        -------
        RAGPipeline
            Pipeline completamente configurado.
        """

        return RAGPipelineFactory.create()

    def run(self) -> None:
        """
        Ejecuta la interfaz principal.
        """

        self._configure_page()

        self._render_header()

        #question, submitted = self._render_input()
        question = self._render_input()

        self._render_output(question)

    def _configure_page(self) -> None:
        """
        Configura la página de Streamlit.
        """

        st.set_page_config(
            page_title=STREAMLIT_TITLE,
            page_icon=STREAMLIT_ICON,
            layout=STREAMLIT_LAYOUT,
        )

    def _render_header(self) -> None:
        """
        Renderiza el encabezado.
        """

        st.title(STREAMLIT_TITLE)

        st.write(STREAMLIT_DESCRIPTION)

        st.divider()

    def _render_input(self) -> str:
        """
        Renderiza el área de captura de preguntas.

        Returns
        -------
        str
            Consulta ingresada por el usuario.
        """

        st.subheader("Consulta")

        question = st.text_area(
            label="",
            placeholder=STREAMLIT_PLACEHOLDER,
            height=140,
        )

        submitted = st.button(
            STREAMLIT_BUTTON_LABEL,
            use_container_width=True,
        )

        if submitted:
            return question.strip()

        return ""

    def _render_output(self, question: str) -> None:
        """
        Renderiza el área de respuesta.

        Parameters
        ----------
        question : str
            Consulta ingresada por el usuario.
        """

        st.divider()

        st.subheader("Respuesta")

        response_placeholder = st.empty()

        if not question:
            response_placeholder.info(
                "Ingrese una consulta para comenzar."
            )
            return

        try:

            pipeline = self._get_pipeline()

            answer = pipeline.answer(question)

            response_placeholder.markdown(answer)

        except Exception as error:

            response_placeholder.error(str(error))