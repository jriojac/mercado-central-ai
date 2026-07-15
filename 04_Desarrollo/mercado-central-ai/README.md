# Mercado Central AI

## Estado del proyecto

**Versión:** v1.2.0

### Componentes

-   ✅ Configuración del proyecto
-   ✅ Document Loader
-   ✅ Splitter
-   ✅ Embeddings
-   ✅ Vector Store
-   ✅ Retriever
-   ✅ Integración Gemini
-   ✅ Interfaz Streamlit

## Arquitectura

    PDF -> Loader -> Splitter -> Embeddings -> FAISS -> Retriever -> Gemini -> Chat

## Tecnologías

-   Python 3.14
-   LangChain
-   Google Gemini
-   FAISS
-   Streamlit

## Estructura

    01_Documentacion/
    03_Knowledge_Base/
    04_Desarrollo/mercado-central-ai/

## Ejecución

``` powershell
.\.venv\Scripts\Activate.ps1
python -m tests.test_loader
```

## Documentación

Ver carpeta `01_Documentacion`.

## Próximo Sprint

Implementación del módulo Splitter.
