# DOC-006 -- AI Knowledge Platform

## Objetivo

Definir cómo el agente obtiene, organiza, recupera y entrega
conocimiento utilizando únicamente fuentes oficiales.

## Explicación sencilla

Imagina una biblioteca. Los documentos son libros, ChromaDB es el
catálogo, el Retriever es el bibliotecario y Gemini es el profesor que
responde usando solo los libros autorizados.

## Arquitectura

PDF → Loader → Chunking → Embeddings → ChromaDB → Retriever → Context
Builder → Gemini → Respuesta.

## Componentes

Loader, Chunker, Metadata Manager, Embeddings, ChromaDB, Retriever,
Context Builder y Gemini Adapter.

## Seguridad

-   Solo documentos autorizados.
-   No exponer API Keys.
-   Validar entradas.
-   Citar la fuente documental.
-   Reducir alucinaciones mediante RAG.

## Archivos Python

src/rag/loader.py src/rag/chunker.py src/rag/retriever.py
src/rag/embeddings.py src/rag/vectordb.py src/core/knowledge_platform.py

## Checklist

□ Loader □ Chunking □ Metadata □ Embeddings □ ChromaDB □ Retriever □
Context Builder □ Pruebas
