# Mercado Central AI

Sistema inteligente basado en arquitectura **RAG (Retrieval-Augmented Generation)** desarrollado para el Challenge **Alura + Oracle Next Education**.

## Estado del proyecto

**Versión:** v1.2.0

**Estado:** Producción

**Despliegue:** Render

**URL pública:**

https://mercado-central-ai.onrender.com

---

# 🌐 Despliegue

La aplicación se encuentra desplegada en la nube mediante Render.

Puede utilizarse directamente desde cualquier navegador.

URL:

https://mercado-central-ai.onrender.com

> Debido al uso del plan gratuito de Render, el primer acceso puede tardar algunos segundos si la aplicación estuvo inactiva.

---
# Demo

Pruebe preguntas como:

- ¿Cuál es la política de devoluciones?
- ¿Cómo registrarse como proveedor?
- ¿Cuál es el horario de atención?
- ¿Qué productos perecederos pueden cambiarse?

---
## Interfaz de la aplicación

![Interfaz de Mercado Central AI](/imagen/MercadoCentralAI.png)

---
# Estado del Proyecto

> **Versión estable:** **v1.2.0**

> **Estado:** Proyecto funcional – Release Final Challenge

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
| Sprint 13 – Hito 11 – Streamlit UI | ✅ |
| Sprint 14 – Hito 12 – Inicialización Base Vectorial e Integración Final | ✅ |
| Release estable | **v1.2.0** |

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
Usuario
      │
      ▼
 Render Cloud
      │
      ▼
 Streamlit
      │
      ▼
 RAG Pipeline
      │
      ▼
 Retriever
      │
      ▼
 ChromaDB
      │
      ▼
 Gemini
      │
      ▼
 Respuesta
```

La arquitectura implementa un pipeline **RAG (Retrieval-Augmented Generation)** completamente desacoplado.

Cada módulo posee una única responsabilidad y se comunica mediante contratos públicos (Interfaces), permitiendo evolucionar el sistema sin afectar los componentes ya implementados.

La incorporación del **LLM Provider** completa la capa de integración con modelos de lenguaje y desacopla completamente el resto del sistema de LangChain y Google Gemini.

El sistema permite responder consultas en lenguaje natural utilizando exclusivamente la información contenida en la Base de Conocimiento. Para ello implementa una arquitectura RAG completa con recuperación semántica mediante ChromaDB y generación de respuestas mediante Google Gemini.
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
| Streamlit UI | ✅ |

Actualmente el pipeline RAG se encuentra completamente implementado e integrado.

El sistema permite responder consultas utilizando recuperación semántica mediante ChromaDB y generación de respuestas con Google Gemini a través de una interfaz desarrollada en Streamlit.

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
| Sprint 13 | Streamlit UI | ✅  |
| Sprint 14 | Inicialización Base Vectorial e Integración Final | ✅  |

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
| Streamlit UI | ✅ |
| RAG Pipeline Integrado | ✅ |


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
| Gemini 3 Flash Preview| Modelo de lenguaje utilizado por el sistema. |
| ChromaDB | Base de datos vectorial. |
| PyPDF | Carga y procesamiento de documentos PDF. |
| python-dotenv | Gestión de variables de entorno. |
| pytest | Pruebas automatizadas. |
| unittest.mock | Simulación de dependencias durante las pruebas. |
| Streamlit | Interfaz de usuario |

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
| v1.0.0 | LLM Provider |
| v1.1.0  | Streamlit UI                                           |
| v1.2.0  | Integración completa del Pipeline RAG + Base Vectorial |


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
- Interfaz gráfica con Streamlit.
- Pipeline RAG completamente integrado.
- Inicialización automática de la Base Vectorial.
- Consultas conversacionales.
- Recuperación semántica mediante ChromaDB.
- Respuestas fundamentadas exclusivamente en la Base de Conocimiento.

---

# Estadísticas del proyecto

| Indicador | Valor |
|-----------|------:|
| Sprint completados | 12 |
| Releases publicadas | 10 |
| Módulos implementados | 10 |
| Pruebas automatizadas | 43 |
| Pruebas exitosas | 43 |
| Fallos | 0 |


| Indicador             |                                                                                   Valor |
| --------------------- | --------------------------------------------------------------------------------------: |
| Sprint completados    |                                                                                  **12** |
| Releases publicadas   |                                                                                  **12** |
| Módulos implementados |                                                                                  **12** |
| Pruebas automatizadas |                                                                                  **43** |
| Pruebas exitosas      |                                                                                  **43** |
| Fallos                |                                                                                   **0** |


---

# Licencia

Proyecto desarrollado con fines académicos como parte del **Challenge Alura + Oracle Next Education**.





