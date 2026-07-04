# SDS-004
# Software Design Specification
## Módulo: Embeddings
## Versión: 1.0
## Release objetivo: v0.4.0

---

# 1. Información del documento

| Campo | Valor |
|--------|-------|
| Documento | SDS-004 |
| Título | Software Design Specification – Embeddings |
| Versión | 1.0 |
| Estado | Implementado |
| Sprint | 6 |
| Hito | 4 |
| Módulo | Embeddings |
| Release objetivo | v0.4.0 |
| Autor | Jacqueline Rioja |
| Fecha | 03/07/2026 |
| Última actualización | 04/07/2026 |

---

# 2. Objetivo

Este documento define el diseño técnico del módulo **Embeddings**, responsable de transformar los documentos enriquecidos por el **Metadata Manager** en representaciones vectoriales (embeddings) que serán utilizadas posteriormente por el **Vector Store** para la indexación y búsqueda semántica.

El SDS constituye la especificación oficial para la implementación del módulo y garantiza la trazabilidad entre los requisitos funcionales, la implementación, las pruebas automatizadas y la futura integración con el resto del pipeline RAG.

---

# 3. Alcance

## Incluye

El módulo será responsable de:

- recibir la colección de documentos enriquecidos por el Metadata Manager;
- validar la estructura de entrada antes de generar los embeddings;
- generar embeddings utilizando un proveedor configurable;
- conservar íntegramente el contenido y la metadata de cada documento;
- preparar la colección para el módulo Vector Store;
- manejar los errores producidos durante la generación de embeddings.

## No incluye

- almacenamiento de embeddings;
- administración de bases vectoriales;
- búsqueda semántica;
- recuperación de documentos;
- construcción del contexto (Context Builder);
- interacción con modelos conversacionales.

Estas responsabilidades corresponden a los siguientes hitos del proyecto.

---

# 4. Referencias

Documentos relacionados:

- HANDBOOK
- ROADMAP
- README
- CHANGELOG
- MTR
- SDS-003 Metadata Manager

---

# 5. Contexto dentro del Pipeline RAG

Dentro del pipeline RAG, el módulo **Embeddings** recibe los documentos procesados por el **Metadata Manager**, genera su representación vectorial y entrega el resultado al **Vector Store**.

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
Embeddings
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
Gemini
```

Su función consiste en convertir el contenido textual de cada documento en una representación numérica que preserve su significado semántico, permitiendo posteriormente realizar búsquedas por similitud dentro del Vector Store.

## Entrada

Colección de objetos `Document` enriquecidos por el Metadata Manager.

Cada documento contiene:

- page_content
- metadata completa
- identificadores del documento
- información de trazabilidad

## Salida

Colección de documentos lista para el módulo **Vector Store**, donde cada elemento conserva:

- documento original;
- metadata enriquecida;
- embedding generado.

---

# 6. Requerimientos funcionales

## RF-040

Recibir la colección de documentos procesados por el Metadata Manager.

### Entrada

Lista de objetos `Document`.

### Proceso

Validar que la colección recibida sea una lista válida de documentos antes de iniciar la generación de embeddings.

### Salida

Colección preparada para la generación de embeddings.

---

## RF-041

Generar embeddings para cada documento utilizando el proveedor configurado.

### Entrada

Colección válida de objetos `Document`.

### Proceso

Enviar el contenido (`page_content`) de cada documento al proveedor de embeddings configurado y obtener su representación vectorial.

### Salida

Colección de documentos con su embedding asociado.

---

## RF-042

Conservar íntegramente la metadata generada por el Metadata Manager.

El proceso de generación de embeddings no deberá modificar ni eliminar ningún campo de la metadata existente.

Toda la información deberá mantenerse disponible para el módulo Vector Store.

---

## RF-043

Gestionar errores durante la generación de embeddings.

El módulo deberá detectar y controlar situaciones como:

- proveedor no disponible;
- tiempo de espera excedido;
- configuración inválida;
- cuota de servicio agotada;
- documento inválido.

Las excepciones deberán propagarse de forma controlada al pipeline.

---

## RF-044

Permitir la configuración del proveedor de embeddings mediante `settings.py`.

La selección del proveedor y del modelo no deberá encontrarse codificada dentro del módulo.

Toda la configuración deberá centralizarse en el archivo de configuración del proyecto.

---

## RF-045

Entregar la colección preparada para el módulo Vector Store.

La salida deberá conservar:

- documento original;
- metadata completa;
- embedding generado.

---

# 7. Responsabilidades del módulo

El módulo Embeddings será responsable de:

- Recibir documentos provenientes del Metadata Manager.
- Validar la estructura de entrada.
- Generar embeddings para cada documento.
- Preservar la metadata existente.
- Asociar cada embedding con su documento correspondiente.
- Retornar la colección lista para el Vector Store.

No será responsabilidad del módulo:

- almacenar embeddings;
- administrar bases vectoriales;
- realizar búsquedas semánticas;
- construir contexto para el LLM;
- invocar modelos conversacionales.

---

# 8. Arquitectura del módulo

```text
Metadata Manager
      │
      ▼
 Embeddings
      │
 ┌────┴─────────────┐
 │                  │
