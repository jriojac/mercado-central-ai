# SDS-009
# Software Design Specification
## Módulo: Tools
## Versión: 1.0
## Release objetivo: v0.9.0


---

# 1. Información del documento

| Campo                | Valor                                           |
| -------------------- | ----------------------------------------------- |
| Documento            | SDS-009                                         |
| Título               | Software Design Specification – Tools           |
| Versión              | 1.0                                             |
| Estado               | Finalizado                                      |
| Sprint               | 11                                              |
| Hito                 | 9                                               |
| Módulo               | Tools                                           |
| Release objetivo     | v0.9.0                                          |
| Dependencia          | Decision Engine (Sprint 10)                     |
| Autor                | Jacqueline Rioja                                |
| Fecha                | 11/07/2026                                      |
| Última actualización | 11/07/2026                   |


---

# 2. Objetivo

El objetivo de este documento es definir el diseño técnico del módulo Tools, responsable de administrar las herramientas disponibles para el sistema, permitiendo registrar, localizar y ejecutar herramientas especializadas sin acoplar el Decision Engine a implementaciones concretas.

El diseño mantiene los principios arquitectónicos consolidados del proyecto Mercado Central AI:

- Responsabilidad Única (SRP).
- Bajo acoplamiento.
- Alta cohesión.
- Arquitectura basada en interfaces.
- Factory Pattern.
- Configuración centralizada.
- Compatibilidad con el pipeline RAG.
- Extensibilidad mediante herramientas especializadas.

---

# 3. Alcance

## Incluye

El módulo deberá permitir:

- Definir ToolInterface.
- Definir ToolManagerInterface.
- Implementar ToolManager.
- Implementar ToolFactory.
- Registrar herramientas.
- Ejecutar herramientas.
- Detectar registros duplicados.
- Preparar la infraestructura para futuras herramientas.

## No incluye

- Implementación de FAQ Tool.
- Implementación de Inventory Tool.
- Implementación de Policy Tool.
- Integración con Gemini.
- Integración con Streamlit.
- Generación de respuestas.
- Ejecución automática desde el Decision Engine.

---

# 4. Referencias

Documentos relacionados:

- PLAN-009
- SDS-009
- MTR-001
- README
- HANDBOOK
- ROADMAP
- CHANGELOG
- LOG

---

# 5. Contexto dentro del Pipeline RAG

El módulo Tools representa la infraestructura encargada de administrar herramientas especializadas que podrán ser utilizadas por el Decision Engine durante futuras versiones del sistema.

Su responsabilidad consiste en registrar herramientas, identificar cuál puede atender una consulta determinada y ejecutar únicamente la herramienta seleccionada.

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
Tool

```

## Entrada

| Campo   | Tipo |
| ------- | ---- |
| query   | str  |

## Procesamiento
 
Durante el procesamiento el módulo:

- Rrecibe la consulta del usuario;
- identifica la herramienta adecuada;
- ejecuta la herramienta correspondiente;
- devuelve el resultado obtenido.

## Salida

| Campo    | Tipo       |
| -------  | ---------- |
| response | str | None |

---

# 6. Requerimientos funcionales

| ID     | Descripción                                 |
| ------ | ------------------------------------------- |
| RF-901 | Definir `ToolInterface`.                    |
| RF-902 | Definir `ToolManagerInterface`.             |
| RF-903 | Implementar `ToolManager`.                  |
| RF-904 | Implementar `ToolFactory`.                  |
| RF-905 | Registrar herramientas.                     |
| RF-906 | Ejecutar herramientas registradas.          |
| RF-907 | Detectar registros duplicados.              |
| RF-908 | Mantener independencia del Decision Engine. |

---

# 7. Responsabilidades del módulo

Su flujo funcional puede representarse de la siguiente manera:

query
   │
   ▼
ToolManager
   │
   ▼
Tool
   │
   ▼
response

El módulo sí será responsable de:

- administrar herramientas;
- registrar herramientas;
- localizar herramientas;
- ejecutar herramientas.

No será responsable de:

- consultar ChromaDB;
- recuperar documentos;
- construir contexto;
- invocar Gemini;
- generar respuestas finales;
- administrar conversaciones.

Esto garantiza el cumplimiento del principio de Responsabilidad Única (SRP).
---

# 8. Arquitectura del módulo

```text
tools/
      ├── interfaces.py
      ├── tool_manager.py
      ├── tool_factory.py
      └── providers/
