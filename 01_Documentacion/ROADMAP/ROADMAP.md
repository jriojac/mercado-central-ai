# ROADMAP — Mercado Central AI

## Objetivo

Este documento presenta la planificación general del proyecto **Mercado Central AI**, mostrando la evolución del pipeline RAG mediante Sprint, Hitos y Releases, hasta alcanzar la versión estable **v1.2.0**.

---

# Estado actual

| Campo               | Valor                                                           |
| ------------------- | --------------------------------------------------------------- |
| Proyecto            | Mercado Central AI                                              |
| **Versión estable** | **v1.2.0**                                                      |
| **Sprint actual**   | **Sprint 14**                                                   |
| **Hito actual**     | **Hito 12 – Inicialización Base Vectorial e Integración Final** |
| **Estado**          | ✅ Finalizado                                                    |

---

# Plan de desarrollo

| Sprint | Hito | Módulo | Release | Estado |
|:------:|:----:|----------------------|:-------:|:------:|
| Sprint 3 | Hito 1 | Document Loader | v0.1.1 | ✅ |
| Sprint 4 | Hito 2 | Text Splitter | v0.2.0 | ✅ |
| Sprint 5 | Hito 3 | Metadata Manager | v0.3.0 | ✅ |
| Sprint 6 | Hito 4 | Embeddings Engine | v0.4.0 | ✅ |
| Sprint 7 | Hito 5 | Vector Store | v0.5.0 | ✅ |
| Sprint 8 | Hito 6 | Retriever | v0.6.0 | ✅ |
| Sprint 9 | Hito 7 | Context Builder | v0.7.0 | ✅ |
| Sprint 10 | Hito 8 | Decision Engine | v0.8.0 | ✅ |
| Sprint 11 | Hito 9 | Tools | v0.9.0 | ✅ |
| Sprint 12 | Hito 10 | LLM Provider | v1.0.0 | ✅ |
| Sprint 13 | Hito 11 | Streamlit UI | v1.1.0 | ✅ |
| Sprint 13 | Hito 11 | Base Vectorial e Integración Final | v1.2.0 | ⏳ |


---

# Estado del Pipeline RAG

| Elemento | Estado |
|-----------|:------:|
| Knowledge Base | ✅ |
| Document Loader | ✅ |
| Text Splitter | ✅ |
| Metadata Manager | ✅ |
| Embeddings Engine | ✅ |
| Vector Store | ✅ |
| Retriever | ✅ |
| Context Builder | ✅ |
| Decision Engine | ✅ |
| Tools | ✅ |
| LLM Provider | ✅ |
| Google Gemini | ✅ |
| Streamlit UI | ✅ |

---

# Avance del proyecto

| Indicador             |                                       Valor |
| --------------------- | ------------------------------------------: |
| Sprint completados    |                                 **12 / 12** |
| Releases publicadas   |                                      **12** |
| Avance estimado       |                                   **100 %** |
| Pruebas automatizadas |                                      **43** |
| Versión estable       |                                  **v1.2.0** |
| Estado                |                     **Proyecto Finalizado** |


---
# Release actual

## v1.2.0 — Integración Final del Pipeline RAG

### Componentes incorporados

- Streamlit UI.
- Prompt Builder.
- RAG Pipeline.
- Inicialización de Base Vectorial.
- Integración completa con Gemini.
- Validación End-to-End.

### Resultados obtenidos

- Pipeline completamente funcional.
- Interfaz conversacional.
- Recuperación semántica.
- Base Vectorial inicializada.
- Arquitectura desacoplada.
- 43 pruebas exitosas.

---

# Historial de Releases

| Release | Sprint | Módulo | Estado |
|----------|:------:|----------------------|:------:|
| v0.1.1 | 3 | Document Loader | ✅ |
| v0.2.0 | 4 | Text Splitter | ✅ |
| v0.3.0 | 5 | Metadata Manager | ✅ |
| v0.4.0 | 6 | Embeddings Engine | ✅ |
| v0.5.0 | 7 | Vector Store | ✅ |
| v0.6.0 | 8 | Retriever | ✅ |
| v0.7.0 | 9 | Context Builder | ✅ |
| v0.8.0 | 10 | Decision Engine | ✅ |
| v0.9.0 | 11 | Tools | ✅ |
| v1.0.0 | 12 | LLM Provider | ✅ |
| v1.1.0 | 13 | Streamlit UI | ✅ |
| v1.2.0 | 14 | Base Vectorial e Integración Final | ✅ |


# Observaciones

El proyecto continúa siguiendo la metodología oficial basada en:

```text
Sprint
    │
    ▼
Hito
    │
    ▼
Release
```

Con la publicación de la Release v1.2.0 se completa el desarrollo del proyecto Mercado Central AI.

El sistema implementa un pipeline RAG completamente funcional, integrando recuperación semántica mediante ChromaDB, generación de respuestas con Google Gemini e interfaz gráfica desarrollada en Streamlit.

El ROADMAP refleja el cierre de los doce Sprint ejecutados durante el Challenge Alura + Oracle Next Education.