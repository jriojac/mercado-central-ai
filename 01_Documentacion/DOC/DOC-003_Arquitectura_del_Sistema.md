# DOC-003 -- Arquitectura del Sistema

## Objetivo

Definir la arquitectura lógica del agente.

## Componentes

Streamlit, LangChain, Prompt Manager, Memory Manager, Tool Manager, RAG,
ChromaDB y Gemini.

## Capas

Presentación → Aplicación → Agente → Herramientas → RAG → Base de
Conocimiento → LLM.

## Flujo

Usuario → Interfaz → Agente → Tool/RAG → LLM → Respuesta.
