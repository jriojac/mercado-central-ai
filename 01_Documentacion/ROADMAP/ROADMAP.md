# ROADMAP — Mercado Central AI

## Objetivo

Este documento presenta la planificación general del proyecto **Mercado Central AI**, mostrando la evolución del pipeline RAG mediante Sprint, Hitos y Releases, hasta alcanzar la versión estable **v1.0.0**.

---

# Estado actual

| Campo               | Valor                        |
| ------------------- | ---------------------------- |
| Proyecto            | Mercado Central AI           |
| **Versión estable** | **v0.9.0**                   |
| **Sprint actual**   | **Sprint 11**                |
| **Hito actual**     | **Hito 9 – Tools**           |
| **Estado**          | ✅ Finalizado                 |
| **Próximo Sprint**  | **Sprint 12 – LLM Provider** |


---

# Plan de desarrollo

| Sprint | Hito | Módulo | Release | Estado |
|:------:|:-----:|-------------------------|:-------:|:------:|
| Sprint 3 | Hito 1 | Document Loader | v0.1.1 | ✅ |
| Sprint 4 | Hito 2 | Text Splitter | v0.2.0 | ✅ |
| Sprint 5 | Hito 3 | Metadata Manager | v0.3.0 | ✅ |
| Sprint 6 | Hito 4 | Embeddings Engine | v0.4.0 | ✅ |
| Sprint 7 | Hito 5 | Vector Store | v0.5.0 | ✅ |
| Sprint 8 | Hito 6 | Retriever | v0.6.0 | ✅ |
| Sprint 9 | Hito 7 | Context Builder | v0.7.0 | ✅ |
| Sprint 10 | Hito 8 | Decision Engine | v0.8.0 | ✅ |
| Sprint 11 | Hito 9  | Tools           | **v0.9.0** |    ✅   |
| Sprint 12 | Hito 10 | LLM Provider    | **v1.0.0** |    ⏳   |


---

# Estado del Pipeline RAG

| Elemento          | Estado |
| ----------------- | :----: |
| Document Loader   |    ✅   |
| Text Splitter     |    ✅   |
| Metadata Manager  |    ✅   |
| Embeddings Engine |    ✅   |
| Vector Store      |    ✅   |
| Retriever         |    ✅   |
| Context Builder   |    ✅   |
| Decision Engine   |    ✅   |
| **Tools**         |    ✅   |
| **LLM Provider**  |    ⏳   |
| **Gemini**        |    ⏳   |
| **Respuesta**     |    ⏳   |

---

# Avance del proyecto

| Indicador             |      Valor |
| --------------------- | ---------: |
| Sprint completados    | **9 / 10** |
| Releases publicadas   |      **9** |
| Avance estimado       |   **90 %** |
| Pruebas automatizadas |     **40** |
| Versión estable       | **v0.9.0** |
| Próxima Release       | **v1.0.0** |

---

# Objetivos de las próximas Releases

| Release    | Objetivo                                                                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **v1.0.0** | Implementar el **LLM Provider**, integrar Google Gemini y completar el pipeline RAG manteniendo la arquitectura basada en interfaces y Factory Pattern. |

---

# Release final

## v1.0.0 — Mercado Central AI

Objetivos de la versión estable:

- Pipeline RAG completamente funcional.
- Recuperación semántica mediante Retriever.
- Construcción automática de contexto.
- Administración de herramientas mediante ToolManager.
- Integración con Google Gemini.
- Arquitectura modular basada en proveedores.
- Interfaz web desarrollada con Streamlit.
- Documentación técnica completa.
- Cobertura de pruebas automatizadas para todos los módulos.
- Decision Engine desacoplado mediante LLMRequest.

---

# Historial de Releases

| Release    | Sprint | Módulo              | Estado |
| ---------- | :----: | ------------------- | :----: |
| v0.1.1     |    3   | Document Loader     |    ✅   |
| v0.2.0     |    4   | Text Splitter       |    ✅   |
| v0.3.0     |    5   | Metadata Manager    |    ✅   |
| v0.4.0     |    6   | Embeddings Engine   |    ✅   |
| v0.5.0     |    7   | Vector Store        |    ✅   |
| v0.6.0     |    8   | Retriever           |    ✅   |
| v0.7.0     |    9   | Context Builder     |    ✅   |
| v0.8.0     |   10   | Decision Engine  |    ✅   |
| **v0.9.0** | **11** | **Tools**        |  **✅** |
| **v1.0.0** | **12** | **LLM Provider** |  **⏳** |

# Observaciones

El desarrollo del proyecto sigue una metodología incremental basada en **Sprint → Hito → Release**, donde cada Sprint incorpora un nuevo módulo funcional al pipeline RAG.

Cada Release representa una versión estable del sistema y se publica únicamente después de completar:

- Implementación.
- Pruebas.
- Documentación técnica.
- Actualización de la trazabilidad.
- Cierre formal del Sprint.

El ROADMAP se actualiza al cierre de cada Sprint y constituye la referencia oficial para el seguimiento del avance del proyecto.

Con la Release v0.9.0, el proyecto incorpora la infraestructura del módulo Tools, consolidando un mecanismo desacoplado para el registro y ejecución de herramientas mediante interfaces y Factory Pattern. Con ello, el pipeline RAG queda preparado para integrar el LLM Provider y Google Gemini en el siguiente Sprint, manteniendo la compatibilidad con la arquitectura establecida desde los módulos anteriores.