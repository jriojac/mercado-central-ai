# HANDBOOK-001 – Guía de Desarrollo

**Código:** HANDBOOK-001

**Versión:** 2.5

**Estado:** Activo

**Proyecto:** Mercado Central AI

---

# 1. Objetivo

Definir la metodología oficial de desarrollo del proyecto **Mercado Central AI**, estableciendo las reglas, convenciones y buenas prácticas que deberán seguirse durante todo el ciclo de vida del software.

El HANDBOOK constituye la guía principal para el desarrollo del proyecto y complementa la información registrada en el ROADMAP, la MTR, el LOG y los documentos SDS.

---

# 2. Alcance

Este documento aplica a todas las actividades relacionadas con:

- desarrollo del software;
- documentación;
- pruebas;
- gestión del repositorio Git;
- control de versiones;
- incorporación de nuevos módulos.

Toda nueva funcionalidad deberá desarrollarse siguiendo las reglas definidas en este documento.

---

# 3. Metodología oficial del proyecto

Durante la Auditoría Arquitectónica (DOC-014) se aprobó la siguiente metodología como estándar del proyecto.

## Ciclo de planificación

```text
Sprint
      ↓
Hito
      ↓
Release
```

## Definiciones

### Sprint

Período de trabajo donde se desarrolla un módulo funcional.

### Hito

Resultado funcional obtenido durante un Sprint.

Cada Hito debe producir un incremento funcional del sistema.

### Release

Versión publicada del proyecto que incorpora el Hito desarrollado.

Cada Release representa un estado estable y validado del sistema.

---

## Relación Sprint – Hito – Release

| Sprint | Hito | Release |
|--------|------|---------|
| Sprint 3 | Hito 1 – Document Loader | v0.1.1 |
| Sprint 4 | Hito 2 – Text Splitter | v0.2.0 |
| Sprint 5 | Hito 3 – Metadata Manager | v0.3.0 |
| Sprint 6 | Hito 4 – Embeddings | v0.4.0 |
| Sprint 7 | Hito 5 – Vector Store | v0.5.0 |
| Sprint 8 | Hito 6 – Retriever | v0.6.0 |
| Sprint 9 | Hito 7 – Context Builder | v0.7.0 |
| Sprint 10 | Hito 8 – Decision Engine | v0.8.0 |
| Sprint 11 | Hito 9 – Tools | v0.9.0 |
| Sprint 12 | Hito 10 – LLM Provider | v1.0.0 |
| Sprint 13 | Hito 11 – Streamlit UI | v1.1.0 |

---

# 4. Ciclo de desarrollo

Cada Hito deberá seguir obligatoriamente el siguiente flujo.

```text
Planificación
      │
      ▼
SDS
      │
      ▼
Implementación
      │
      ▼
Pruebas
      │
      ▼
README
      │
      ▼
CHANGELOG
      │
      ▼
LOG
      │
      ▼
ROADMAP
      │
      ▼
HANDBOOK
      │
      ▼
MTR
      │
      ▼
Acta de Cierre
      │
      ▼
Git
      │
      ▼
Release
```

---

# 5. Organización del proyecto

## Documentación

La carpeta **01_Documentacion** se organiza por categorías funcionales:

- ADR
- DIA
- DOC
- HANDBOOK
- INSTALL
- LOG
- MTR
- ROADMAP
- SDS

Los documentos **DOC** se organizan por Hito.

Los documentos de planificación y diseño (PLAN, SDS, MTR y Acta de Cierre) se generan de forma independiente para cada Sprint/Hito.

Una vez aprobados y publicados como parte de una Release, dichos documentos no deberán reutilizarse ni sobrescribirse. Cualquier corrección posterior deberá gestionarse mediante control de versiones del repositorio.

---

## Desarrollo

La estructura Python se organiza por responsabilidades.

```text
config/
```

Configuración global del proyecto.

```text
core/
```

Componentes comunes del proyecto y manejo de excepciones compartidas.

