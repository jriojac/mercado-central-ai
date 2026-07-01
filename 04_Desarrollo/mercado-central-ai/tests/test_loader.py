from src.knowledge.loader import DocumentLoader

print("=" * 50)
print("TEST - DOCUMENT LOADER")
print("=" * 50)

loader = DocumentLoader()

documents = loader.load_all()

print("\nResumen del Test")
print("-" * 50)
print(f"Total de documentos: {len(documents)}")

# Validaciones
assert len(documents) > 0, "No se cargó ningún documento."

assert len(documents) >= 124, (
    f"Se esperaban 124 documentos y se obtuvieron {len(documents)}."
)

if documents:
    print("\nPrimer documento:")
    print(documents[0].metadata)

print("\nTEST FINALIZADO")