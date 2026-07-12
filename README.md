# Mercado Central AI

Sistema inteligente de atención al cliente basado en Inteligencia Artificial para **Mercado Central 24h (México)**.

El proyecto implementa un agente conversacional utilizando una arquitectura **RAG (Retrieval-Augmented Generation)**, desarrollado como parte del **Challenge de Alura + Oracle Next Education**.

La solución integra un pipeline modular basado en **Python**, **LangChain**, **ChromaDB** y **Google Gemini**, siguiendo una arquitectura desacoplada mediante **Interfaces**, **Factory Pattern** y **Configuración Centralizada**.

---

# Estado del Proyecto

> **Versión estable:** **v1.0.0**

> **Estado:** Desarrollo activo

| Elemento | Estado |
|----------|:------:|
| Arquitectura | ✅ Consolidada |
| Documentación | ✅ Actualizada |
| Sprint 3 – Hito 1 – Document Loader | ✅ |
| Sprint 4 – Hito 2 – Text Splitter | ✅ |
| Sprint 5 – Hito 3 – Metadata Manager | ✅ |
| Sprint 6 – Hito 4 – Embeddings Engine | ✅ |
| Sprint 7 – Hito 5 – Vector Store | ✅ |
| Sprint 8 – Hito 6 – Retriever | ✅ |
| Sprint 9 – Hito 7 – Context Builder | ✅ |
| Sprint 10 – Hito 8 – Decision Engine | ✅ |
| Sprint 11 – Hito 9 – Tools | ✅ |
| Sprint 12 – Hito 10 – LLM Provider | ✅ |
| Release estable | **v1.0.0** |
| Próximo Sprint | **Sprint 13 – Streamlit UI** |

---

# Objetivo

Construir un agente inteligente capaz de responder consultas relacionadas con la operación de **Mercado Central 24h**, utilizando exclusivamente la información disponible en la Base de Conocimiento del proyecto.

Actualmente el sistema es capaz de procesar información relacionada con:

- Atención al cliente.
- Operación del supermercado.
- Políticas internas.
- Gestión de proveedores.
- Inventario.
- Información corporativa.

El proyecto mantiene una arquitectura modular que permite evolucionar el pipeline RAG de forma incremental, preservando el desacoplamiento entre sus componentes y facilitando la incorporación de nuevas capacidades en futuras versiones.


---

# Arquitectura General

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
LLMRequest
        │
        ▼
LLM Provider
        │
        ▼
Google Gemini
        │
        ▼
Respuesta
```

La arquitectura implementa un pipeline **RAG (Retrieval-Augmented Generation)** completamente desacoplado.

Cada módulo posee una única responsabilidad y se comunica mediante contratos públicos (Interfaces), permitiendo evolucionar el sistema sin afectar los componentes ya implementados.

La incorporación del **LLM Provider** completa la capa de integración con modelos de lenguaje y desacopla completamente el resto del sistema de LangChain y Google Gemini.

---

# Estado del Pipeline RAG

| Componente | Estado |
|------------|:------:|
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

Actualmente la infraestructura principal del pipeline RAG se encuentra completamente implementada.

El siguiente Sprint estará orientado a incorporar la interfaz de usuario mediante **Streamlit**, reutilizando todos los componentes desarrollados durante los Sprint anteriores.

---

# Metodología del Proyecto

El desarrollo sigue una metodología incremental basada en entregas funcionales y documentación sincronizada.

Cada Sprint desarrolla un único módulo del pipeline RAG siguiendo el flujo:

```text
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
```

Cada Hito se desarrolla mediante microentregas siguiendo el proceso:

```text
Analizar
      │
      ▼
Proponer
      │
      ▼
Implementar
      │
      ▼
Validar
      │
      ▼
Refactorizar
      │
      ▼
Documentar
      │
      ▼
Publicar
```

Toda la metodología del proyecto se encuentra documentada en:

```text
01_Documentacion/
└── HANDBOOK/
    └── HANDBOOK-001_Guia_Desarrollo.md
