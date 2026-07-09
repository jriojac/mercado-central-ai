# Mercado Central AI

Sistema de atención inteligente basado en IA para **Mercado Central 24h (México)**.

El proyecto implementa un agente conversacional utilizando un pipeline **RAG (Retrieval-Augmented Generation)**, desarrollado como parte del **Challenge de Alura + Oracle Next Education**.

---

## Estado del Proyecto

> **Versión estable:** **v0.6.0**

> **Estado:** Desarrollo activo

| Elemento                              | Estado                 |
| ------------------------------------- | ---------------------- |
| Arquitectura                          | ✅ Consolidada          |
| Documentación                         | ✅ Actualizada          |
| Sprint 3 – Hito 1 – Document Loader   | ✅ Finalizado           |
| Sprint 4 – Hito 2 – Text Splitter     | ✅ Finalizado           |
| Sprint 5 – Hito 3 – Metadata Manager  | ✅ Finalizado           |
| Sprint 6 – Hito 4 – Embeddings Engine | ✅ Finalizado           |
| Sprint 7 – Hito 5 – Vector Store      | ✅ Finalizado           |
| Sprint 8 – Hito 6 – Retriever         | ✅ Finalizado           |
| Release estable                       | **v0.7.0**              |
| Próxima Release                       | **v0.8.0** |


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

```text
Knowledge Base
        │
        ▼
Document Loader
        │
        ▼
Text Splitter
        │
        ▼
Metadata Manager
        │
        ▼
Embeddings Engine
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
Decision Engine
        │
        ▼
Gemini
        │
        ▼
Respuesta
```
---

## Estado del Pipeline RAG

Knowledge Base          ✅

↓

Document Loader         ✅

↓

Text Splitter           ✅

↓

Metadata Manager        ✅

↓

Embeddings Engine       ✅

↓

Vector Store            ✅

↓

Retriever               ✅

↓

Context Builder         ✅

↓

Gemini                  ⏳

↓

Respuesta               ⏳



## Metodología del Proyecto

### El desarrollo sigue una metodología incremental basada en:

Sprint
   │
   ▼
Hito
   │
   ▼
Implementación
   │
   ▼
Pruebas
   │
   ▼
Documentación
   │
   ▼
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


## Estructura del Proyecto
Challenge-Alura-Agente-IA/
│
├── 01_Documentacion/
│   ├── ADR/
│   ├── DIA/
│   ├── DOC/
│   │   ├── Hito_01/
│   │   └── Hito_02/
│   │   └── Hito_03&
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
│       │       ├──settings.py
│       │   ├── core/
│       │       ├── exceptions.py
│       │   ├── knowledge/
│       │       ├── loader.py
│       │       ├── text_splitter.py
│       │       ├── metadata.py
│       │       ├── embeddings.py
│       │       ├── vector_store.py
│       │       ├── provider.py
│       │       ├── constants.py
│       │       ├── types.py
│       │       ├── providers/
│       │       ├── chroma_provider.py
│       │   ├── llm/
│       │       ├── embedding_provider.py
│       │   ├── retriever/
│       │       ├── interfaces.py
│       │       ├── chroma_retriever.py
│       │       ├── retriever_factory.py
│       │   ├──context_builder/
│       │       ├── __init__.py
│       │       ├── interfaces.py
│       │       ├── simple_context_builder.py
│       │       └── context_builder_factory.py
│       │   ├── prompts/
│       │   ├── tools/
│       │   └── utils/
│       ├── temp/
│       │    ├── check_settings.py
│       │    ├── check_loader.py
│       │    ├── check_text_splitter.py
│       │    ├── check_loader_splitter.py
│       │    ├── check_metadata.py
│       │    ├── check_pipeline_embeddings.py
│       ├── tests/
│       │    ├── test_metadata.py
│       │    ├── test_embeddings.py
│       │    ├── test_vector_store.py
│       │    ├── test_retriever.py
│       │    ├── test_context_builde.py
│       └── app.py
│
├── 05_Pruebas/
├── 06_Presentacion/
├── 07_Entregables/
├── 08_Backups/
└── 09_Gestion_Proyecto/


## Roadmap

Sprint	Hito	Estado
|---------|------|:------:|
Sprint 3	Document Loader	✅
Sprint 4	Text Splitter	✅
Sprint 5	Metadata Manager✅
Sprint 6	Embeddings	✅
Sprint 7	Vector Store	✅
Sprint 8	Retriever	✅
Sprint 9	Context Builder	✅
Sprint 10	Decision Engine	⏳
Sprint 11	Tools	        ⏳
Sprint 12	Streamlit	⏳

