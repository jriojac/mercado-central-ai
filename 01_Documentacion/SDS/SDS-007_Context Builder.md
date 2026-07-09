# SDS-007
# Software Design Specification
## Módulo: Context Builder
## Versión: 1.0
## Release objetivo: v0.7.0


---

# 1. Información del documento

| Campo                | Valor                                           |
| -------------------- | ----------------------------------------------- |
| Documento            | SDS-007                                         |
| Título               | Software Design Specification – Context Builder |
| Versión              | 1.0                                             |
| Estado               | En desarrollo                                   |
| Sprint               | 9                                               |
| Hito                 | 7                                               |
| Módulo               | Context Builder                                 |
| Release objetivo     | v0.7.0                                          |
| Dependencia          | Retriever (Sprint 8)                            |
| Autor                | Jacqueline Rioja                                |
| Fecha                | 08/07/2026                                      |
| Última actualización | *(Actualizar al cierre)*                        |


---

# 2. Objetivo

El objetivo de este documento es definir el diseño técnico del módulo Context Builder, responsable de transformar la colección de documentos recuperados por el módulo Retriever en un contexto textual único, estructurado y configurable, listo para ser consumido por el Decision Engine.

El diseño del módulo mantiene los principios arquitectónicos consolidados durante el desarrollo del proyecto Mercado Central AI:

- Responsabilidad única (SRP).
- Bajo acoplamiento.
- Alta cohesión.
- Programación orientada a interfaces.
- Configuración centralizada.
- Uso de Factory Pattern.
- Compatibilidad con la arquitectura RAG.
- Independencia del proveedor LLM.

---

# 3. Alcance

## Incluye

El módulo deberá permitir:

- Definición de la interfaz ContextBuilderInterface.
- Implementación de SimpleContextBuilder.
- Construcción de un contexto textual único a partir de documentos recuperados.
- Preservación del orden de relevancia recibido del Retriever.
- Configuración centralizada mediante settings.py.
- Implementación de ContextBuilderFactory.
- Definición del contrato de entrada y salida.
- Preparación para futuras estrategias de construcción de contexto.

## No incluye

- Recuperación de documentos.
- Re-ranking.
- Prompt Engineering.
- Decision Engine.
- Invocación del modelo Gemini.
- Generación de respuestas.
- Herramientas (Tools).
- Interfaz Streamlit.

---

# 4. Referencias

Documentos relacionados:

- PLAN-007
- SDS-006 – Retriever
- MTR-001
- README
- HANDBOOK
- ROADMAP
- CHANGELOG
- LOG

---

# 5. Contexto dentro del Pipeline RAG

El Context Builder representa la transición entre la recuperación de información y la generación de respuestas.

Su responsabilidad consiste en transformar una colección de documentos relevantes en un único contexto textual que posteriormente será utilizado por el Decision Engine para construir la solicitud que será enviada al modelo de lenguaje.

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
LLM (Gemini)

