# Mercado Central AI

Sistema de atención inteligente basado en IA para **Mercado Central 24h (México)**.

El proyecto implementa un agente conversacional utilizando un pipeline **RAG (Retrieval-Augmented Generation)**, desarrollado como parte del **Challenge de Alura + Oracle Next Education**.

---

## Estado del Proyecto

> **Versión estable:** **v0.9.0**

> **Estado:** Desarrollo activo

| Elemento                              | Estado                 |
| --------------------------------------------- | ---------------------- |
| Arquitectura                                  | ✅ Consolidada          |
| Documentación                                 | ✅ Actualizada          |
| Sprint 3 – Hito 1 – Document Loader           | ✅ Finalizado           |
| Sprint 4 – Hito 2 – Text Splitter             | ✅ Finalizado           |
| Sprint 5 – Hito 3 – Metadata Manager          | ✅ Finalizado           |
| Sprint 6 – Hito 4 – Embeddings Engine         | ✅ Finalizado           |
| Sprint 7 – Hito 5 – Vector Store              | ✅ Finalizado           |
| Sprint 8 – Hito 6 – Retriever                 | ✅ Finalizado           |
| Sprint 9 – Hito 7 – Context Builder           | ✅ Finalizado           |
| Sprint 10 – Hito 8 – Decision Engine          | ✅ Finalizado           |
| Sprint 11 – Hito 9 – Tools (Infraestructura)  | ✅ Finalizado           |
| Release estable                               | **v0.9.0**               |
| Próxima Release                               | **v0.10.0**              |

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
Tool Manager
        │
        ▼
LLM Provider
        │
        ▼
Respuesta
```

A partir de la Release v0.9.0, el proyecto incorpora el módulo Tools, que introduce una infraestructura desacoplada para el registro y ejecución de herramientas especializadas mediante interfaces y Factory Pattern. Esta incorporación prepara la arquitectura para integrar capacidades adicionales sin modificar el núcleo del pipeline RAG.

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

Decision Engine         ✅

↓

Tools                   ✅

↓

LLM Provider            ⏳

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

```text
mercado-central-ai/
│
├── src/
│   ├── config/
│   ├── core/
│   ├── knowledge/
│   ├── retriever/
│   ├── context_builder/
│   ├── prompts/
│   ├── tools/
│   └── utils/
│
├── llm/
├── tests/
├── temp/
│
├── requirements.txt
├── README.md
└── app.py
```


| Carpeta           | Descripción                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `config`          | Configuración centralizada.                                          |
| `core`            | Componentes base del sistema.                                        |
| `knowledge`       | Pipeline RAG (Loader, Splitter, Metadata, Embeddings, Vector Store). |
| `retriever`       | Recuperación semántica de documentos.                                |
| `context_builder` | Construcción del contexto para el LLM.                               |
| `tests`           | Pruebas automatizadas con `pytest`.                                  |
| `temp`            | Pruebas manuales e integración.                                      |
| `llm`             | Modelos, interfaces, Decision Engine y futuros proveedores LLM.      |



## Roadmap

| Sprint    | Hito                                                          | Estado  |
| --------- | ------------------------------------------------------------- | ----    |
| Sprint 3  | Document Loader                                               |    ✅   |
| Sprint 4  | Text Splitter                                                 |    ✅   |
| Sprint 5  | Metadata Manager                                              |    ✅   |
| Sprint 6  | Embeddings Engine                                             |    ✅   |
| Sprint 7  | Vector Store                                                  |    ✅   |
| Sprint 8  | Retriever                                                     |    ✅   |
| Sprint 9  | Context Builder                                               |    ✅   |
| Sprint 10 | Decision Engine                                               |    ✅   |
| Sprint 11 | Tools                                                         |    ✅   |
| Sprint 12 | LLM Provider                                                  |    ⏳   |
| Sprint 13 | Streamlit                                                     |    ⏳   |

---

# Módulos implementados

| Módulo | Estado |
|--------|:------:|
| Document Loader       | ✅ |
| Text Splitter         | ✅ |
| Metadata Manager      | ✅ |
| Embeddings            | ✅ |
| Vector Store          | ✅ |
| Retriever             | ✅ |
| Context Builder       | ✅ |
| Decision Engine       | ✅ |
| Tools                 | ⏳ |
| LLM Provider          | ⏳ |
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
- ToolInterface
- ToolManager
- ToolFactory

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
- Decision Engine
- Decision Engine Factory
- LLMRequest

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

Las pruebas del **Decision Engine** se validan mediante pytest, al no requerir scripts manuales específicos en esta versión.

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
| v0.8.0 | Decision Engine |
| **v0.9.0** | Tools     |


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
- LLMRequest
- DecisionEngine
- DecisionEngineInterface
- DecisionEngineFactory
- Arquitectura desacoplada del proveedor LLM
- ToolInterface
- ToolManagerInterface
- ToolManager
- ToolFactory
- DuplicateToolError
- DummyTool


## Estadísticas del proyecto

| Indicador             |      Valor |
| --------------------- | ---------: |
| Sprint completados    |      **9** |
| Release estable       | **v0.9.0** |
| Módulos implementados |      **9** |
| Pruebas automatizadas |     **40** |
| Pruebas exitosas      |     **40** |


## Próximo objetivo

## Sprint 12 – LLM Provider

Implementar el proveedor LLM responsable de consumir las solicitudes generadas por el Decision Engine, integrar Google Gemini y completar el flujo del pipeline RAG manteniendo el desacoplamiento mediante interfaces y Factory Pattern.
---

## Licencia

Proyecto desarrollado con fines académicos como parte del Challenge Alura + Oracle Next Education.