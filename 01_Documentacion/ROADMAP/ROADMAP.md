# ROADMAP — Mercado Central AI

## Objetivo

Este documento presenta la planificación general del proyecto **Mercado Central AI**, mostrando la evolución del pipeline RAG mediante Sprint, Hitos y Releases, hasta alcanzar la versión estable **v1.0.0**.

---

# Estado actual

| Campo | Valor |
|-------|-------|
| Proyecto | Mercado Central AI |
| **Versión estable** | **v1.0.0** |
| **Sprint actual** | **Sprint 12** |
| **Hito actual** | **Hito 10 – LLM Provider** |
| **Estado** | ✅ Finalizado |
| **Próximo Sprint** | **Sprint 13 – Streamlit UI** |


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
| Sprint 13 | Hito 11 | Streamlit UI | v1.1.0 | ⏳ |

---

# Estado del Pipeline RAG

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
| Streamlit UI | ⏳ |

---

# Avance del proyecto

| Indicador | Valor |
|-----------|------:|
| Sprint completados | **10 / 11** |
| Releases publicadas | **10** |
| Avance estimado | **95 %** |
| Pruebas automatizadas | **43** |
| Versión estable | **v1.0.0** |
| Próxima Release | **v1.1.0** |

---

# Objetivos de las próximas Releases

| Release | Objetivo |
|----------|----------|
| **v1.1.0** | Desarrollar la **Interfaz Streamlit**, integrando el pipeline RAG completo y proporcionando una experiencia de usuario de extremo a extremo. |

---

# Release actual

## v1.0.0 — LLM Provider

La Release **v1.0.0** representa un hito importante en la evolución del proyecto, al completar la infraestructura principal del pipeline RAG.

### Componentes incorporados

- LLMProviderInterface.
- GoogleGeminiProvider.
- LLMProviderFactory.
- Integración con Google Gemini mediante LangChain.
- Configuración centralizada del proveedor.
- Validaciones manuales.
- Pruebas automatizadas.

### Resultados obtenidos

- Pipeline RAG completamente implementado.
- Arquitectura desacoplada mediante Interfaces.
- Factory Pattern consolidado.
- Comunicación con Google Gemini encapsulada.
- Decision Engine desacoplado mediante `LLMRequest`.
- 43 pruebas automatizadas exitosas.
- Documentación técnica sincronizada.

La siguiente etapa del proyecto estará orientada al desarrollo de la interfaz de usuario mediante **Streamlit**.

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
| **v1.0.0** | **12** | **LLM Provider** | **✅** |
| **v1.1.0** | **13** | **Streamlit UI** | **⏳** |

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

Cada Sprint incorpora un nuevo módulo funcional al pipeline RAG y genera una Release estable, documentada y validada mediante pruebas automatizadas.

Con la publicación de la **Release v1.0.0**, el proyecto completa la infraestructura principal del pipeline RAG, incorporando el módulo **LLM Provider** y la integración con **Google Gemini**, manteniendo la arquitectura desacoplada basada en Interfaces, Factory Pattern y configuración centralizada.

La siguiente fase del proyecto estará orientada al desarrollo de la **Interfaz Streamlit**, reutilizando todos los componentes implementados hasta la fecha para ofrecer una aplicación funcional de extremo a extremo.

El ROADMAP constituye la referencia oficial para el seguimiento del avance del proyecto y se actualiza al cierre de cada Sprint.