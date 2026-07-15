# PLAN-011
# Sprint 13 – Hito 11
# Interfaz Streamlit

Versión: 1.0
Estado: EN DESARROLLO
Release asociada: v1.1.0

---

# 1. Información del documento

| Campo | Valor |
|--------|-------|
| Documento | SDS-010 |
| Título | Software Design Specification – LLM Provider |
| Versión | 1.0 |
| Estado | Finalizado |
| Sprint | 12 |
| Hito | 10 |
| Módulo | LLM Provider |
| Release objetivo | v1.0.0 |
| Dependencia | Decision Engine (Sprint 10) |
| Autor | Jacqueline Rioja |
| Fecha | 11/07/2026 |
| Última actualización | 11/07/2026 |

---

# 2. Objetivo

Implementar la interfaz gráfica del proyecto Mercado Central AI mediante Streamlit, integrando el pipeline RAG desarrollado en los Sprint anteriores y validando su funcionamiento de extremo a extremo.


---

# 3. Contexto Arquitectónico

Hasta el Sprint 11, el pipeline RAG finalizaba en el **Decision Engine**, responsable de construir una solicitud (`LLMRequest`) preparada para ser procesada por un proveedor de modelos de lenguaje.

Con el Sprint 12 se incorpora el módulo **LLM Provider**, cuya responsabilidad consiste en encapsular toda la comunicación con el proveedor LLM, manteniendo desacoplado al resto del sistema de las implementaciones concretas de LangChain y Google Gemini.

La arquitectura resultante es la siguiente:

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
LLM Provider
        │
        ▼
Google Gemini
```

El **Decision Engine** mantiene su responsabilidad exclusiva de construir el objeto `LLMRequest`.

La ejecución del modelo de lenguaje queda delegada al **LLM Provider**, preservando el principio de Responsabilidad Única (SRP).

---

# 4. Alcance

## Incluye

El módulo implementa:

- Aplicación app.py.
- Implementación de StreamlitApp.
- Implementación de PromptBuilder.
- Implementación de RAGPipeline.
- Implementación de RAGPipelineFactory.
- Integración con:
      * Retriever.
      * Context Builder.
      * Decision Engine.
      * LLM Provider.
      * Google Gemini.
- Integración con @st.cache_resource.
- Validación funcional mediante Streamlit.

## No incluye

No forman parte del presente Sprint:

- Memoria conversacional.
- Historial de conversaciones.
- Persistencia de chats.
- Autenticación.
- Despliegue en la nube.
- Inicialización automática de la Base Vectorial (Chroma).

---

# 5. Responsabilidades del módulo

El flujo funcional del módulo puede representarse mediante el siguiente diagrama:

```text
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

## El módulo será responsable de:

- inicializar el proveedor LLM configurado;
- enviar solicitudes al modelo de lenguaje;
- recibir la respuesta generada;
- encapsular la comunicación con LangChain;
- abstraer la implementación concreta del proveedor.

## El módulo no será responsable de:

- recuperar documentos;
- consultar ChromaDB;
- construir contexto;
- construir el `LLMRequest`;
- ejecutar herramientas;
- administrar conversaciones;
- controlar la interfaz de usuario.

Esta separación garantiza el cumplimiento del principio de Responsabilidad Única (SRP) y mantiene desacoplados los componentes del pipeline RAG.

---

# 6. Arquitectura del módulo

El módulo **LLM Provider** adopta la arquitectura estándar utilizada por los componentes del pipeline RAG, basada en **Interfaces**, **Factory Pattern** y **Responsabilidad Única (SRP)**.

La organización del paquete es la siguiente:

```text
src/
└── llm/
    ├── interfaces.py
    ├── llm_factory.py
    ├── decision_engine.py
    ├── decision_engine_factory.py
    ├── models.py
    ├── providers/
    │      └── google_gemini_provider.py
    └── __init__.py
```

Esta estructura mantiene la uniformidad arquitectónica con los módulos implementados en los Sprint anteriores y facilita la incorporación de nuevos proveedores sin modificar los consumidores del módulo.