Validación     Embedding Provider
                      │
                      ▼
             Modelo de Embeddings
                      │
                      ▼
          Asociación Documento + Vector
                      │
                      ▼
               Vector Store
```

La arquitectura separa la lógica de negocio del proveedor de embeddings, permitiendo sustituir el modelo de IA sin modificar el flujo principal del pipeline.

---

# 9. Flujo de procesamiento

```text
Recibir Document[]

        │

        ▼

Validar colección

        │

        ▼

Validar documento

        │

        ▼

Generar embedding

        │

        ▼

Asociar embedding al documento

        │

        ▼

Verificar resultado

        │

        ▼

Retornar colección
```

---

# 10. Modelo de datos

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| document | Document | Sí | Documento original proveniente del Metadata Manager |
| page_content | str | Sí | Contenido textual utilizado para generar el embedding |
| metadata | dict | Sí | Metadata enriquecida del documento |
| embedding | list[float] | Sí | Vector generado por el modelo de embeddings |
| embedding_model | str | Sí | Modelo utilizado para generar el embedding |
| embedding_provider | str | Sí | Proveedor configurado |
| embedding_dimension | int | Sí | Dimensión del vector generado |
| embedding_date | datetime | Sí | Fecha y hora de generación |
| embedding_version | str | Sí | Versión del módulo Embeddings |


---

# 11. Diseño de clases

## Clase principal

```python
class Embeddings:
```

### Responsabilidad

Administrar el proceso completo de generación de embeddings para los documentos procesados por el Metadata Manager.

La clase será responsable de:

- validar la colección recibida;
- generar embeddings mediante el proveedor configurado;
- preservar la metadata existente;
- asociar el vector generado a cada documento;
- retornar la colección preparada para el Vector Store.

---

## Clase de soporte

```python
class EmbeddingProvider:
```

### Responsabilidad

Abstraer la comunicación con el proveedor de embeddings.

Su implementación permitirá sustituir el proveedor de IA sin modificar el módulo Embeddings.

Inicialmente utilizará Google Generative AI, pero la arquitectura permitirá incorporar otros proveedores en futuras versiones.

---

# 12. Interfaces públicas

```python
generate_embeddings()
```

Genera embeddings para una colección de documentos.

---

```python
_generate_embedding()
```

Genera el embedding de un único documento.

Uso interno.

---

```python
_validate_documents()
```

Verifica la validez de la colección recibida antes del procesamiento.

Uso interno.

---

```python
_create_provider()
```

Inicializa el proveedor de embeddings configurado.

Uso interno.

---

# 13. Reglas de validación

Validaciones mínimas:

- La entrada debe ser una lista.
- La colección puede estar vacía.
- Todos los elementos deben ser objetos `Document`.
- Todo documento debe contener `page_content`.
- Todo documento debe contener `metadata`.
- El contenido textual no puede ser nulo.
- El proveedor de embeddings debe encontrarse configurado.
- El modelo seleccionado debe existir.
- La API Key debe encontrarse disponible.

---

# 14. Configuración del módulo

Toda la configuración deberá mantenerse centralizada en:

```text
src/config/settings.py
```

Configuraciones previstas:

```python
EMBEDDING_PROVIDER

EMBEDDING_MODEL

EMBEDDING_BATCH_SIZE

EMBEDDING_TIMEOUT