```

## Entrada

| Campo     | Tipo             | Descripción                                                        |
| --------- | ---------------- | ------------------------------------------------------------------ |
| documents | `list[Document]` | Documentos recuperados por el Retriever, ordenados por relevancia. |

## Procesamiento
 
Durante el procesamiento el módulo:

- Validar la colección recibida.
- Preservar el orden de los documentos.
- Eliminar contenido vacío cuando corresponda.
- Aplicar la configuración definida en settings.py.
- Construir un contexto textual único.
- Entregar el contexto al Decision Engine.

## Salida

| Campo   | Tipo  | Descripción                                                                   |
| ------- | ----- | ----------------------------------------------------------------------------- |
| context | `str` | Contexto textual consolidado listo para ser utilizado por el Decision Engine. |


---

# 6. Requerimientos funcionales

| ID         | Descripción                                                                             |
| ---------- | --------------------------------------------------------------------------------------- |
| **RF-701** | Definir la interfaz `ContextBuilderInterface` como contrato público del módulo.         |
| **RF-702** | Construir un contexto textual único a partir de una colección de documentos.            |
| **RF-703** | Preservar el orden de relevancia entregado por el Retriever.                            |
| **RF-704** | Centralizar la configuración del módulo mediante `settings.py`.                         |
| **RF-705** | Implementar `SimpleContextBuilder` como primera estrategia de construcción de contexto. |
| **RF-706** | Implementar `ContextBuilderFactory` como punto único de creación de dependencias.       |
| **RF-707** | Mantener independencia respecto al modelo LLM y al Decision Engine.                     |

---

# 7. Responsabilidades del módulo

El Context Builder será responsable exclusivamente de transformar la información recuperada por el Retriever en un contexto textual consolidado.

Su flujo funcional puede representarse de la siguiente manera:

Documentos recuperados
        │
        ▼
Validación
        │
        ▼
Preservación del orden
        │
        ▼
Construcción del contexto
        │
        ▼
Aplicación de configuración
        │
        ▼
Contexto consolidado

## Responsabilidad
| RF         | Responsabilidad                           |
| ---------- | ----------------------------------------- |
| **RF-702** | Construir un único contexto textual.      |
| **RF-703** | Mantener el orden recibido del Retriever. |
| **RF-704** | Aplicar la configuración centralizada.    |
| **RF-707** | Permanecer independiente del LLM.         |


No será responsable de:

- recuperar documentos;
- generar embeddings;
- consultar el Vector Store;
- invocar Gemini;
- construir prompts;
- generar respuestas;
- tomar decisiones de negocio.

Esto garantiza el cumplimiento del principio de Responsabilidad Única (SRP).
---

# 8. Arquitectura del módulo

```text
context_builder/

        ├── interfaces.py

        ├── simple_context_builder.py

        ├── context_builder_factory.py

        └── __init__.py
```

| Archivo                      | Responsabilidad                                               |
| ---------------------------- | ------------------------------------------------------------- |
| `interfaces.py`              | Define el contrato público del módulo.                        |
| `simple_context_builder.py`  | Implementa la estrategia básica de construcción del contexto. |
| `context_builder_factory.py` | Ensambla la implementación concreta del Context Builder.      |
| `__init__.py`                | Expone públicamente el paquete.                               |

## Patrón arquitectónico
El módulo adopta la arquitectura estándar del proyecto:

                ContextBuilderInterface
                           ▲
                           │
               SimpleContextBuilder
                           ▲
                           │
              ContextBuilderFactory

Esta estructura permite incorporar nuevas estrategias de construcción de contexto sin modificar los módulos consumidores.

# 9. Flujo de procesamiento

```text
Retriever
        │
        ▼
list[Document]
        │
        ▼
Validación
        │
        ▼
Aplicación de configuración
        │
        ▼
Construcción del contexto
        │
        ▼
Contexto consolidado (str)
        │
        ▼