---

# 7. Componentes del módulo

## 7.1 LLMProviderInterface

Define el contrato público que deberán implementar todos los proveedores de modelos de lenguaje.

Responsabilidades:

- definir la operación `generate_response()`;
- desacoplar el consumidor de implementaciones concretas;
- garantizar un contrato estable para futuros proveedores.

---

## 7.2 GoogleGeminiProvider

Implementación concreta del contrato `LLMProviderInterface`.

Responsabilidades:

- inicializar el cliente `ChatGoogleGenerativeAI`;
- enviar solicitudes al modelo Gemini;
- devolver el contenido generado;
- encapsular completamente el uso de LangChain y Google Gemini.

---

## 7.3 LLMProviderFactory

Responsable de crear el proveedor configurado por el sistema.

Actualmente instancia:

- GoogleGeminiProvider

La utilización de una Factory permite incorporar nuevos proveedores sin modificar el código consumidor.

---

## 7.4 DecisionEngine

El Decision Engine no forma parte del módulo LLM Provider, pero constituye su dependencia funcional inmediata.

Su responsabilidad consiste exclusivamente en construir una instancia de `LLMRequest`, que posteriormente podrá ser utilizada por el proveedor LLM.

---

# 8. Diagrama de componentes

```text
                  Decision Engine
                          │
                          │ construye
                          ▼
                     LLMRequest
                          │
                          │ consume
                          ▼
              LLMProviderInterface
                          ▲
                          │ implementa
            ┌─────────────┴─────────────┐
            │                           │
GoogleGeminiProvider         Future Providers
            │
            ▼
 ChatGoogleGenerativeAI
            │
            ▼
      Google Gemini
```

La dependencia con LangChain queda completamente encapsulada dentro de `GoogleGeminiProvider`, evitando que el resto del sistema conozca detalles de implementación.

---

# 9. Flujo interno del módulo

El procesamiento del módulo puede representarse mediante el siguiente flujo:

```text
LLMRequest
      │
      ▼
LLMProviderFactory
      │
      ▼
GoogleGeminiProvider
      │
      ▼
ChatGoogleGenerativeAI
      │
      ▼
invoke()
      │
      ▼
AIMessage
      │
      ▼
response.content
      │
      ▼
str
```

El método `generate_response()` adapta la respuesta devuelta por LangChain (`AIMessage`) al contrato público del módulo (`str`), evitando exponer tipos propios de bibliotecas externas.

---

# 10. Patrón arquitectónico

El módulo implementa los siguientes patrones de diseño:

| Patrón | Aplicación |
|---------|------------|
| Interface | Contrato entre consumidores y proveedores LLM. |
| Factory Pattern | Creación centralizada del proveedor configurado. |
| Dependency Inversion | El consumidor depende de `LLMProviderInterface` y no de implementaciones concretas. |
| SRP | Cada componente posee una única responsabilidad claramente definida. |
| OCP | La incorporación de nuevos proveedores no requiere modificar el código existente. |



---

# 11. Configuración del módulo

Toda la configuración del módulo permanece centralizada en:

```text
src/config/settings.py
```

Los principales parámetros utilizados por el proveedor Google Gemini son:

- `GOOGLE_API_KEY`
- `GEMINI_MODEL`
- `GEMINI_TEMPERATURE`
- `GEMINI_MAX_OUTPUT_TOKENS`
- `LLM_PROVIDER`

La configuración centralizada evita valores hardcodeados dentro de la implementación y facilita la incorporación de nuevos proveedores LLM.

---

# 12. Modelo de datos

El módulo no define modelos de datos propios.

La interacción con el resto del pipeline se realiza utilizando el modelo:

```text
LLMRequest
```

Este modelo es construido por el **Decision Engine** y contiene toda la información necesaria para preparar una solicitud hacia un proveedor LLM.

La responsabilidad del LLM Provider comienza una vez recibido el `LLMRequest` o el prompt construido a partir de éste.