```

## Patrón arquitectónico
El módulo adopta la arquitectura estándar del proyecto:

ToolManagerInterface
          ▲
          │
     ToolManager
          ▲
          │
     ToolFactory

ToolInterface
        ▲
        │
     Future Tools

Esta estructura permite incorporar nuevas estrategias de construcción de contexto sin modificar los módulos consumidores.

# 9. Flujo de procesamiento

```text
Usuario
      │
      ▼
Consulta
      │
      ▼
Decision Engine
      │
      ▼
ToolManager
      │
      ▼
Tool
      │
      ▼
Resultado
```

Durante este proceso:

- se recibe la consulta del usuario;
- el ToolManager identifica la herramienta adecuada;
- la herramienta procesa la consulta;
- el resultado se devuelve al módulo consumidor.

---

# 10. Modelo de datos

En la versión v0.9.0, el módulo Tools no define modelos de datos propios.

La interacción entre el consumidor (DecisionEngine) y el módulo se realiza mediante tipos primitivos (str) para mantener una implementación simple.

La incorporación de modelos específicos será evaluada en futuras versiones cuando exista una necesidad funcional.

## Entrada

| Campo | Tipo | Descripción                                               |
| ----- | ---- | --------------------------------------------------------- |
| query | str  | Consulta recibida para ser evaluada por las herramientas. |

## Salida

| Campo    | Tipo       | Descripción                                                                                                       |
| -------- | ---------- | ----------------------------------------------------------------------------------------------------------------- |
| response | str | None | Resultado devuelto por la herramienta seleccionada o `None` cuando ninguna herramienta pueda atender la consulta. |

---

# 11. Diseño de clases

                 ToolInterface
                       ▲
                       │
              Future Tool Providers
                       │
                       ▼

          ToolManagerInterface
                    ▲
                    │
              ToolManager
                    ▲
                    │
              ToolFactory


- ToolInterface: contrato público que deberán implementar todas las herramientas.
- ToolManagerInterface: contrato del administrador de herramientas.
- ToolManager: administra el registro y ejecución de herramientas.
- ToolFactory: centraliza la creación del ToolManager.

---

# 12. Interfaces públicas

La API pública del módulo queda definida por el siguiente contrato:

## ToolINterface
```python
name

description

can_handle(
    query: str,
) -> bool

execute(
    query: str,
) -> str
```
## ToolManagerInterface
```python
register(
    tool: ToolInterface,
) -> None

execute(
    query: str,
) -> str | None

