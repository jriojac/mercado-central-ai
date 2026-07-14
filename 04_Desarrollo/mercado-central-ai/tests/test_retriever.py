from unittest.mock import Mock, patch

from langchain_core.documents import Document

from src.knowledge.vector_store import VectorStore
from src.retriever.chroma_retriever import ChromaRetriever


def test_retrieve_calls_vector_store_similarity_search() -> None:
    """
    Verify that ChromaRetriever delegates the similarity search
    to the VectorStore.
    """

    # -----------------------------------------------------------------
    # Arrange
    # -----------------------------------------------------------------

    mock_vector_store = Mock(spec=VectorStore)

    fake_documents = [
        Document(page_content="Documento de prueba")
    ]

    mock_vector_store.similarity_search.return_value = fake_documents

    fake_embedding = [0.1, 0.2, 0.3]

    with patch(
        "src.retriever.chroma_retriever.Embeddings.generate_query_embedding",
        return_value=fake_embedding,
    ):

        retriever = ChromaRetriever(mock_vector_store)

        # -----------------------------------------------------------------
        # Act
        # -----------------------------------------------------------------

        result = retriever.retrieve("consulta")

    # -----------------------------------------------------------------
    # Assert
    # -----------------------------------------------------------------

    mock_vector_store.similarity_search.assert_called_once_with(
        embedding=fake_embedding,
        k=4,
    )

    assert result == fake_documents