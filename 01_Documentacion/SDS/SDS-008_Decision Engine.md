# SDS-008
# Software Design Specification
## Módulo: Decision Engine
## Versión: 1.0
## Release objetivo: v0.8.0


---

# 1. Información del documento

| Campo                | Valor                                           |
| -------------------- | ----------------------------------------------- |
| Documento            | SDS-008                                         |
| Título               | Software Design Specification – Decision Engine |
| Versión              | 1.0                                             |
| Estado               | Finalizado                                      |
| Sprint               | 10                                              |
| Hito                 | 8                                               |
| Módulo               | Decision Engine                                 |
| Release objetivo     | v0.8.0                                          |
| Dependencia          | Context Builder (Sprint 9)                      |
| Autor                | Jacqueline Rioja                                |
| Fecha                | 10/07/2026                                      |
| Última actualización | 10/07/2026                   |


---

# 2. Objetivo

El objetivo de este documento es definir el diseño técnico del módulo Decision Engine, responsable de construir una solicitud (LLMRequest) a partir de la consulta del usuario y del contexto generado por el Context Builder, manteniendo independencia respecto al proveedor LLM y preparando la arquitectura para soportar múltiples proveedores de modelos de lenguaje.

El diseño mantiene los principios consolidados del proyecto Mercado Central AI:

- Responsabilidad Única (SRP).
- Bajo acoplamiento.
- Alta cohesión.
- Arquitectura basada en interfaces.
- Factory Pattern.
- Configuración centralizada.
- Compatibilidad con el pipeline RAG.
- Independencia del proveedor LLM.

---

# 3. Alcance

## Incluye

El módulo deberá permitir:

- Definición de DecisionEngineInterface.
- Implementación de LLMRequest.
- Implementación de DecisionEngine.
- Implementación de DecisionEngineFactory.
- Construcción de solicitudes independientes del proveedor LLM.
- Preparación para múltiples proveedores LLM.

## No incluye

- LLM Provider.
- Gemini.
- Prompt Builder.
- Tools.
- Streamlit.
- Generación de respuestas.

---

# 4. Referencias

Documentos relacionados:

- PLAN-008
- SDS-008
- MTR-001
- README
- HANDBOOK
- ROADMAP
- CHANGELOG
- LOG

---

# 5. Contexto dentro del Pipeline RAG

El Decision Engine representa la transición entre la construcción del contexto y el proveedor LLM.

Su responsabilidad consiste en recibir la consulta del usuario y el contexto generado por el Context Builder para construir una instancia de LLMRequest, que será consumida posteriormente por un proveedor LLM.

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

```

## Entrada

| Campo   | Tipo |
| ------- | ---- |
| query   | str  |
| context | str  |


## Procesamiento
 
Durante el procesamiento el módulo:

- Recibe la consulta del usuario.
- Recibe el contexto generado por el Context Builder.
- Construye una instancia de LLMRequest.
- Devuelve la solicitud preparada para el proveedor LLM.


## Salida

| Campo   | Tipo       |
| ------- | ---------- |
| request | LLMRequest |



---

# 6. Requerimientos funcionales

| ID     | Descripción                               |
| ------ | ----------------------------------------- |
| RF-801 | Definir `DecisionEngineInterface`.        |
| RF-802 | Construir un `LLMRequest`.                |
| RF-803 | Recibir `query` y `context`.              |
| RF-804 | Mantener independencia del proveedor LLM. |
| RF-805 | Implementar `DecisionEngine`.             |
| RF-806 | Implementar `DecisionEngineFactory`.      |


---

# 7. Responsabilidades del módulo

Su flujo funcional puede representarse de la siguiente manera:

query

+

context

↓

LLMRequest


No será responsable de:

- invocar Gemini;
- ejecutar prompts;
- recuperar documentos;
- generar respuestas;
- ejecutar herramientas (Tools);
- administrar conversaciones.

## Responsabilidad

| ID     | Descripción                               |
| ------ | ----------------------------------------- |
| RF-801 | Definir `DecisionEngineInterface`.        |
| RF-802 | Construir un `LLMRequest`.                |
| RF-803 | Recibir `query` y `context`.              |
| RF-804 | Mantener independencia del proveedor LLM. |
| RF-805 | Implementar `DecisionEngine`.             |
| RF-806 | Implementar `DecisionEngineFactory`.      |

Esto garantiza el cumplimiento del principio de Responsabilidad Única (SRP).
---

# 8. Arquitectura del módulo

```text
llm/

        ├── interfaces.py

        ├── models.py

        ├── decision_engine.py

        └── decision_engine_factory.py