Decision Engine
```

Durante este proceso:

- Se recibe la colección de documentos.
- Se verifica la existencia de contenido útil.
- Se preserva el orden original.
- Se construye el contexto textual.
- Se devuelve un único bloque de texto.

---

# 10. Modelo de datos

## Entrada
| Campo       | Tipo             | Descripción                                           |
| ----------- | ---------------- | ----------------------------------------------------- |
| `documents` | `list[Document]` | Colección de documentos recuperados por el Retriever. |

Cada objeto Document deberá conservar:

- page_content
- metadata

## Salida
| Campo     | Tipo  | Descripción                   |
| --------- | ----- | ----------------------------- |
| `context` | `str` | Contexto textual consolidado. |

El Context Builder no modifica los documentos originales; únicamente genera una representación textual

---

# 11. Diseño de clases

                ContextBuilderInterface
                           ▲
                           │
               SimpleContextBuilder
                           ▲
                           │
              ContextBuilderFactory

- ContextBuilderInterface : Define el contrato público del módulo.

- ContextBuilderInterface : Define el contrato público del módulo.

- ContextBuilderFactory : Centraliza la creación de implementaciones concretas, facilitando futuras extensiones.

---

# 12. Interfaces públicas

La API pública del módulo queda definida por el siguiente contrato:

```python
build_context(
    documents: list[Document],
) -> str
```

## Parámetros

| Parámetro   | Tipo             | Descripción                              |
| ----------- | ---------------- | ---------------------------------------- |
| `documents` | `list[Document]` | Documentos recuperados por el Retriever. |

## Retorna
str

---

# 13 Interfaces privadas

La primera implementación del módulo (SimpleContextBuilder) no expone interfaces privadas.

Toda la funcionalidad se concentra en un único método público:

```python
build_context(
    documents: list[Document],
) -> str
```
Las futuras implementaciones podrán incorporar métodos privados para optimizar el proceso de construcción del contexto, tales como:

-  _filter_documents()
- _format_document()
- _truncate_context()
- _append_metadata()

Estos métodos deberán permanecer encapsulados dentro de la implementación concreta y no formarán parte del contrato público del módulo.

---

# 14. Reglas de validación

El Context Builder deberá aplicar las siguientes validaciones antes de construir el contexto:

| ID     | Regla                                                                  |
| ------ | ---------------------------------------------------------------------- |
| RV-701 | La colección de documentos puede estar vacía.                          |
| RV-702 | Los documentos con contenido vacío deberán ignorarse.                  |
| RV-703 | El orden recibido del Retriever no podrá modificarse.                  |
| RV-704 | La construcción deberá utilizar la configuración oficial del proyecto. |
| RV-705 | No deberán modificarse los objetos `Document` originales.              |
| RV-706 | El resultado siempre será una cadena de texto (`str`).                 |

Estas validaciones garantizan que el módulo permanezca desacoplado y predecible.

---

# 15. Configuración del módulo

Toda la configuración del Context Builder se centraliza en:

src/config/settings.py

Parámetros previstos:

| Parámetro           | Descripción                                                                      |
| ------------------- | -------------------------------------------------------------------------------- |
| `CONTEXT_SEPARATOR` | Separador utilizado entre documentos del contexto.                               |
| `MAX_CONTEXT_CHARS` | Longitud máxima permitida para el contexto consolidado.                          |
| `INCLUDE_METADATA`  | Indica si deben incorporarse los metadatos durante la construcción del contexto. |

Principios
- No utilizar valores hardcodeados.
- Mantener una única fuente de configuración.
- Facilitar cambios sin modificar el código del Provider.
- Permitir configuraciones específicas para distintos proveedores LLM.

---

# 16. Manejo de errores
El Context Builder deberá gestionar de forma controlada las siguientes situaciones:

- colección vacía;
- documentos sin contenido;
- configuración inválida;
- contexto resultante vacío.

No deberá propagar excepciones de bajo nivel relacionadas con implementaciones concretas.

La gestión de errores propios del modelo LLM será responsabilidad del Decision Engine.

---

# 17. Logging

El módulo deberá registrar, como mínimo, los siguientes eventos:

- inicio del proceso de construcción;
- cantidad de documentos recibidos;
- cantidad de documentos utilizados;
- longitud final del contexto generado;
- aplicación de la configuración;
- errores de validación.

El objetivo del registro es facilitar la trazabilidad y el diagnóstico durante el desarrollo y la operación del sistema.

---

# 18. Consideraciones de rendimiento
El diseño del Context Builder seguirá las siguientes directrices:

- preservar una complejidad temporal aproximada de O(n);
- evitar copias innecesarias de documentos;
- minimizar el consumo de memoria;
- construir el contexto mediante operaciones eficientes de concatenación;
- prepararse para futuras estrategias de optimización.

En versiones posteriores podrán incorporarse técnicas como:

- truncamiento inteligente;
- ventanas deslizantes (Sliding Window);
- compresión de contexto;
- selección jerárquica de documentos.

Estas mejoras no requerirán modificaciones en los módulos consumidores gracias al uso de interfaces y Factory Pattern.

---

# 19. Extensibilidad
El diseño del Context Builder permite incorporar nuevas estrategias de construcción sin modificar el resto del pipeline RAG.

Ejemplos previstos:
ContextBuilderInterface
        │
        ├── SimpleContextBuilder
        ├── SlidingWindowContextBuilder
        ├── CompressedContextBuilder
        ├── HierarchicalContextBuilder
        └── MapReduceContextBuilder

Cada implementación deberá cumplir el contrato definido por ContextBuilderInterface.

La selección de la estrategia concreta será responsabilidad de ContextBuilderFactory, manteniendo el principio Open/Closed (OCP) y evitando modificaciones en los módulos consumidores.

---

# 20. Casos de Prueba

La validación del módulo **Context Builder** se realizará mediante pruebas automatizadas utilizando **pytest**.

Cada caso de prueba mantiene trazabilidad con los requisitos funcionales definidos para el módulo.


| Caso       | Objetivo                                                       | Requisito asociado |
| ---------- | -------------------------------------------------------------- | ------------------ |
| **CP-040** | Validar la creación de `ContextBuilderInterface`.              | RF-701             |
| **CP-041** | Validar la construcción del contexto con un documento.         | RF-702             |
| **CP-042** | Validar la construcción del contexto con múltiples documentos. | RF-702             |
| **CP-043** | Verificar la preservación del orden recibido del Retriever.    | RF-703             |
| **CP-044** | Ignorar documentos con contenido vacío.                        | RF-702             |
| **CP-045** | Validar `ContextBuilderFactory`.                               | RF-706             |


## Resultado obtenido 

Al finalizar el Sprint deberán obtenerse los siguientes resultados:

- 25 pruebas ejecutadas.
- 25 exitosas.
- 0 fallidas.
- Cobertura funcional: 100%

## Validación de integración

La validación funcional deberá realizarse mediante:

- pruebas unitarias con pytest;
- validación manual del Context Builder utilizando documentos recuperados por el Retriever;
- revisión arquitectónica para verificar el cumplimiento de los principios de desacoplamiento.

---

## Cobertura de pruebas

Cada requisito funcional deberá encontrarse cubierto por al menos un caso de prueba automatizado.

La relación definitiva será registrada en la Matriz de Trazabilidad (MTR-001).
---

## Herramienta de pruebas

Las **pruebas automatizadas** del proyecto continúan implementándose mediante:

- pytest

La estructura oficial permanece sin cambios:

- temp/

Pruebas de integración y validaciones manuales.

- tests/

Pruebas automatizadas.

```bash
python -m pytest
python -m pytest tests
python -m pytest tests/test_context_builder.py
```

---

# 21. Trazabilidad

| Artefacto      | Relación                           |
| -------------- | ---------------------------------- |
| PLAN-007       | Planificación del Sprint           |
| SDS-007        | Diseño técnico del Context Builder |
| IMP-01         | Estructura del módulo              |
| IMP-02         | ContextBuilderInterface            |
| IMP-03         | SimpleContextBuilder               |
| IMP-04         | ContextBuilderFactory              |
| IMP-05         | Configuración centralizada         |
| IMP-06         | Pruebas unitarias                  |
| TST-02         | Validación funcional               |
| MTR-001        | Actualización de trazabilidad      |
| Release v0.7.0 | Entrega del Sprint                 |


---

# 22. Riesgos identificados

| Riesgo                                     | Mitigación                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------------- |
| Crecimiento excesivo del contexto          | Configuración mediante `MAX_CONTEXT_CHARS`.                                     |
| Acoplamiento con el modelo LLM             | El Context Builder finaliza su responsabilidad antes del Decision Engine.       |
| Cambios en las estrategias de construcción | Uso de `ContextBuilderInterface` y `ContextBuilderFactory`.                     |
| Cambios en LangChain                       | Encapsular la lógica utilizando únicamente `Document` como contrato de entrada. |
| Evolución del pipeline RAG                 | Mantener desacoplamiento mediante interfaces y configuración centralizada.      |


---

# 23. Estado de implementación

| Implementación                    | Estado |
| --------------------------------- | :----: |
| IMP-01 Arquitectura del módulo    |    ✅   |
| IMP-02 `ContextBuilderInterface`  |    ✅   |
| IMP-03 `SimpleContextBuilder`     |    ✅   |
| IMP-04 `ContextBuilderFactory`    |    ✅   |
| IMP-05 Configuración centralizada |    ✅   |
| IMP-06 Pruebas unitarias          |    ✅   |

---

# 24. Resultados de implementación

- ContextBuilderInterface      ✓ Implementada
- SimpleContextBuilder         ✓ Implementado
- ContextBuilderFactory        ✓ Implementada
- Configuración                ✓ Centralizada
- Pruebas automatizadas        ✓ 25/25
- Cobertura funcional          ✓ 100 %
- Arquitectura desacoplada     ✓ Validada

Resultado esperado
- Interfaces implementadas.
- Provider desacoplado.
- Factory funcional.
- Configuración centralizada.
- Compatibilidad completa con el Sprint 8.
- Context Builder listo para integrarse con el Decision Engine.

---

# 25. Registro de Decisiones Arquitectónicas (ADR Resumido) ✅ (Nueva sección)

| ID             | Decisión                                    | Justificación                                                                              |
| -------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **ADR-007-01** | Uso de `ContextBuilderInterface`            | Permite desacoplar la implementación concreta del consumidor.                              |
| **ADR-007-02** | El Context Builder no invoca el LLM         | Mantiene el principio de Responsabilidad Única (SRP).                                      |
| **ADR-007-03** | Preservar el orden recibido del Retriever   | La relevancia calculada por el Retriever no debe alterarse.                                |
| **ADR-007-04** | Configuración centralizada en `settings.py` | Evita valores hardcodeados y simplifica el mantenimiento.                                  |
| **ADR-007-05** | Uso de `ContextBuilderFactory`              | Facilita incorporar nuevas estrategias de construcción sin modificar el resto del sistema. |


## Decisiones consolidadas del proyecto
A partir del Sprint 9, las siguientes decisiones se consideran estándares permanentes de Mercado Central AI:

| Estándar                             | Aplicación                                                   |
| ------------------------------------ | ------------------------------------------------------------ |
| Arquitectura basada en interfaces    | Todos los módulos del pipeline.                              |
| Factory Pattern                      | Ensamblado de dependencias.                                  |
| Configuración centralizada           | `src/config/settings.py`.                                    |
| Imports absolutos entre paquetes     | `from src...`.                                               |
| Imports relativos dentro del paquete | `from .interfaces import ...`.                               |
| Validación incremental               | Antes de modificar módulos cerrados.                         |
| Eliminación de *magic numbers*       | Toda constante configurable debe residir en `settings.py`.   |
| Compatibilidad hacia atrás           | Ningún Sprint cerrado debe romperse sin análisis de impacto. |


# 26. Contrato de la Interfaz (API Contract) ✅ (Nueva sección)

## Entrada
- documents: list[Document]

Cada documento deberá contener:

- page_content
- metadata

## Precondiciones
- La colección puede estar vacía.
- Los objetos Document deberán ser válidos.
- La configuración del módulo deberá estar disponible.
- El orden recibido deberá preservarse.

## Salida
str

## Postcondiciones

- Se preserva el orden de relevancia.
- No se modifican los documentos originales.
- Se construye un único contexto textual.
- Se aplica la configuración centralizada.
- El resultado queda listo para ser consumido por el Decision Engine.

## Excepciones previstas

- Configuración inválida.
- Contexto vacío.
- Documentos sin contenido útil.

Las excepciones relacionadas con el modelo de lenguaje quedan fuera del alcance del Context Builder.

# 27. Control de versiones

| Versión | Cambios                                                                                                                              |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **1.0** | Creación del SDS-007 y definición del diseño del Context Builder.                                                                    |
| **1.1** | Implementación completa del Context Builder, incorporación de pruebas unitarias, ADR, contrato de la interfaz y cierre del Sprint 9. |








