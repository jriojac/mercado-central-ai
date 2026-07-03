# LOG-001 -- Bitácora Técnica

## 2026-07-01 -- Cierre del Hito 1

### Actividades realizadas

-   Finalización del módulo `DocumentLoader`.
-   Validación de la Base de Conocimiento.
-   Integración de 4 documentos PDF.
-   Carga exitosa de 124 objetos `Document`.
-   Refactorización de `loader.py`.
-   Ejecución de pruebas funcionales.
-   Configuración de Git y GitHub.
-   Creación de los tags `v0.1.0` y `v0.1.1`.
-   Consolidación de la documentación.

### Resultado

**Hito 1 finalizado satisfactoriamente.**

Estado del proyecto:

-   Loader operativo.
-   Base de Conocimiento integrada.
-   Proyecto documentado y versionado.
-   Listo para iniciar el Sprint 4.

# Registro de Avances (LOG)

---

## Sprint 4 – Hito 2

## 2026-07-01 -- Cierre del Hito 2

### Módulo
Text Splitter

### Estado
Finalizado

### Actividades realizadas

- Implementación de la clase `TextSplitter`.
- Integración de `RecursiveCharacterTextSplitter`.
- Lectura de configuración desde `settings.py`.
- Implementación de validación de documentos de entrada.
- Implementación de la fragmentación de documentos.
- Implementación del enriquecimiento de metadata de los chunks.
- Integración con el módulo `DocumentLoader`.
- Validación mediante pruebas unitarias y de integración.

### Resultados

- Fragmentación correcta de documentos.
- Conservación de metadata original.
- Incorporación de metadata enriquecida:
  - `chunk_index`
  - `total_chunks`
  - `chunk_size`
  - `splitter_version`
- Generación correcta de chunks para documentos reales de la Knowledge Base.

### Evidencias

#### check_text_splitter

- Validación de inicialización.
- Validación de errores.
- Documento corto.
- Documento largo.
- Metadata enriquecida.

#### check_loader_splitter

- Integración Document Loader → Text Splitter.
- 4 PDFs procesados.
- 124 documentos cargados.
- 367 chunks generados.
- 0 errores.

### Estado final

Sprint 4 – Hito 2 listo para documentación final, control de versiones y preparación de la Release v0.2.0.

---


# Registro de avance

---

## Fecha

03/07/2026

## Sprint

Sprint 5

## Hito

Hito 3 – Metadata Manager

## Release objetivo

v0.3.0

---

## Objetivo

Implementar el módulo **Metadata Manager**, responsable de validar, normalizar y enriquecer la metadata asociada a los documentos generados por el Text Splitter antes del proceso de generación de embeddings.

---

## Actividades realizadas

### Planificación

- Definición del alcance del Metadata Manager.
- Identificación de los requisitos funcionales RF-011 a RF-015.
- Definición de la estrategia de implementación del módulo.

### Diseño

- Elaboración del documento **SDS-003 – Software Design Specification**.
- Definición de la arquitectura interna del Metadata Manager.
- Definición de reglas oficiales para la normalización de metadata.
- Incorporación de trazabilidad entre requisitos funcionales, implementaciones y casos de prueba.

### Implementación

Se implementó la clase:

```text
MetadataManager
```

con las siguientes responsabilidades:

- Validación de metadata obligatoria.
- Normalización de metadata.
- Enriquecimiento automático de metadata.
- Validación de colecciones de documentos.
- Preparación de documentos para el módulo Embeddings.

También se incorporó el archivo:

```text
src/core/exceptions.py
```

para centralizar las excepciones personalizadas del proyecto.

---

## Pruebas

Se incorporó por primera vez un framework de pruebas automatizadas basado en **pytest**.

Se creó la siguiente estructura:

```text
tests/
│
├── __init__.py
└── test_metadata.py
```

Casos de prueba implementados:

| Caso | Estado |
|------|--------|
| CP-001 | ✅ |
| CP-002 | ✅ |
| CP-003 | ✅ |
| CP-004 | ✅ |
| CP-005 | ✅ |
| CP-006 | ✅ |
| CP-007 | ✅ |
| CP-008 | ✅ |
| CP-009 | ✅ |

Resultado:

```text
9 passed
```

Se mantiene adicionalmente el script de integración:

```text
temp/check_metadata.py
```

---

## Mejoras metodológicas

Durante este Sprint se incorporaron nuevas prácticas al proyecto:

- Uso oficial de **pytest** para pruebas funcionales.
- Separación entre pruebas de integración (`temp/`) y pruebas automatizadas (`tests/`).
- Incorporación de Casos de Prueba (CP) dentro del SDS.
- Trazabilidad completa:

```text
RF
 ↓
SDS
 ↓
IMP
 ↓
CP
 ↓
Release
```

- Recomendación oficial de utilizar:

```bash
python -m pip
```

en lugar de `pip` para la instalación de dependencias.

---

## Archivos creados

```text
src/knowledge/metadata.py
src/core/exceptions.py
tests/test_metadata.py
temp/check_metadata.py  | Herramientas y scripts de apoyo para el desarrollo (locales, no forman parte de la Release).
```

