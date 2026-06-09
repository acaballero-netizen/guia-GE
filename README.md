# README · Proyecto MADERAMEN
## Guía práctica de autoconstrucción en Guinea Ecuatorial

Este documento es el punto de entrada del repositorio. Define qué es el proyecto, qué contiene cada archivo y cómo debe actuar el asistente de IA en cada tipo de tarea.

---

## Qué es este proyecto

Una guía visual de autoconstrucción para comunidades de Guinea Ecuatorial, orientada a que cualquier persona —sin formación técnica especializada— pueda entender cómo construir una vivienda segura y digna utilizando materiales y técnicas locales. El referente visual son los manuales de Ikea: las imágenes son las protagonistas, el texto complementa y amplía cuando hace falta.

El proyecto está impulsado por la Cátedra MADERAMEN de la Universitat Politècnica de València (UPV), en el marco del programa ADSIDEO Cooperación 2024, en colaboración con la UNGE, la AAUCA, Arquitectura Sin Fronteras y REMAR Guinea Ecuatorial.

---

## A quién va dirigido

El público principal son personas sin formación técnica: familias de comunidades fang, carpinteros locales con saber empírico, y cualquier persona que quiera construir o mejorar su vivienda en Guinea Ecuatorial continental. La guía también es útil para estudiantes de arquitectura de la UNGE y la AAUCA, y para técnicos e investigadores del equipo.

Esto tiene una consecuencia directa en todo el contenido: **la claridad siempre por encima de la exhaustividad**. Si algo no se puede explicar de forma sencilla, hay que buscar otra forma de explicarlo.

---

## Estructura del repositorio

```
/contexto
    README.md               → este documento
    memoria_ADSIDEO.md      → contexto y objetivos del proyecto de investigación
    documento_diagnostico.md → diagnóstico de técnicas constructivas en Guinea Ecuatorial
    tono_estilo.md          → cómo se escribe: registro, estructura, convenciones
    outline.md              → índice completo de la guía y listado de imágenes necesarias
    criterio_grafico.md     → cómo se ilustra: paleta, estilo, prompt base

/docs
    paso00_criterios_de_diseño.md  → Criterios de diseño
    paso01_pasos_previos.md        → Pasos previos: limpieza, nivelación y replanteo
    paso02_cimentacion.md          → fundación: zapata corrida y zócalo
    paso03_cerramiento.md          → Cerramiento: paramentos verticales de madera
    paso04_cubierta.md             → Cubierta: estructura de cerchas y chapa
    paso05_carpinterias.md         → Carpintería y particiones interiores
    paso06_instalaciones.md        → Instalaciones
    paso99_mantemiento.md          → Mantenimiento
```

---

## Documentos de referencia · para qué sirve cada uno

Antes de generar cualquier contenido, el asistente debe conocer estos documentos. Si alguno no está disponible en el contexto, solicitarlo antes de continuar.

| Documento | Cuándo consultarlo |
|---|---|
| `memoria_ADSIDEO.md` | Para entender el contexto del proyecto, sus objetivos, actores y fases |
| `documento_diagnostico.md` | Para cualquier pregunta sobre materiales, técnicas o condiciones locales de Guinea Ecuatorial |
| `tono_estilo.md` | Antes de redactar cualquier sección de la guía |
| `outline.md` | Para saber en qué punto de la guía se está trabajando y qué viene antes y después |
| `criterio_grafico.md` | Antes de escribir cualquier `<!-- PROMPT: -->` de imagen |

---

## Cómo actúa el asistente según el tipo de tarea

### Redactar una sección de la guía

1. Consultar `outline.md` para situar la sección en el conjunto.
2. Consultar `tono_estilo.md` para aplicar el registro, la estructura y las convenciones.
3. Consultar `documento_diagnostico.md` y `memoria_ADSIDEO.md` si la sección implica materiales, técnicas o condiciones locales.
4. Redactar siguiendo la estructura: introducción breve → materiales (con alternativas locales donde las haya) → paso a paso → a tener en cuenta.
5. Incluir un `<!-- PROMPT: -->` en cada paso que introduce un elemento constructivo nuevo o una acción con componente espacial.
6. Marcar con `<!-- TODO: -->` cualquier laguna de información que no pueda resolverse sin trabajo de campo o validación técnica.
7. Antes de entregar, verificar internamente el checklist de `tono_estilo.md` (apartado 6). Este checklist no aparece en el documento generado.

### Escribir un prompt de imagen

1. Consultar `criterio_grafico.md` para aplicar el prompt base y la paleta.
2. Identificar el elemento nuevo del paso (el que va en rojo).
3. Determinar el punto de vista más adecuado: perspectiva axonométrica, sección transversal o detalle en perspectiva.
4. Construir el prompt completo: prompt base + descripción específica del paso.
5. El prompt se inserta como comentario `<!-- PROMPT: -->` en el punto exacto del documento donde debe aparecer la imagen.

### Responder una consulta técnica del equipo

- Si la respuesta está en los documentos del repositorio, priorizarla sobre el conocimiento general.
- Si no está, responder con conocimiento general señalando explícitamente que debe verificarse en campo o incorporarse al repositorio.
- Las recomendaciones estructurales o de seguridad siempre se señalan como pendientes de validación por el equipo técnico antes de incorporarse a la guía definitiva.

### Recopilar los TODO del repositorio

Cuando se solicite, recorrer todos los documentos disponibles y exportar todos los `<!-- TODO: -->` en orden, con el nombre del documento y el número de línea aproximado, formateados como lista con casillas de seguimiento:

```markdown
- [ ] `tono_estilo.md` · Redactar el prompt base cuando se disponga de imagen de referencia.
- [ ] `criterio_grafico.md` · Adjuntar imagen validada como ejemplo visual del estilo.
```

---

## Principios que rigen todo el contenido

Estos principios están desarrollados en `memoria_ADSIDEO.md` y se aplican a cualquier decisión de contenido:

- **Autoconstrucción como marco.** Todo lo que se proponga debe poder ejecutarse sin maquinaria especializada, por personas sin titulación técnica, con materiales disponibles localmente.
- **Madera como protagonista.** Es el material más abundante, culturalmente integrado y viable en el contexto. Las propuestas lo priorizan en estructura y cubierta.
- **Sencillez ante todo.** Tanto en el texto como en las imágenes. Si algo puede simplificarse sin perder rigor, se simplifica.
- **Respeto cultural.** Las soluciones deben ser aceptables para las comunidades fang y co-creadas con ellas, no impuestas desde fuera.
- **Mínimos dignos.** El objetivo no es la perfección técnica sino garantizar seguridad estructural, salubridad y confort básico adaptado al clima ecuatorial.

---

## Limitaciones que el asistente señala siempre

- No reemplaza la observación directa de campo ni el juicio de los técnicos locales.
- Cualquier recomendación estructural o de seguridad debe ser validada por el equipo técnico antes de incorporarse a la versión definitiva de la guía.
- Si falta información de campo para responder bien una pregunta, lo indica explícitamente y sugiere qué dato o fuente resolvería la laguna.

---

<!-- TODO: Actualizar la estructura del repositorio cuando se añadan nuevas secciones de la guía. -->
<!-- TODO: Añadir enlace al repositorio GitHub cuando esté disponible públicamente. -->

---

*Borrador · Mayo 2026 · Pendiente de validación por el equipo técnico*