```text
knowledge/
```
Implementación del pipeline RAG, incluyendo carga documental, fragmentación, gestión de metadata, generación de embeddings, almacenamiento vectorial, recuperación semántica (Retriever) y construcción de contexto (Context Builder).

```text
llm/
```
Modelos, contratos públicos, Decision Engine, LLM Provider, Factories y componentes de integración con proveedores de modelos de lenguaje.

El paquete `llm` constituye la capa de abstracción entre el pipeline RAG y los modelos LLM, manteniendo el desacoplamiento respecto a implementaciones concretas.

```text
prompts/
```

Plantillas de prompts.

```text
tools/
```

Herramientas del agente.

```text
utils/
```

Utilidades compartidas.

---

# 6. Convenciones de desarrollo

## Configuración

Toda configuración global deberá centralizarse en:

```text
src/config/settings.py
```

No se permite definir rutas, modelos, versiones o parámetros de forma duplicada.

Toda nueva constante global deberá incorporarse en este archivo.

No se recomienda utilizar valores hardcoded cuando exista una configuración equivalente.

---

## Scripts de validación

Estos scripts se utilizan durante el desarrollo para realizar validaciones rápidas de integración entre módulos.

```text
temp/
```

Se ejecutan siempre como módulos:

```bash
python -m temp.check_settings

python -m temp.check_loader

python -m temp.check_text_splitter

python -m temp.check_loader_splitter

python -m temp.check_metadata
```

No deberán ejecutarse mediante rutas directas.

---

## Estrategia oficial de pruebas

El proyecto utiliza dos niveles de validación.
Las **pruebas unitarias** deberán validar preferentemente contratos públicos e interfaces, evitando dependencias directas con implementaciones concretas cuando sea posible.

Las **pruebas automatizadas** no deberán depender de atributos o métodos privados de las implementaciones.

Siempre que sea posible, la validación se realizará utilizando únicamente la API pública definida por los contratos del módulo.

### Uso de fixtures

Las pruebas automatizadas deberán utilizar `pytest.fixture` cuando sea necesario compartir configuraciones o recursos comunes entre múltiples casos de prueba, evitando duplicidad de código y facilitando el mantenimiento de la suite de pruebas.

### Pruebas de integración

Ubicación:

```text
temp/
```

Objetivo:

Validar la integración entre módulos durante el desarrollo.

---

### Pruebas automatizadas

Ubicación:

```text
tests/
```

Framework oficial:

```text
pytest
```

Las pruebas automatizadas validan el cumplimiento de los requisitos funcionales definidos en cada SDS.

### Principios de validación

Las pruebas automatizadas deberán validar el comportamiento observable del módulo y el cumplimiento de sus contratos públicos.

Siempre que sea posible:

- validar Interfaces en lugar de implementaciones concretas;
- utilizar Mock para aislar dependencias externas;
- evitar dependencias con servicios remotos;
- evitar validar atributos privados;
- favorecer pruebas estables frente a cambios internos de implementación.

Esta estrategia mejora la mantenibilidad de la suite de pruebas y facilita la evolución de la arquitectura.



Ejecución oficial:

```bash
python -m pytest
```

o

```bash
python -m pytest tests
```

---

## Instalación de dependencias

Todas las dependencias deberán instalarse utilizando:

```bash
python -m pip install <paquete>
```

No se recomienda utilizar directamente:

```bash
pip install <paquete>
```

especialmente en Windows.

---

## Nuevos módulos

Cada nuevo módulo deberá incluir como mínimo:

- Planificación.
- Documento SDS.
- Implementación.
- Validación incremental mediante microentregas.
- Pruebas de integración.
- Pruebas automatizadas.
- Actualización del MTR.
- Actualización del README.
- Actualización del CHANGELOG.
- Actualización del LOG.
- Actualización del ROADMAP (cuando corresponda).
- Actualización del HANDBOOK (si se incorpora una nueva práctica metodológica).
- Acta de Cierre.
- Release correspondiente.
- Revisión arquitectónica.
- Refactorización antes del cierre documental.
- Diseño del contrato público mediante interfaces (cuando aplique).
- Definición explícita de responsabilidades del módulo.
- Evaluación del impacto arquitectónico antes de modificar componentes existentes.
- Registro de decisiones arquitectónicas relevantes mediante ADR.