---

# Módulos implementados

| Módulo | Estado |
|--------|:------:|
| Document Loader       | ✅ |
| Text Splitter         | ✅ |
| Metadata Manager      | ✅ |
| Embeddings            | ✅ |
| Vector Store          | ✅ |
| Retriever             | ✅  |
| Context Builder       | ⏳ |
| Decision Engine       | ⏳ |
| Tools                 | ⏳ |
| Streamlit UI          | ⏳ |

---

# Estrategia de Pruebas

El proyecto utiliza dos niveles de validación.

## 1. Pruebas de integración

Ubicación:
Estos scripts se utilizan durante el desarrollo para realizar validaciones rápidas de integración entre módulos.

```text
temp/
```

Scripts disponibles:

- check_settings.py
- check_loader.py
- check_text_splitter.py
- check_loader_splitter.py
- check_metadata.py

Estas pruebas permiten validar la integración progresiva del pipeline RAG durante el desarrollo.

---

## 2. Pruebas automatizadas

Ubicación:

```text
tests/
```

Framework utilizado:

- pytest

Actualmente se encuentran implementadas las pruebas automatizadas para:

- Metadata Manager
- Embeddings Engine
- Vector Store
- Retriever
- Context Builder

Ejecución:

```bash
python -m pytest
```

o

```bash
python -m pytest tests
```

---



## Validaciones oficiales

Los scripts oficiales del proyecto se ejecutan como módulos de Python:

```bash
python -m temp.check_settings

python -m temp.check_loader

python -m temp.check_text_splitter

python -m temp.check_loader_splitter

python -m temp.check_pipeline_embeddings

python -m temp.check_vector_store  

```

El módulo Vector Store fue validado mediante pruebas automatizadas implementadas con pytest.

## Documentación

La documentación del proyecto se organiza por categorías:

| Documento | Propósito |
|-----------|-----------|
| HANDBOOK | Metodología |
| ROADMAP | Planificación |
| LOG | Bitácora técnica |
| MTR | Matriz de trazabilidad |
| SDS | Diseño técnico |
| DOC | Documentación funcional |
| ADR | Decisiones arquitectónicas |


## Configuración

### Variables de entorno

El proyecto utiliza un archivo `.env` ubicado en la raíz de `04_Desarrollo/mercado-central-ai`.

Variables requeridas:

```env
GOOGLE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
```

El archivo `.env` no debe incluirse en el repositorio y se utiliza para configurar de forma segura el acceso a Google Generative AI.


## Tecnologías

- Python
- LangChain
- Google Gemini
- PyPDF
- python-dotenv
- pytest
- ChromaDB
- Streamlit *(planificado)*

## Versiones

| Versión | Contenido |
|----------|-----------|
| v0.1.1 | Document Loader |
| v0.2.0 | Text Splitter |
| v0.3.0 | Metadata Manager |
| v0.4.0 | Embeddings |
| v0.5.0 | Vector Store |
| v0.6.0 | Retriever |
| v0.7.0 | Context Builder |


## Incluye:

- Document Loader
- Text Splitter
- Metadata Manager
- Excepciones personalizadas
- Scripts oficiales de integración
- Pruebas automatizadas con pytest
- Arquitectura RAG
- Auditoría Arquitectónica
- Documentación técnica
- Matriz de trazabilidad
- Embeddings
- Embedding Provider
- Integración con Google Generative AI
- Vector Store
- VectorStoreProvider
- ChromaProvider
- ChromaDB
- Persistencia vectorial
- Búsqueda por similitud
- Gestión de colecciones
- IRetriever
- ChromaRetriever
- RetrieverFactory
- Configuración del Retriever
- Arquitectura basada en interfaces
- Factory Pattern
- ContextBuilderInterface
- SimpleContextBuilder
- ContextBuilderFactory
- Construcción de contexto
- Configuración del Context Builder


## Próximo objetivo

## Sprint 10 - Hito 8 – Decision Engine 

Implementar el módulo responsable de recibir el contexto generado por el Context Builder, aplicar la estrategia de decisión, construir la solicitud para el modelo Gemini y coordinar la generación de la respuesta del agente.

---

## Licencia

Proyecto desarrollado con fines académicos como parte del Challenge Alura + Oracle Next Education.