---

# 13. Interfaces públicas

El contrato público del módulo queda definido mediante:

## LLMProviderInterface

```python
generate_response(
    prompt: str,
) -> str
```

### Entrada

| Campo | Tipo | Descripción |
|--------|------|-------------|
| prompt | str | Prompt completamente construido por el Decision Engine. |

### Salida

| Campo | Tipo | Descripción |
|--------|------|-------------|
| response | str | Respuesta generada por el proveedor LLM. |

Este contrato garantiza que el resto del sistema permanezca independiente de la implementación concreta del proveedor.

---

# 14. Contrato de la API (API Contract)

## Precondiciones

Antes de invocar el proveedor deberán cumplirse las siguientes condiciones:

- El proveedor debe haber sido creado mediante `LLMProviderFactory`.
- La configuración debe encontrarse correctamente inicializada.
- El prompt debe recibirse como una cadena (`str`).

## Postcondiciones

Después de ejecutar `generate_response()` se garantiza que:

- se devuelve una respuesta textual (`str`);
- el consumidor no recibe objetos propios de LangChain;
- la implementación concreta del proveedor permanece encapsulada.

---

# 15. Reglas de validación

| ID | Regla |
|----|--------|
| RV-1001 | Todo proveedor deberá implementar `LLMProviderInterface`. |
| RV-1002 | La creación del proveedor será responsabilidad exclusiva de `LLMProviderFactory`. |
| RV-1003 | El método `generate_response()` deberá devolver un `str`. |
| RV-1004 | El resto del sistema no deberá depender directamente de `ChatGoogleGenerativeAI`. |
| RV-1005 | Toda configuración deberá obtenerse desde `settings.py`. |

Estas reglas garantizan la uniformidad arquitectónica del proyecto y facilitan la incorporación de nuevos proveedores sin modificar los consumidores.

---

# 16. Manejo de errores

Durante la implementación del Sprint 12 se adoptó la política general del proyecto para el manejo de errores.

La implementación evita propagar detalles internos de bibliotecas externas hacia el resto del sistema.

Los errores relacionados con:

- configuración;
- inicialización;
- comunicación con el proveedor;

podrán encapsularse mediante excepciones específicas del dominio en futuras versiones.

En la versión actual se mantiene la política de centralización de excepciones definida para el proyecto.

---

# 17. Consideraciones de rendimiento

El módulo fue diseñado para minimizar la sobrecarga durante la comunicación con el proveedor LLM.

Para ello:

- el cliente `ChatGoogleGenerativeAI` se inicializa una única vez por instancia del proveedor;
- se evita recrear el cliente en cada solicitud;
- el método `generate_response()` realiza únicamente la invocación al modelo y la adaptación de la respuesta al contrato público (`str`);
- no se mantiene estado interno entre solicitudes, permitiendo un comportamiento liviano y fácilmente reutilizable.

Esta estrategia reduce el acoplamiento con la biblioteca LangChain y simplifica futuras optimizaciones del módulo.



---

# 18. Estrategia de pruebas

La validación del módulo se realizó mediante pruebas unitarias implementadas con **pytest**, siguiendo la metodología incremental utilizada durante todo el proyecto.

Las pruebas verifican:

- implementación del contrato `LLMProviderInterface`;
- creación del proveedor mediante `LLMProviderFactory`;
- funcionamiento de `generate_response()`;
- utilización de **Mock** para evitar dependencias con la API de Google Gemini;
- validación de la API pública sin acceder a atributos privados.

Las validaciones manuales continúan realizándose desde la carpeta:

```text
temp/
```

Las pruebas automatizadas permanecen en:

```text
tests/
```

---

# 19. Casos de prueba

| Caso | Objetivo | Requisito |
|------|----------|-----------|
| CP-1001 | Validar `LLMProviderInterface`. | RV-1001 |
| CP-1002 | Validar `GoogleGeminiProvider`. | RV-1003 |
| CP-1003 | Validar `LLMProviderFactory`. | RV-1002 |
| CP-1004 | Validar `generate_response()` mediante Mock. | RV-1004 |