| Actividad                   | Obligatoria |
| --------------------------- | :---------: |
| Planificación               |      ✅      |
| SDS                         |      ✅      |
| Implementación              |      ✅      |
| Validación incremental      |      ✅      |
| **Revisión arquitectónica** |      ✅      |
| **Refactorización**         |      ✅      |
| **Validación incremental mediante microentregas**         |      ✅      |
| Pruebas                     |      ✅      |
| Documentación               |      ✅      |
| Release                     |      ✅      |

---

# 7. Reglas de documentación

Todo cambio significativo deberá reflejarse en la documentación correspondiente.

Cada documento debe contener:

- código identificador;
- versión;
- objetivo;
- control de versiones.

Toda mejora metodológica aprobada durante un Sprint deberá incorporarse al HANDBOOK antes de la publicación de la Release correspondiente.

Los documentos técnicos deberán diferenciar claramente entre:

- especificación del diseño implementado;
- decisiones arquitectónicas adoptadas durante el desarrollo.

Las decisiones de arquitectura deberán registrarse inicialmente en el SDS correspondiente mediante ADR y únicamente incorporarse al HANDBOOK cuando se conviertan en estándares reutilizables para futuros Sprint.

Toda decisión arquitectónica permanente deberá reflejarse primero en el SDS correspondiente y posteriormente incorporarse al HANDBOOK únicamente cuando represente un estándar reutilizable para futuros Sprint.

Antes de incorporar una mejora arquitectónica o metodológica, deberá analizarse su impacto sobre los Sprint previamente cerrados. Ninguna modificación estructural se implementará sin una evaluación previa y su correspondiente aprobación.

El HANDBOOK constituye la referencia oficial de las prácticas de desarrollo vigentes del proyecto.

Se mantendrá un único documento vivo.

Git conservará el historial completo.

Toda incorporación de un nuevo módulo, herramienta, dependencia o componente compartido deberá documentarse antes de realizar el commit.

---

# 8. Reglas para Git

Cada Hito deberá finalizar con:

1. Validación técnica.
2. Ejecución de pruebas automatizadas.
3. Actualización de la documentación.
4. Revisión del estado del repositorio (`git status`).
5. git diff --stat ,con el fin de verificar que únicamente se incorporan los archivos previstos para la Release.
6. Commit descriptivo.
7. Push al repositorio remoto.
8. Creación del tag de Release (cuando corresponda).

Las Releases únicamente se publicarán cuando el Hito haya sido completamente validado.

---

# 9. Criterios para cerrar un Hito

Un Hito se considerará finalizado únicamente cuando se cumplan todos los siguientes criterios:

- SDS aprobado.
- Implementación completada.
- Pruebas de integración ejecutadas cuando correspondan al alcance del Hito.
- Pruebas automatizadas aprobadas.
- Cobertura completa de los Casos de Prueba (CP).
- Documentación actualizada.
- Git actualizado.
- Release preparada.
- ROADMAP actualizado (cuando corresponda).
- HANDBOOK actualizado (cuando se aprueben nuevas prácticas metodológicas).
- Arquitectura validada y sin regresiones respecto a Sprint anteriores.
- Validación de la consistencia documental entre PLAN, SDS, README, CHANGELOG, LOG, ROADMAP, HANDBOOK y MTR antes de preparar la Release.

---

# 10. Relación con otros documentos

| Documento      | Propósito                                                |
| -------------- | -------------------------------------------------------- |
| ROADMAP        | Planificación estratégica del proyecto.                  |
| PLAN           | Planificación del Sprint.                                |
| LOG            | Registro de decisiones y evolución técnica.              |
| MTR            | Trazabilidad entre requisitos, implementación y pruebas. |
| SDS            | Diseño técnico del módulo.                               |
| DOC            | Documentación funcional y de apoyo.                      |
| README         | Estado general y guía del proyecto.                      |
| CHANGELOG      | Historial de Releases.                                   |
| Acta de Cierre | Evidencia formal del cierre del Sprint.                  |


