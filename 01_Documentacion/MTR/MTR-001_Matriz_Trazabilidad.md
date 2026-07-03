# MTR-001 – Matriz de Trazabilidad

**Código:** MTR-001

**Versión:** 2.1

**Estado:** Activo

**Proyecto:** Mercado Central AI

---

# 1. Objetivo

Establecer la trazabilidad entre los módulos funcionales del proyecto, los requisitos asociados, los documentos de diseño, la implementación, las pruebas y las releases.

La matriz permite verificar que cada requisito tenga:

- documentación;
- diseño;
- implementación;
- validación;
- seguimiento.

Con ello se garantiza la consistencia entre la planificación y la implementación del proyecto.

---

# 2. Alcance

La matriz cubre todo el ciclo de vida del proyecto:

```text
Requisito
      ↓
Diseño (SDS)
      ↓
Código
      ↓
Pruebas
      ↓
Release
```

Cada nuevo módulo deberá incorporarse a esta matriz antes de considerarse finalizado.

---

# 3. Metodología

La trazabilidad oficial del proyecto sigue la siguiente estructura:

```text
Sprint
      ↓
Hito
      ↓
Requisito
      ↓
SDS
      ↓
Código
      ↓
Pruebas
      ↓
Release
```

Esta metodología fue aprobada durante la Auditoría Arquitectónica (DOC-014).

---

# 4. Matriz de trazabilidad

| Módulo | Sprint | Hito | RF | SDS | Código | Validación | Release | Estado |
|--------|:------:|:----:|----|-----|---------|------------|:-------:|:------:|
| Document Loader | Sprint 3 | Hito 1 | RF-001 | SDS-001 | loader.py | check_loader.py | v0.1.1 | ✅ |
| Text Splitter | Sprint 4 | Hito 2 | RF-006–RF-010 | SDS-002 | splitter.py | check_text_splitter.py / check_loader_splitter.py | v0.2.0 | ✅ |
| Metadata Manager | Sprint 5 | Hito 3 | RF-011–RF-015 | SDS-003 | metadata.py + exceptions.py | check_metadata.py / test_metadata.py | v0.3.0 | ✅ |
| Embeddings Engine | Sprint 6 | Hito 4 | RF-016–RF-020 | SDS-004 | embeddings.py | test_embeddings.py | v0.4.0 | ⏳ |
| Vector Store | Sprint 7 | Hito 5 | RF-021–RF-025 | SDS-005 | vector_store.py | test_vector_store.py | v0.5.0 | ⏳ |
| Retriever | Sprint 8 | Hito 6 | RF-026–RF-030 | SDS-006 | retriever.py | test_retriever.py | v0.6.0 | ⏳ |
| Context Builder | Sprint 9 | Hito 7 | RF-031–RF-035 | SDS-007 | context_builder.py | test_context_builder.py | v0.7.0 | ⏳ |
| Decision Engine | Sprint 10 | Hito 8 | RF-036–RF-040 | SDS-008 | decision_engine.py | test_decision_engine.py | v0.8.0 | ⏳ |
| Tools | Sprint 11 | Hito 9 | RF-041–RF-045 | SDS-009 | tools/*.py | test_tools.py | v0.9.0 | ⏳ |
| Interfaz Streamlit | Sprint 12 | Hito 10 | RF-046–RF-050 | SDS-010 | app.py | test_ui.py | v1.0.0 | ⏳ |

---

# Sprint 4 – Hito 2

## Módulo

Text Splitter

| RF | Descripción | SDS | Implementación | Pruebas | Estado |
|----|-------------|-----|----------------|----------|:------:|
| RF-006 | Recibir una colección de documentos | SDS-002 | TextSplitter | check_text_splitter | ✅ |
| RF-007 | Fragmentar documentos utilizando RecursiveCharacterTextSplitter | SDS-002 | _split() | Caso 4 y Caso 5 | ✅ |
| RF-008 | Leer configuración desde settings.py | SDS-002 | __init__() | Inicialización | ✅ |
| RF-009 | Enriquecer la metadata de los chunks | SDS-002 | _enrich_metadata() | Caso 5 | ✅ |
| RF-010 | Integrarse con Document Loader | SDS-002 | split_documents() | check_loader_splitter | ✅ |

### Resultado

Todos los requerimientos funcionales definidos para el módulo Text Splitter fueron implementados, validados y preparados para la Release v0.2.0.

---

# Sprint 5 – Hito 3

## Módulo

Metadata Manager

**Sprint:** 5

**Hito:** 3

**Estado:** Implementado y validado

---

| RF | Descripción | SDS | Implementación | Código | Casos de Prueba | Estado |
|----|-------------|-----|----------------|--------|-----------------|:------:|
| RF-011 | Recibir la colección de chunks generados por el Text Splitter | SDS-003 | IMP-02 | process_documents() | CP-001 | ✅ |
| RF-012 | Validar la metadata mínima requerida | SDS-003 | IMP-02 | _validate_metadata() | CP-002, CP-003 | ✅ |
| RF-013 | Normalizar la metadata | SDS-003 | IMP-03 | _normalize_metadata() | CP-004 | ✅ |
| RF-014 | Enriquecer la metadata | SDS-003 | IMP-04 | _enrich_metadata() | CP-005 | ✅ |
| RF-015 | Entregar documentos listos para Embeddings | SDS-003 | IMP-05 | process_documents() | CP-006, CP-007, CP-008, CP-009 | ✅ |

---

## Cobertura de requisitos

| Tipo | Cantidad |
|------|---------:|
| Requisitos funcionales | 5 |
| Implementaciones | 5 |
| Casos de prueba | 9 |
| Requisitos cubiertos | 5 |
| Cobertura | **100 %** |

---

## Archivos asociados

### Código fuente

```text
src/
│
├── knowledge/
│      metadata.py
│
└── core/
       exceptions.py
```

### Configuración

```text
src/config/settings.py
```

### Pruebas

### 1. Scripts de validación para desarrollo

```text
temp/
└── check_metadata.py

Estos scripts se utilizan durante el desarrollo para realizar validaciones rápidas de integración entre módulos.

La carpeta `temp/` no forma parte de los entregables versionados del proyecto y puede estar excluida del control de versiones mediante `.gitignore`.


tests/
├── __init__.py
└── test_metadata.py
```

### Diseño

```text
01_Documentacion/
└── SDS/
    SDS-003_Metadata_Manager.md
```

---

## Flujo de trazabilidad

```text
RF
 │
 ▼
SDS
 │
 ▼
Implementación (IMP)
 │
 ▼
Código
 │
 ▼
Caso de Prueba (CP)
 │
 ▼
Release
```

---

## Convenciones

| Sigla | Significado |
|-------|-------------|
| RF | Requisito Funcional |
| SDS | Software Design Specification |
| IMP | Implementación |
| CP | Caso de Prueba |
| MTR | Matriz de Trazabilidad |

---

## Observaciones

A partir del Sprint 5 se incorporó oficialmente la estrategia de pruebas automatizadas mediante **pytest**, complementando los scripts de validación ubicados en `temp/`.

La trazabilidad del proyecto ahora relaciona cada requisito funcional con su diseño, implementación, código, casos de prueba y release correspondiente, fortaleciendo la mantenibilidad y la auditoría técnica del proyecto.