```

---

# Roadmap

| Sprint | Módulo | Estado |
|---------|--------|:------:|
| Sprint 3 | Document Loader | ✅ |
| Sprint 4 | Text Splitter | ✅ |
| Sprint 5 | Metadata Manager | ✅ |
| Sprint 6 | Embeddings Engine | ✅ |
| Sprint 7 | Vector Store | ✅ |
| Sprint 8 | Retriever | ✅ |
| Sprint 9 | Context Builder | ✅ |
| Sprint 10 | Decision Engine | ✅ |
| Sprint 11 | Tools | ✅ |
| Sprint 12 | LLM Provider | ✅ |
| Sprint 13 | Streamlit UI | ⏳ |

---

# Estructura del Proyecto

```text
mercado-central-ai/
│
├── src/
│   ├── config/
│   ├── core/
│   ├── knowledge/
│   ├── retriever/
│   ├── context_builder/
│   ├── llm/
│   ├── prompts/
│   ├── tools/
│   └── utils/
│
├── tests/
├── temp/
│
├── requirements.txt
├── README.md
└── app.py
```

| Carpeta | Descripción |
|----------|-------------|
| `config` | Configuración centralizada del proyecto. |
| `core` | Componentes y excepciones compartidas. |
| `knowledge` | Document Loader, Text Splitter, Metadata, Embeddings y Vector Store. |
| `retriever` | Recuperación semántica de documentos. |
| `context_builder` | Construcción del contexto para el LLM. |
| `llm` | Decision Engine, modelos, interfaces, Provider y Factory del LLM. |
| `tools` | Infraestructura para herramientas especializadas. |
| `tests` | Pruebas automatizadas con `pytest`. |
| `temp` | Validaciones manuales e integración incremental. |

---

# Módulos implementados

| Módulo | Estado |
|---------|:------:|
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
| Streamlit UI | ⏳ |

---

# Estrategia de Pruebas

El proyecto utiliza dos niveles de validación para garantizar la calidad del código.

## 1. Validaciones manuales

Ubicación:

```text
temp/
```

Estos scripts permiten comprobar de forma incremental el funcionamiento de cada módulo antes de incorporarlo a la suite de pruebas automatizadas.

Entre las validaciones disponibles se encuentran:

- Configuración (`settings.py`)
- Document Loader
- Text Splitter
- Metadata Manager
- Embeddings
- Vector Store
- Retriever
- Context Builder
- Decision Engine
- GoogleGeminiProvider
- LLMProviderFactory

---

## 2. Pruebas automatizadas

Ubicación:

```text
tests/
```

Framework utilizado:

- `pytest`
- `unittest.mock`

Actualmente el proyecto incluye pruebas automatizadas para:

- Document Loader
- Text Splitter
- Metadata Manager
- Embeddings Engine
- Vector Store
- Retriever
- Context Builder
- Decision Engine
- LLM Provider
- LLM Provider Factory

Ejecución:

```bash
python -m pytest
```

o

```bash
python -m pytest tests
```

Resultado actual:

```text
43 passed
1 warning (ChromaDB con Python 3.14)
```

---

# Configuración

El proyecto utiliza un archivo `.env` ubicado en la raíz del repositorio para almacenar las credenciales necesarias.

Variables principales:

```env
GOOGLE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
```

La configuración específica del sistema permanece centralizada en:

```text
src/config/settings.py
```

El archivo `.env` no debe incluirse en el repositorio Git.


---

# Tecnologías utilizadas

El proyecto fue desarrollado utilizando las siguientes tecnologías:

| Tecnología | Uso |
|------------|-----|
| Python | Lenguaje principal del proyecto. |
| LangChain | Orquestación de componentes LLM. |
| Google Gemini | Modelo de lenguaje utilizado por el sistema. |
| ChromaDB | Base de datos vectorial. |
| PyPDF | Carga y procesamiento de documentos PDF. |
| python-dotenv | Gestión de variables de entorno. |
| pytest | Pruebas automatizadas. |
| unittest.mock | Simulación de dependencias durante las pruebas. |
| Streamlit | Interfaz de usuario (Sprint 13). |

---

# Historial de versiones

| Versión | Contenido |
|----------|-----------|
| v0.1.1 | Document Loader |
| v0.2.0 | Text Splitter |
| v0.3.0 | Metadata Manager |
| v0.4.0 | Embeddings Engine |
| v0.5.0 | Vector Store |
| v0.6.0 | Retriever |
| v0.7.0 | Context Builder |
| v0.8.0 | Decision Engine |
| v0.9.0 | Tools |
| **v1.0.0** | **LLM Provider** |

---

# Principales funcionalidades implementadas

El proyecto incorpora actualmente:

- Arquitectura RAG completa.
- Document Loader.
- Text Splitter.
- Metadata Manager.
- Embeddings Engine.
- Vector Store.
- Retriever semántico.
- Context Builder.
- Decision Engine.
- Infraestructura de Tools.
- LLM Provider.
- Integración con Google Gemini.
- Configuración centralizada mediante `settings.py`.
- Arquitectura basada en Interfaces.
- Factory Pattern.
- Validaciones manuales.
- Pruebas automatizadas con `pytest`.
- Documentación técnica sincronizada.
- Arquitectura desacoplada y extensible.

---

# Estadísticas del proyecto

| Indicador | Valor |
|-----------|------:|
| Sprint completados | 10 |
| Releases publicadas | 10 |
| Módulos implementados | 10 |
| Pruebas automatizadas | 43 |
| Pruebas exitosas | 43 |
| Fallos | 0 |

---

# Próximo objetivo

## Sprint 13 – Interfaz Streamlit

El siguiente Sprint estará orientado a desarrollar la interfaz de usuario del proyecto utilizando **Streamlit**.

Los objetivos principales serán:

- Integrar el pipeline RAG completo.
- Consumir el módulo **LLM Provider**.
- Mostrar respuestas generadas por Google Gemini.
- Diseñar una interfaz sencilla para consultas.
- Preparar el sistema para una demostración funcional de extremo a extremo (End-to-End).

Con este Sprint se completará el flujo principal del proyecto **Mercado Central AI**, permitiendo interactuar con el agente conversacional desde una interfaz gráfica.

---

# Licencia

Proyecto desarrollado con fines académicos como parte del **Challenge Alura + Oracle Next Education**.