---

# 11. Mejora continua

Las reglas establecidas en este HANDBOOK podrán evolucionar cuando una mejora metodológica sea aprobada durante una Auditoría Arquitectónica o durante el cierre de un Sprint.

Toda modificación deberá registrarse en el control de versiones del documento.

Las mejoras metodológicas aprobadas durante un Sprint deberán incorporarse a este HANDBOOK antes del cierre de la Release correspondiente, garantizando que el documento represente siempre el estándar oficial vigente del proyecto.

Las mejoras metodológicas deberán incorporarse respetando la estabilidad de los módulos previamente liberados.

Toda mejora metodológica deberá ser analizada, justificada y aprobada antes de incorporarse al HANDBOOK.

Las mejoras metodológicas deberán mantenerse compatibles con los Sprint previamente cerrados y no implicarán modificaciones retroactivas de la arquitectura sin un análisis formal de impacto.

---

# Control de versiones

| Versión | Fecha | Descripción |
|----------|--------|-------------|
| 1.0 | Junio 2026 | Guía inicial del proyecto. |
| 2.0 | 02/07/2026 | Reestructuración completa tras la Auditoría Arquitectónica. Incorporación de la metodología Sprint → Hito → Release. |
| 2.1 | 03/07/2026 | Incorporación de la estrategia oficial de pruebas con pytest, separación entre pruebas de integración y automatizadas, reglas para instalación de dependencias, actualización del flujo de cierre de Hitos y formalización de las mejoras metodológicas derivadas del Sprint 5. |
| 2.2 | 05/07/2026  | Actualización metodológica derivada del Sprint 7. Incorporación del flujo documental completo (MTR, README, CHANGELOG, LOG, ROADMAP, HANDBOOK y Acta de Cierre), formalización del uso de `pytest.fixture`, actualización de los criterios de cierre de Hitos y consolidación de la metodología documental del proyecto. |
| 2.3 | 08/07/2026 | Actualización derivada del Sprint 8. Formalización del estándar oficial de imports (`src.` entre paquetes e imports relativos dentro del mismo paquete), incorporación del patrón Factory como mecanismo oficial de ensamblado de dependencias, adopción de la validación incremental mediante microentregas y consolidación de la política de no introducir cambios arquitectónicos sin análisis previo de impacto. |
| 2.4 | 09/07/2026 | Actualización derivada del Sprint 9. Incorporación del flujo documental optimizado (MTR al final del proceso), formalización de la revisión arquitectónica previa al cierre, consolidación de los estándares permanentes del proyecto (interfaces, Factory Pattern, configuración centralizada, tipado fuerte y validación incremental) y actualización del pipeline RAG con el módulo Context Builder. |
| 2.5 | 10/07/2026 | Actualización derivada del Sprint 10. Formalización del uso de contratos públicos mediante interfaces cuando corresponda, consolidación del modelo de validación incremental por microentregas, incorporación de la revisión de git diff --stat antes del commit y actualización de la organización del paquete llm para reflejar la incorporación del Decision Engine. |
| 2.6 | 11/07/2026 | Actualización derivada del Sprint 11. Formalización de la generación independiente de la documentación por Sprint/Hito (PLAN, SDS, MTR y Acta de Cierre), consolidación del principio de validar únicamente la API pública en las pruebas automatizadas, incorporación de la separación entre especificación técnica y decisiones arquitectónicas mediante ADR, y establecimiento de la validación de consistencia documental como requisito previo a la publicación de una Release. |
| **2.7** | **11/07/2026** | Actualización derivada del Sprint 12. Formalización del principio de validar el comportamiento observable mediante contratos públicos, adopción del uso sistemático de `Mock` para aislar dependencias externas, consolidación del análisis de responsabilidades antes de implementar nuevos módulos, fortalecimiento del registro de decisiones arquitectónicas (ADR) y actualización de la organización del paquete `llm` para incorporar la capa `LLM Provider`. |