```

## Patrón arquitectónico
El módulo adopta la arquitectura estándar del proyecto:

DecisionEngineInterface
          ▲
          │
    DecisionEngine
          ▲
          │
DecisionEngineFactory


DecisionEngine

↓

LLMRequest

Esta estructura permite incorporar nuevas estrategias de construcción de contexto sin modificar los módulos consumidores.

# 9. Flujo de procesamiento

```text
Usuario
      │
      ▼
Query
      │
      ▼
Context Builder
      │
      ▼
Contexto
      │
      ▼
Decision Engine
      │
      ▼
LLMRequest
```

Durante este proceso:

- Se recibe la consulta del usuario.
- Se recibe el contexto generado por el Context Builder.
- Se construye una instancia de LLMRequest.
- Se prepara la solicitud para el proveedor LLM.
- Se devuelve el objeto LLMRequest.

---

# 10. Modelo de datos

| Campo         | Tipo        | Descripción                               |
| ------------- | ----------- | ----------------------------------------- |
| query         | str         | Consulta original del usuario.            |
| context       | str         | Contexto generado por el Context Builder. |
| system_prompt | str | None  | Prompt del sistema.                       |
| metadata      | dict | None | Información adicional.                    |


## Entrada

## Salida

---

# 11. Diseño de clases

DecisionEngineInterface
          ▲
          │
    DecisionEngine
          │
          ▼
      LLMRequest

DecisionEngineFactory
          │
          ▼
    DecisionEngine


- DecisionEngineInterface: define el contrato público.
- DecisionEngine: implementa la lógica de construcción del LLMRequest.
- DecisionEngineFactory: centraliza la creación de la implementación.
- LLMRequest: representa la solicitud preparada para el proveedor LLM.

---

# 12. Interfaces públicas

La API pública del módulo queda definida por el siguiente contrato:

```python
build_request(
    query: str,
    context: str,
) -> LLMRequest
```

## Parámetros

| Parámetro | Tipo | Descripción                               |
| --------- | ---- | ----------------------------------------- |
| query     | str  | Consulta del usuario.                     |
| context   | str  | Contexto generado por el Context Builder. |

## Retorna
LLMRequest

---

# 13 Interfaces privadas

La primera implementación del DecisionEngine no expone interfaces privadas.

Toda la funcionalidad se concentra en build_request().

Futuras implementaciones podrán incorporar métodos privados como:

- _build_system_prompt()
- _build_metadata()
- _validate_request()
---

# 14. Reglas de validación

| ID     | Regla                                       |
| ------ | ------------------------------------------- |
| RV-801 | `query` no debe ser nula.                   |
| RV-802 | `context` debe recibirse como cadena.       |
| RV-803 | Debe construirse un `LLMRequest`.           |
| RV-804 | El módulo no debe conocer el proveedor LLM. |


---

# 15. Configuración del módulo

En la versión v0.8.0 el Decision Engine no requiere parámetros de configuración centralizada. La incorporación de configuraciones específicas se evaluará en futuras versiones cuando se integren proveedores LLM.

---

# 16. Manejo de errores

El Decision Engine deberá gestionar de forma controlada las siguientes situaciones:

- consulta vacía;
- contexto vacío;
- parámetros inválidos;
- construcción incompleta del LLMRequest.

No deberá gestionar errores propios del proveedor LLM.

Las excepciones relacionadas con Gemini u otros proveedores serán responsabilidad del módulo LLM Provider.
---

# 17. Logging

El módulo deberá registrar, como mínimo, los siguientes eventos:

- inicio de construcción de la solicitud;
- consulta recibida;
- longitud del contexto;
- creación de LLMRequest;
- errores de validación.

El objetivo del registro es facilitar la trazabilidad y el diagnóstico durante el desarrollo y la operación del sistema.

---

# 18. Consideraciones de rendimiento

El Decision Engine deberá mantener un procesamiento ligero y predecible.

Principios:

- complejidad temporal O(1);
- evitar copias innecesarias del contexto;
- minimizar el consumo de memoria;
- limitarse a construir el objeto LLMRequest;
- no realizar procesamiento propio del proveedor LLM.
---

# 19. Extensibilidad

Ejemplos previstos:
DecisionEngineInterface
        │
        ├── DecisionEngine
        ├── AdvancedDecisionEngine
        ├── PromptAwareDecisionEngine
        └── CustomDecisionEngine

Todas las implementaciones futuras deberán cumplir el contrato definido por DecisionEngineInterface.

La selección de la implementación concreta será responsabilidad de DecisionEngineFactory, manteniendo el principio Open/Closed (OCP).
---

# 20. Casos de Prueba

| Caso   | Objetivo                         | Requisito |
| ------ | -------------------------------- | --------- |
| CP-050 | Validar `LLMRequest`.            | RF-802    |
| CP-051 | Validar `DecisionEngine`.        | RF-805    |
| CP-052 | Validar `DecisionEngineFactory`. | RF-806    |


## Resultado obtenido 

Al finalizar el Sprint deberán obtenerse los siguientes resultados:

- 29 pruebas ejecutadas.
- 29 exitosas.
- 0 fallidas.
- Cobertura funcional: 100%

## Validación de integración

La validación del flujo: deberá realizarse mediante:

validación manual del flujo:

Context Builder
        │
        ▼
Decision Engine
        │
        ▼
LLMRequest

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
python -m pytest tests/test_models.py
python -m pytest tests/test_decision_engine.py
python -m pytest tests/test_decision_engine_factory.py
```