has_tool(
    name: str,
) -> bool
```

---

# 13 Interfaces privadas

La implementación actual únicamente expone un método privado.

```python
_find(
    query: str,
)
```
Su responsabilidad consiste en localizar internamente la primera herramienta capaz de atender la consulta.

Este método forma parte de la implementación interna del ToolManager y no deberá ser utilizado por componentes externos.
---

# 14. Reglas de validación

| ID     | Regla                                                                                   |
| ------ | --------------------------------------------------------------------------------------- |
| RV-901 | La herramienta registrada debe implementar `ToolInterface`.                             |
| RV-902 | No se permite registrar herramientas duplicadas.                                        |
| RV-903 | La ejecución debe devolver `None` cuando ninguna herramienta pueda atender la consulta. |
| RV-904 | El `ToolManager` no debe conocer implementaciones concretas del `DecisionEngine`.       |
| RV-905 | El `ToolFactory` será el único responsable del ensamblado del módulo.                   |

---

# 15. Configuración del módulo

En la versión v0.9.0, el módulo Tools no requiere parámetros de configuración centralizada.

La incorporación de configuraciones específicas se evaluará cuando existan herramientas que necesiten parámetros propios o integración con servicios externos.
---

# 16. Manejo de errores

El módulo gestiona de forma controlada las siguientes situaciones:

- registro de objetos que no implementan ToolInterface;
- registro duplicado de herramientas;
- consultas sin una herramienta disponible.

- Para ello se definió la excepción: **DuplicateToolError**

- Las excepciones comunes permanecen centralizadas en: **src/core/exceptions.py** 

No se crean excepciones específicas dentro del paquete tools, manteniendo la política de centralización del proyecto.
---

# 17. Logging

En esta versión no se incorpora registro de eventos (logging) específico para el módulo.

Cuando se implementen herramientas concretas, se evaluará registrar eventos como:

- inicio de ejecución de una herramienta;
- herramienta seleccionada;
- herramienta no encontrada;
- errores de ejecución.

---

# 18. Consideraciones de rendimiento

El módulo Tools deberá mantener un comportamiento ligero y determinístico.

Principios:

- complejidad lineal O(n) para la búsqueda de herramientas registradas;
- registro de herramientas con complejidad O(1) mediante diccionario;
- evitar dependencias innecesarias;
- minimizar el acoplamiento con el resto del pipeline;
- mantener el ToolManager como un componente de coordinación, sin lógica de negocio propia.
---

# 19. Extensibilidad

El módulo Tools fue diseñado para permitir la incorporación de nuevas herramientas sin modificar el resto del pipeline RAG.

La arquitectura prevista es la siguiente:

ToolInterface
        │
        ├── FAQTool
        ├── InventoryTool
        ├── PolicyTool
        ├── SupplierTool
        └── FutureTool

Todas las herramientas futuras deberán implementar obligatoriamente ToolInterface.

El registro y ensamblado de las herramientas será responsabilidad exclusiva del ToolFactory, manteniendo el cumplimiento del principio Open/Closed (OCP).
---

# 20. Casos de Prueba

| Caso   | Objetivo                           | Requisito |
| ------ | ---------------------------------- | --------- |
| CP-090 | Validar `ToolInterface`.           | RF-901    |
| CP-091 | Validar `ToolManager`.             | RF-903    |
| CP-092 | Validar `ToolFactory`.             | RF-904    |
| CP-093 | Validar registro duplicado.        | RF-907    |
| CP-094 | Validar ejecución sin herramienta. | RF-906    |


## Resultado obtenido 

Al finalizar el Sprint deberán obtenerse los siguientes resultados:

- 40 pruebas ejecutadas.
- 40 pruebas exitosas.
- 0 pruebas fallidas.
- Cobertura funcional: 100 %.

## Validación de integración

En esta versión únicamente se valida la infraestructura del módulo.

La integración con el DecisionEngine será implementada en un Sprint posterior.

La validación realizada comprende:

- pruebas unitarias mediante pytest;
- revisión arquitectónica;
- validación del cumplimiento de interfaces;
- validación del Factory Pattern;
- verificación del desacoplamiento.

---

## Cobertura de pruebas

Cada requisito funcional definido para este Sprint se encuentra cubierto por al menos un caso de prueba automatizado.

La relación definitiva será registrada en la Matriz de Trazabilidad (MTR-001).
---

## Herramienta de pruebas

Las **pruebas automatizadas** continúan implementándose mediante:**pytest**

La estructura oficial permanece sin cambios:

- temp/

Pruebas de integración y validaciones manuales.

- tests/

Pruebas automatizadas.

```bash
python -m pytest tests/test_tools_interface.py
python -m pytest tests/test_tool_manager.py
python -m pytest tests/test_tool_factory.py
```

---

# 21. Trazabilidad

| Artefacto      | Relación                        |
| -------------- | ------------------------------- |
| PLAN-009       | Planificación del Sprint        |
| SDS-009        | Diseño técnico del módulo Tools |
| IMP-01         | Diseño arquitectónico           |
| IMP-02         | Interfaces                      |
| IMP-03         | ToolManager                     |
| IMP-04         | ToolFactory                     |
| IMP-05         | Validación y documentación      |
| Release v0.9.0 | Entrega del Sprint              |

---

# 22. Riesgos identificados

| Riesgo                               | Mitigación                     |
| ------------------------------------ | ------------------------------ |
| Acoplamiento con el Decision Engine  | Uso de `ToolManagerInterface`. |
| Registro duplicado de herramientas   | `DuplicateToolError`.          |
| Exposición del estado interno        | Uso de `has_tool()`.           |
| Crecimiento del módulo               | Uso de `ToolFactory`.          |
| Incorporación de nuevas herramientas | Uso de `ToolInterface`.        |

---

# 23. Estado de implementación

| Implementación      | Estado |
| ------------------- | :----: |
| IMP-01 Arquitectura |    ✅   |
| IMP-02 Interfaces   |    ✅   |
| IMP-03 ToolManager  |    ✅   |
| IMP-04 ToolFactory  |    ✅   |
| IMP-05 Validación   |    ✅   |

---

# 24. Resultados de implementación

Durante el Sprint se implementó satisfactoriamente la infraestructura base del módulo Tools.

Resultados obtenidos:

- ToolInterface implementada.
- ToolManagerInterface implementada.
- ToolManager implementado.
- ToolFactory implementada.
- DuplicateToolError incorporada.
- DummyTool para pruebas.
- 40/40 pruebas exitosas.
- Arquitectura desacoplada validada.
- Release v0.9.0 preparada.

---

# 25. Registro de Decisiones Arquitectónicas (ADR Resumido) ✅ (Nueva sección)

| ADR        | Decisión                                                 | Justificación                                                                                                                               |
| ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| ADR-009-01 | Uso de `ToolInterface`.                                  | Define un contrato estable para todas las herramientas.                                                                                     |
| ADR-009-02 | Uso de `ToolManagerInterface`.                           | Desacopla el consumidor de la implementación concreta.                                                                                      |
| ADR-009-03 | Uso de `ToolFactory`.                                    | Centraliza el ensamblado de dependencias.                                                                                                   |
| ADR-009-04 | Uso de `DuplicateToolError`.                             | Detecta errores de configuración durante el registro.                                                                                       |
| ADR-009-05 | No incorporar `ToolRequest` ni `ToolResponse` en v0.9.0. | Se aplica el principio **YAGNI**. El intercambio mediante `str` es suficiente en esta versión.                                              |
| ADR-009-06 | Incorporar `has_tool()` en `ToolManager`.                | Evita acceder al atributo privado `_tools`, preservando el encapsulamiento y permitiendo que las pruebas validen únicamente la API pública. |



## Decisiones consolidadas del proyecto
A partir del Sprint 11, las siguientes decisiones se consideran estándares permanentes de Mercado Central AI:

| Estándar                             | Aplicación                                                                                                        |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Arquitectura basada en interfaces    | Todos los módulos del pipeline.                                                                                   |
| Factory Pattern                      | Ensamblado de dependencias.                                                                                       |
| Configuración centralizada           | `src/config/settings.py`.                                                                                         |
| Imports absolutos entre paquetes     | `from src...`.                                                                                                    |
| Imports relativos dentro del paquete | `from .interfaces import ...`.                                                                                    |
| Validación incremental               | Antes de modificar módulos cerrados.                                                                              |
| Eliminación de valores hardcodeados  | Toda constante configurable reside en `settings.py`.                                                              |
| Compatibilidad hacia atrás           | Ningún Sprint cerrado se modifica sin análisis de impacto.                                                        |
| Documentación por Sprint/Hito        | Cada Sprint genera su propio PLAN, SDS, MTR y Acta de Cierre, preservando la trazabilidad histórica del proyecto. |


# 26. Contrato de la Interfaz (API Contract) ✅ (Nueva sección)

## Entrada
query

context

## Precondiciones
- El ToolManager debe encontrarse correctamente inicializado.
- La herramienta debe implementar ToolInterface.
- La consulta debe recibirse como una cadena (str).

## Salida
response

## Postcondiciones

- Se ejecuta la primera herramienta capaz de atender la consulta.
- Si ninguna herramienta puede procesarla, se devuelve None.
- El estado interno del ToolManager permanece consistente.

## Excepciones previstas

- Registro de un objeto que no implemente ToolInterface.
- Registro duplicado de herramientas (DuplicateToolError).
- Parámetros inválidos (TypeError).

# 27. Control de versiones

| Versión | Cambios                                                                                                                                                                                                               |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Creación del SDS-009 y diseño arquitectónico del módulo **Tools**.                                                                                                                                                    |
| 1.1     | Implementación completa de `ToolInterface`, `ToolManagerInterface`, `ToolManager`, `ToolFactory`, incorporación de `DuplicateToolError`, validación con **40 pruebas exitosas**, registro ADR y cierre del Sprint 11. |









