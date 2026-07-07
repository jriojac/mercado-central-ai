# ROADMAP — Mercado Central AI

## Objetivo

Este documento presenta la planificación general del proyecto **Mercado Central AI**, mostrando la evolución del pipeline RAG mediante Sprint, Hitos y Releases, hasta alcanzar la versión estable **v1.0.0**.

---

# Estado actual

| Proyecto | Mercado Central AI |
|-----------|--------------------|
| Versión estable | **v0.5.0** |
| Sprint actual | **Sprint 7** |
| Hito actual | **Hito 5 – Vector Store** |
| Estado | ✅ En desarrollo |
| Próximo Sprint | **Sprint 8 – Retriever** |

---

# Plan de desarrollo

| Sprint | Hito | Módulo | Release | Estado |
|:------:|:-----:|-------------------------|:-------:|:------:|
| Sprint 3 | Hito 1 | Document Loader | v0.1.1 | ✅ |
| Sprint 4 | Hito 2 | Text Splitter | v0.2.0 | ✅ |
| Sprint 5 | Hito 3 | Metadata Manager | v0.3.0 | ✅ |
| Sprint 6 | Hito 4 | Embeddings Engine | v0.4.0 | ✅ |
| Sprint 7 | Hito 5 | Vector Store | v0.5.0 | ✅ |
| Sprint 8 | Hito 6 | Retriever | v0.6.0 | ⏳ |
| Sprint 9 | Hito 7 | Context Builder | v0.7.0 | ⏳ |
| Sprint 10 | Hito 8 | Decision Engine | v0.8.0 | ⏳ |
| Sprint 11 | Hito 9 | Tools | v0.9.0 | ⏳ |
| Sprint 12 | Hito 10 | Interfaz Streamlit | v1.0.0 | ⏳ |

---

# Estado del Pipeline RAG

```text
Knowledge Base
        │
        ▼
Document Loader            ✅
        │
        ▼
Text Splitter              ✅
        │
        ▼
Metadata Manager           ✅
        │
        ▼
Embeddings Engine          ✅
        │
        ▼
Vector Store               ✅
        │
        ▼
Retriever                  ⏳
        │
        ▼
Context Builder            ⏳
        │
        ▼
Decision Engine            ⏳
        │
        ▼
Tools                      ⏳
        │
        ▼
Interfaz Streamlit         ⏳
```

---

# Avance del proyecto

| Indicador | Valor |
|-----------|-------:|
| Sprint completados | **5 / 10** |
| Releases publicadas | **5** |
| Avance estimado | **50 %** |
| Próxima Release | **v0.6.0** |

---

# Objetivos de las próximas Releases

| Release | Objetivo |
|----------|----------|
| **v0.6.0** | Implementar el módulo Retriever. |
| **v0.7.0** | Construir automáticamente el contexto para el LLM. |
| **v0.8.0** | Implementar el motor de decisión del Agente. |
| **v0.9.0** | Integrar herramientas (Tools) del Agente IA. |
| **v1.0.0** | Desarrollar la interfaz web mediante Streamlit e integrar el pipeline completo. |

---

# Release final

## v1.0.0 — Mercado Central AI

Objetivos de la versión estable:

- Pipeline RAG completamente funcional.
- Recuperación semántica mediante Retriever.
- Construcción automática de contexto.
- Integración con Google Gemini.
- Arquitectura modular basada en proveedores.
- Interfaz web desarrollada con Streamlit.
- Documentación técnica completa.
- Cobertura de pruebas automatizadas para todos los módulos.

---

# Observaciones

El desarrollo del proyecto sigue una metodología incremental basada en **Sprint → Hito → Release**, donde cada Sprint incorpora un nuevo módulo funcional al pipeline RAG.

Cada Release representa una versión estable del sistema y se publica únicamente después de completar:

- Implementación.
- Pruebas.
- Documentación técnica.
- Actualización de la trazabilidad.
- Cierre formal del Sprint.

El ROADMAP se actualiza al cierre de cada Sprint y constituye la referencia oficial para el seguimiento del avance del proyecto.