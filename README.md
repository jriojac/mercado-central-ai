# Mercado Central AI

Sistema de atención inteligente basado en IA para **Mercado Central 24h (México)**.

El proyecto implementa un agente conversacional utilizando un pipeline **RAG (Retrieval-Augmented Generation)**, desarrollado como parte del **Challenge de Alura + Oracle Next Education**.

---

## Estado del Proyecto

| Elemento | Estado |
|-----------|--------|
| Arquitectura | ✅ Consolidada |
| Documentación | ✅ Actualizada |
| Hito 1 | ✅ Finalizado |
| Sprint actual | Sprint 4 |
| Próximo módulo | Text Splitter |
| Release actual | v0.1.1 |

---

## Objetivo

Construir un agente inteligente capaz de responder consultas relacionadas con:

- Atención al cliente.
- Operación del supermercado.
- Políticas internas.
- Gestión de proveedores.
- Inventario.
- Información corporativa.

La información proviene exclusivamente de la Base de Conocimiento del proyecto.

---

## Arquitectura General

Knowledge Base
        │
        ▼
Document Loader
        │
        ▼
Text Splitter
        │
        ▼
Metadata
        │
        ▼
Embeddings
        │
        ▼
Vector Store
        │
        ▼
Retriever
        │
        ▼
Context Builder
        │
        ▼
Gemini
        │
        ▼
Respuesta


---

## Metodología del Proyecto

### El desarrollo sigue una metodología incremental basada en:

Sprint
      ↓
Hito
      ↓
Release

### Cada Hito sigue obligatoriamente el siguiente flujo:

Planificación
      ↓
SDS
      ↓
Implementación
      ↓
Pruebas
      ↓
Documentación
      ↓
Git
      ↓
Release


## La metodología completa se encuentra documentada en:

01_Documentacion/
HANDBOOK/
HANDBOOK-001_Guia_Desarrollo
Estructura del Proyecto
Challenge-Alura-Agente-IA/
│
├── 01_Documentacion/
│   ├── ADR/
│   ├── DIA/
│   ├── DOC/
│   │   ├── Hito_01/
│   │   └── Hito_02/
│   ├── HANDBOOK/
│   ├── INST/
│   ├── LOG/
│   ├── MTR/
│   ├── ROADMAP/
│   └── SDS/
│
├── 02_Recursos_Alura/
│
├── 03_Knowledge_Base/
│
├── 04_Desarrollo/
│   └── mercado-central-ai/
│       ├── src/
│       │   ├── config/
│       │   ├── core/
│       │   ├── knowledge/
│       │   ├── llm/
│       │   ├── prompts/
│       │   ├── tools/
│       │   └── utils/
│       │
│       ├── temp/
│       ├── tests/
│       └── app.py
│
├── 05_Pruebas/
├── 06_Presentacion/
├── 07_Entregables/
├── 08_Backups/
└── 09_Gestion_Proyecto/


## Roadmap

Sprint	Hito	Estado
Sprint 3	Document Loader	✅
Sprint 4	Text Splitter	🔜
Sprint 5	Metadata	⏳
Sprint 6	Embeddings	⏳
Sprint 7	Vector Store	⏳
Sprint 8	Retriever	⏳
Sprint 9	Context Builder	⏳
Sprint 10	Decision Engine	⏳
Sprint 11	Tools	⏳
Sprint 12	Streamlit	⏳
Validaciones oficiales

## Los scripts oficiales del proyecto se ejecutan como módulos de Python:

python -m temp.check_settings

python -m temp.check_loader

Estos scripts permiten verificar la configuración del proyecto y el correcto funcionamiento del Document Loader.

## Documentación

La documentación del proyecto se organiza por categorías:

Documento	Propósito
HANDBOOK	Metodología
ROADMAP	Planificación
LOG	Bitácora técnica
MTR	Trazabilidad
SDS	Diseño técnico
DOC	Documentación funcional
ADR	Decisiones arquitectónicas
Tecnologías
Python
LangChain
Google Gemini
PyPDF
ChromaDB (planificado)
Streamlit (planificado)
Release actual

## Versión

v0.1.1

## Incluye:

Document Loader.
Arquitectura consolidada.
Auditoría Arquitectónica.
Scripts oficiales de validación.
Documentación actualizada.
Próximo objetivo

## Sprint 4  - Hito 2

Text Splitter

## Licencia

Proyecto desarrollado con fines académicos como parte del Challenge Alura + Oracle Next Education.