
from src.llm.embedding_provider import EmbeddingProvider

provider = EmbeddingProvider()

embedding = provider.generate_document_embedding(
    "Hola mundo"
)

print(len(embedding))
print("OK")