---

# 21. Trazabilidad

| Artefacto      | Relación                           |
| -------------- | ---------------------------------- |
| PLAN-008       | Planificación del Sprint           |
| SDS-008        | Diseño técnico del Decision Engine |
| IMP-01         | Arquitectura del módulo            |
| IMP-02         | Modelo `LLMRequest`                |
| IMP-03         | `DecisionEngine`                   |
| IMP-04         | `DecisionEngineFactory`            |
| IMP-05         | Validación y documentación         |
| Release v0.8.0 | Entrega del Sprint                 |



---

# 22. Riesgos identificados

| Riesgo                            | Mitigación                                               |
| --------------------------------- | -------------------------------------------------------- |
| Acoplamiento con el proveedor LLM | Mantener independencia mediante `LLMRequest`.            |
| Evolución del contrato            | Utilizar `DecisionEngineInterface`.                      |
| Cambios de proveedor              | Encapsular la creación mediante `DecisionEngineFactory`. |
| Integración futura                | Mantener contratos públicos estables.                    |



---

# 23. Estado de implementación

| Implementación                 | Estado |
| ------------------------------ | :----: |
| IMP-01 Arquitectura            |    ✅   |
| IMP-02 `LLMRequest`            |    ✅   |
| IMP-03 `DecisionEngine`        |    ✅   |
| IMP-04 `DecisionEngineFactory` |    ✅   |
| IMP-05 Validación              |    ✅   |

---

# 24. Resultados de implementación

- LLMRequest implementado.
- DecisionEngine implementado.
- DecisionEngineFactory implementada.
- 29/29 pruebas exitosas.
- Arquitectura desacoplada validada.
- Release v0.8.0 preparada.

---

# 25. Registro de Decisiones Arquitectónicas (ADR Resumido) ✅ (Nueva sección)

| ADR        | Decisión                          | Justificación                                   |
| ---------- | --------------------------------- | ----------------------------------------------- |
| ADR-008-01 | Uso de `LLMRequest`.              | Desacopla el Decision Engine del proveedor LLM. |
| ADR-008-02 | Uso de `DecisionEngineInterface`. | Facilita futuras implementaciones.              |
| ADR-008-03 | Uso de `DecisionEngineFactory`.   | Centraliza la creación de dependencias.         |
| ADR-008-04 | Independencia del proveedor LLM.  | Cumple SRP y DIP.                               |



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
query

context

## Precondiciones
- query válida.
- context generado por el Context Builder.
- DecisionEngine disponible.

## Salida
LLMRequest

## Postcondiciones

- Se genera un LLMRequest.
- No se modifica el contexto recibido.
- La solicitud queda preparada para el proveedor LLM.

## Excepciones previstas

- Query inválida.
- Contexto inválido.
- Error durante la construcción del LLMRequest.

# 27. Control de versiones

| Versión | Cambios                                                       |
| ------- | ------------------------------------------------------------- |
| 1.0     | Creación del SDS-008 y diseño del Decision Engine.            |
| 1.1     | Implementación completa, pruebas, ADR y cierre del Sprint 10. |