---

## Archivos actualizados

```text
src/config/settings.py

SDS-003_Document_Metadata.md

README.md (pendiente)

LOG-001_Bitacora_Tecnica.md

MTR-001_Matriz_Trazabilidad.md (pendiente)

CHANGELOG.md (pendiente)
```

---

## Resultado del Sprint

Estado del Metadata Manager:

```text
MetadataManager

✔ Validación

✔ Normalización

✔ Enriquecimiento

✔ Integración

✔ Pruebas automatizadas
```

Estado general del pipeline:

```text
Knowledge Base
      │
      ▼
Document Loader        ✅
      │
      ▼
Text Splitter          ✅
      │
      ▼
Metadata Manager       ✅
      │
      ▼
Embeddings             ⏳
```

---

## Observaciones

El Sprint permitió consolidar la estrategia de validación automática del proyecto mediante pytest y establecer una metodología reutilizable para los siguientes módulos del pipeline RAG.

# Registro de avance

---

## Fecha

03/07/2026

## Sprint

Sprint 5

## Hito

Hito 3 – Metadata Manager

## Release objetivo

v0.3.0

---

## Objetivo

Implementar el módulo **Metadata Manager**, responsable de validar, normalizar y enriquecer la metadata asociada a los documentos generados por el Text Splitter antes del proceso de generación de embeddings.

---

## Actividades realizadas

### Planificación

- Definición del alcance del Metadata Manager.
- Identificación de los requisitos funcionales RF-011 a RF-015.
- Definición de la estrategia de implementación del módulo.

### Diseño

- Elaboración del documento **SDS-003 – Software Design Specification**.
- Definición de la arquitectura interna del Metadata Manager.
- Definición de reglas oficiales para la normalización de metadata.
- Incorporación de trazabilidad entre requisitos funcionales, implementaciones y casos de prueba.

### Implementación

Se implementó la clase:

```text
MetadataManager
```

con las siguientes responsabilidades:

- Validación de metadata obligatoria.
- Normalización de metadata.
- Enriquecimiento automático de metadata.
- Validación de colecciones de documentos.
- Preparación de documentos para el módulo Embeddings.

También se incorporó el archivo:

```text
src/core/exceptions.py
```

para centralizar las excepciones personalizadas del proyecto.

---

## Pruebas

Se incorporó por primera vez un framework de pruebas automatizadas basado en **pytest**.

Se creó la siguiente estructura:

```text
tests/
│
├── __init__.py
└── test_metadata.py
```

Casos de prueba implementados:

| Caso | Estado |
|------|--------|
| CP-001 | ✅ |
| CP-002 | ✅ |
| CP-003 | ✅ |
| CP-004 | ✅ |
| CP-005 | ✅ |
| CP-006 | ✅ |
| CP-007 | ✅ |
| CP-008 | ✅ |
| CP-009 | ✅ |

Resultado:

```text
9 passed
```

Se mantiene adicionalmente el script de integración:
Estos scripts se utilizan durante el desarrollo para realizar validaciones rápidas de integración entre módulos.

```text
temp/check_metadata.py
```

---

## Mejoras metodológicas

Durante este Sprint se incorporaron nuevas prácticas al proyecto:

- Uso oficial de **pytest** para pruebas funcionales.
- Separación entre pruebas de integración (`temp/`) y pruebas automatizadas (`tests/`).
- Incorporación de Casos de Prueba (CP) dentro del SDS.
- Trazabilidad completa:

```text
RF
 ↓
SDS
 ↓
IMP
 ↓
CP
 ↓
Release
```

- Recomendación oficial de utilizar:

```bash
python -m pip
```

en lugar de `pip` para la instalación de dependencias.

---

## Archivos creados

```text
src/knowledge/metadata.py
src/core/exceptions.py
tests/test_metadata.py
temp/check_metadata.py
```

---

## Archivos actualizados

```text
src/config/settings.py

SDS-003_Document_Metadata.md

README.md (pendiente)

LOG-001_Bitacora_Tecnica.md

MTR-001_Matriz_Trazabilidad.md (pendiente)

CHANGELOG.md (pendiente)
```

---

## Resultado del Sprint

Estado del Metadata Manager:

```text
MetadataManager

✔ Validación

✔ Normalización

✔ Enriquecimiento

✔ Integración

✔ Pruebas automatizadas
```

Estado general del pipeline:

```text
Knowledge Base
      │
      ▼
Document Loader        ✅
      │
      ▼
Text Splitter          ✅
      │
      ▼
Metadata Manager       ✅
      │
      ▼
Embeddings             ⏳
```

---

## Observaciones

El Sprint permitió consolidar la estrategia de validación automática del proyecto mediante pytest y establecer una metodología reutilizable para los siguientes módulos del pipeline RAG.

## Lecciones aprendidas

- Centralizar la configuración en `settings.py` simplifica el mantenimiento del proyecto.
- El uso de `python -m pip` evita problemas con entornos virtuales en Windows.
- La incorporación de `pytest` mejora significativamente la calidad y automatización de las pruebas.
- Mantener trazabilidad entre RF, IMP y CP facilita la validación y evolución del sistema.