EMBEDDING_RETRIES
```

La implementación no deberá contener valores codificados (hardcoded).

La configuración deberá permitir cambiar el proveedor de embeddings sin modificar el código del módulo.

La autenticación con Google Generative AI se realiza mediante la variable de entorno:

GOOGLE_API_KEY

La clave no debe almacenarse en el repositorio y deberá configurarse mediante el archivo .env.

---

# 15. Generación de embeddings

Para cada documento recibido el módulo deberá ejecutar el siguiente proceso:

1. Validar la estructura del documento.
2. Obtener el contenido textual (`page_content`).
3. Enviar el contenido al proveedor configurado.
4. Obtener el vector generado.
5. Asociar el embedding al documento correspondiente.
6. Conservar íntegramente la metadata.
7. Registrar la información necesaria para trazabilidad.
8. Agregar el documento procesado a la colección de salida.

El proceso deberá mantener la correspondencia entre cada documento y su embedding, garantizando la integridad de la información durante todo el pipeline.

---

# 16. Manejo de errores

Excepciones previstas:

- EmbeddingProviderError
- InvalidDocumentError
- EmbeddingConfigurationError
- EmbeddingTimeoutError

Cada excepción deberá indicar:

- causa;
- impacto;
- acción correctiva recomendada.

El módulo no deberá finalizar inesperadamente ante errores controlados.

Los errores deberán registrarse y propagarse al pipeline para permitir su tratamiento por los módulos superiores.

---

# 17. Logging

Registrar como mínimo:

- Inicio del proceso de generación de embeddings.
- Fin del procesamiento.
- Cantidad de documentos recibidos.
- Cantidad de embeddings generados.
- Modelo utilizado.
- Proveedor utilizado.
- Tiempo total de procesamiento.
- Advertencias.
- Errores detectados.

El contenido de los documentos y los embeddings generados no deberán registrarse en los logs para evitar un consumo innecesario de almacenamiento y proteger la información procesada.

---

# 18. Consideraciones de rendimiento

Objetivos:

- Complejidad O(n).
- Procesamiento por lotes (Batch Processing).
- Reutilizar la instancia del proveedor de embeddings.
- Evitar llamadas innecesarias al servicio de IA.
- Reducir el consumo de memoria.
- Mantener la correspondencia entre documentos y embeddings.
- Permitir el procesamiento de grandes volúmenes de documentos.

La arquitectura deberá facilitar futuras optimizaciones como procesamiento paralelo o generación asíncrona de embeddings.

---

# 19. Extensibilidad

La arquitectura deberá permitir incorporar nuevas funcionalidades sin modificar el flujo principal del módulo.

Ejemplos:

- nuevos proveedores de embeddings;
- nuevos modelos de embeddings;
- procesamiento asíncrono;
- generación por lotes configurable;
- caché de embeddings;
- soporte para modelos locales (Ollama);
- integración con múltiples motores Vector Store;
- métricas de rendimiento;
- monitoreo del consumo de tokens.

---

# 20. Casos de Prueba

La validación del módulo **Embeddings** se realizará mediante pruebas automatizadas utilizando **pytest**.

Cada caso de prueba mantiene trazabilidad con los requisitos funcionales definidos para el módulo.

| Caso | Requisito | Objetivo | Resultado esperado |
|------|-----------|----------|--------------------|
| CP-019 | RF-040 | Procesar una colección válida de documentos. | La colección se procesa correctamente. |
| CP-020 | RF-041 | Generar embeddings para múltiples documentos. | Todos los documentos obtienen un embedding válido. |
| CP-021 | RF-042 | Verificar la conservación de la metadata. | La metadata permanece sin modificaciones. |
| CP-022 | RF-043 | Simular un proveedor no disponible. | Se genera `EmbeddingProviderError`. |
| CP-023 | RF-043 | Simular un tiempo de espera excedido. | Se genera `EmbeddingTimeoutError`. |
| CP-024 | RF-044 | Verificar la configuración desde `settings.py`. | El proveedor y el modelo se cargan correctamente. |
| CP-025 | RF-045 | Ejecutar el flujo completo del módulo. | La colección queda preparada para el Vector Store. |


## Validación de integración

Se implementó el script:

temp/check_pipeline_embeddings.py

Este script valida el flujo completo:

Document Loader
↓
Text Splitter
↓
Metadata Manager
↓
Embeddings

Durante las pruebas se utiliza una muestra reducida de documentos para respetar las restricciones del nivel gratuito del proveedor Google Generative AI.

---

## Cobertura de pruebas

La siguiente matriz muestra la relación entre los requisitos funcionales y los casos de prueba.

| Requisito | Casos de prueba |
|-----------|-----------------|
| RF-040 | CP-019 |
| RF-041 | CP-020 |
| RF-042 | CP-021 |
| RF-043 | CP-022, CP-023 |
| RF-044 | CP-024 |
| RF-045 | CP-025 |

---

## Herramienta de pruebas

Las pruebas funcionales del proyecto se implementan utilizando **pytest**.

Las pruebas de integración rápida continúan ejecutándose mediante los scripts ubicados en:

Herramientas y scripts de apoyo para el desarrollo (locales, no forman parte de la Release)

```text
temp/
```

Las pruebas automatizadas se ubican en:

```text
tests/
```

Ejemplos de ejecución:

```bash
python -m pytest
```

```bash
python -m pytest tests
```

```bash
python -m pytest tests/test_embeddings.py
```


---

# 21. Trazabilidad

La siguiente matriz establece la relación entre los requisitos funcionales, la implementación y los casos de prueba definidos para el módulo Embeddings.

| RF | Clase | Método | Implementación | Caso de prueba |
|----|--------|---------|----------------|----------------|
| RF-040 | Embeddings | generate_embeddings | IMP-04 | CP-019 |
| RF-041 | Embeddings | generate_embeddings | IMP-05 | CP-020 |
| RF-042 | Embeddings | _generate_embedding | IMP-05 | CP-021 |
| RF-043 | Embeddings | _generate_embedding | IMP-06 | CP-022, CP-023 |
| RF-044 | Embeddings | _create_provider | IMP-03 | CP-024 |
| RF-045 | Embeddings | generate_embeddings | IMP-07 | CP-025 |

---

# 22. Riesgos técnicos

Los principales riesgos identificados para este módulo son los siguientes:

- Cambios futuros en la API del proveedor de embeddings.
- Cambios en LangChain que afecten la integración.
- Límites de cuota o restricciones del servicio de IA.
- Incremento en el tiempo de procesamiento para grandes volúmenes de documentos.
- Cambios en las dimensiones de los embeddings generados por futuros modelos.
- Errores de conectividad con el proveedor.
- Configuración incorrecta del modelo o de las credenciales.

La arquitectura propuesta reduce estos riesgos mediante la separación entre el módulo Embeddings y el proveedor de IA, permitiendo sustituir el proveedor con un impacto mínimo sobre el resto del pipeline.

---

# 23. Estado de implementación

| Implementación | Estado | RF |
|---------------|--------|----|
| IMP-01 | ✅ | Diseño de la arquitectura del módulo |
| IMP-02 | ✅ | Creación de la estructura base |
| IMP-03 | ✅ | Integración del proveedor de embeddings |
| IMP-04 | ✅ | RF-040 |
| IMP-05 | ✅ | RF-041, RF-042 |
| IMP-06 | ✅ | RF-043 |
| IMP-07 | ✅ | RF-044, RF-045 |
| IMP-08 | ✅ | Scripts de validación (temp/) |
| IMP-09 | ⏳ | Pruebas automatizadas (tests/) |
| IMP-10 | ⏳ | Documentación y preparación de Release |

---

# 24. Resultados de implementación

La validación de integración del módulo Embeddings fue ejecutada satisfactoriamente utilizando el script:

temp/check_pipeline_embeddings.py

Resultados obtenidos:

- Document Loader: OK
- Text Splitter: OK
- Metadata Manager: OK
- Embeddings: OK

Se verificó la generación de embeddings mediante Google Generative AI.

Modelo utilizado:

gemini-embedding-2

Dimensión del embedding generado:

3072

La prueba se ejecutó utilizando una muestra reducida de documentos para respetar las limitaciones de cuota del servicio gratuito.


---

# 25. Control de versiones

| Versión | Fecha | Autor | Cambios |
|----------|--------|--------|----------|
| 1.0 | 03/07/2026 | Jacqueline Rioja | Creación inicial del documento SDS-004 correspondiente al módulo Embeddings. |
| 1.1 | 04/07/2026 | Jacqueline Rioja | Actualización posterior a la implementación del módulo Embeddings. Se documenta la integración con Google Generative AI, la validación del pipeline RAG y las consideraciones sobre el uso de la cuota gratuita. |