## Resultado obtenido

Al finalizar el Sprint se obtuvieron los siguientes resultados:

- 43 pruebas ejecutadas.
- 43 pruebas exitosas.
- 0 pruebas fallidas.
- 1 warning conocido correspondiente a ChromaDB con Python 3.14.
- Cobertura funcional del Sprint: 100 %.

---

# 20. Registro de Decisiones Arquitectónicas (ADR)

| ADR | Decisión | Justificación |
|-----|----------|---------------|
| ADR-010-01 | Uso de `LLMProviderInterface`. | Define un contrato estable para todos los proveedores LLM. |
| ADR-010-02 | Uso de `LLMProviderFactory`. | Centraliza la creación del proveedor configurado. |
| ADR-010-03 | Encapsular LangChain dentro del Provider. | Evita dependencias directas con bibliotecas externas. |
| ADR-010-04 | Mantener la configuración en `settings.py`. | Elimina valores hardcodeados y facilita el mantenimiento. |
| ADR-010-05 | El `DecisionEngine` mantiene la responsabilidad exclusiva de construir `LLMRequest`. | Preserva el principio de Responsabilidad Única (SRP) y evita acoplar el motor de decisión con la ejecución del proveedor LLM. |
| ADR-010-06 | Validar el Provider mediante Mock. | Permite pruebas unitarias independientes de Internet, API Keys y cuota de Google Gemini. |

---

# 21. Riesgos identificados

| Riesgo | Mitigación |
|---------|------------|
| Cambios en la API de Google Gemini. | Encapsular la integración en `GoogleGeminiProvider`. |
| Cambios en LangChain. | Limitar el uso de LangChain al Provider. |
| Incorporación de nuevos proveedores. | Uso de `LLMProviderInterface` y `LLMProviderFactory`. |
| Cambios en la configuración. | Centralización mediante `settings.py`. |

---

# 22. Estado de implementación

| Implementación | Estado |
|---------------|:------:|
| Arquitectura del módulo | ✅ |
| LLMProviderInterface | ✅ |
| GoogleGeminiProvider | ✅ |
| LLMProviderFactory | ✅ |
| Configuración centralizada | ✅ |
| Validaciones manuales | ✅ |
| Pruebas automatizadas | ✅ |
| Documentación técnica | ✅ |

---

# 23. Resultados del Sprint

Durante el Sprint 12 se implementó satisfactoriamente la infraestructura del módulo **LLM Provider**.

Resultados obtenidos:

- Implementación de `LLMProviderInterface`.
- Implementación de `GoogleGeminiProvider`.
- Implementación de `LLMProviderFactory`.
- Configuración centralizada mediante `settings.py`.
- Validación incremental mediante pruebas manuales y automatizadas.
- 43 pruebas ejecutadas.
- 43 pruebas exitosas.
- Arquitectura desacoplada validada.
- Preparación de la Release v1.0.0.

---

# 24. Trazabilidad

| Artefacto | Relación |
|-----------|----------|
| PLAN-010 | Planificación del Sprint 12 |
| SDS-010 | Diseño técnico del módulo LLM Provider |
| IMP-01 | Diseño arquitectónico |
| IMP-02 | Implementación de la interfaz |
| IMP-03 | Implementación del Provider |
| IMP-04 | Implementación de la Factory |
| IMP-05 | Validación técnica y documentación |
| MTR-010 | Matriz de trazabilidad |
| Release v1.0.0 | Entrega del Sprint |

---

# 25. Control de versiones

| Versión | Cambios |
|---------|---------|
| 1.0 | Creación del SDS-010 y diseño arquitectónico del módulo **LLM Provider**. |
| 1.1 | Implementación de `LLMProviderInterface`, `GoogleGeminiProvider` y `LLMProviderFactory`; incorporación de configuración centralizada; validación mediante 43 pruebas exitosas; registro de decisiones arquitectónicas (ADR) y cierre del Sprint 12. |