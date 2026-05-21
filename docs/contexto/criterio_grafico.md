# Criterio gráfico · Ilustraciones de la guía
## Proyecto MADERAMEN · Autoconstrucción sostenible en Guinea Ecuatorial

Este documento define el estilo visual de todas las ilustraciones de la guía y contiene el prompt base que debe cargarse en el Gem antes de generar cualquier imagen. Su objetivo es garantizar coherencia visual entre todas las imágenes, independientemente de cuándo o por quién se generen.

---

## 1. Concepto visual

Las ilustraciones siguen el modelo de un **manual técnico dibujado a mano**. El referente es doble: la cercanía y legibilidad de guías como *The Barefoot Architect* de Johan van Lengen, y la secuencialidad paso a paso de los manuales de montaje de Ikea. El resultado es un dibujo que parece hecho a mano, con trazos limpios pero no perfectos, que cualquier persona puede entender sin formación técnica.

Cada imagen muestra **un único paso**. No hay viñetas compuestas ni secuencias dentro de una misma imagen. La secuencia la construye el documento, no la ilustración.

---

## 2. Formato

- **Proporción:** cuadrada, 1:1. El sujeto principal llena el encuadre — no se deja espacio vacío decorativo alrededor.
- **Fondo:** blanco puro `#ffffff`, sin textura de papel, sin márgenes de color, sin bordes.
- **Sin texto dentro de la imagen.** Ninguna medida, etiqueta, cota, flecha ni número aparece dentro del cuadro. Las explicaciones y medidas van siempre en el documento Markdown. La imagen comunica únicamente a través de geometría, posición y contraste.

---

## 3. Paleta de color

La paleta es intencionalmente mínima.

### Grises · toda la ilustración

| Nombre   | Hex       | Uso                                                  |
|----------|-----------|------------------------------------------------------|
| Trazo    | `#1c1c1c` | Contornos, líneas de trazo, bordes de todos los elementos |
| Sombra   | `#5a5a5a` | Sombras proyectadas, profundidad, piel de personas, acuarela oscura |
| Relleno  | `#b0b0b0` | Relleno de superficies, acuarela media               |
| Claro    | `#e0e0e0` | Rellenos ligeros, zonas en segundo plano             |
| Fondo    | `#ffffff` | Fondo de la imagen, siempre blanco puro              |

### Rojo · un único uso por imagen

| Nombre           | Hex       | Uso                                      |
|------------------|-----------|------------------------------------------|
| Rojo MADERAMEN   | `#dc2f39` | El único elemento nuevo o más relevante del paso |

**Regla absoluta:** el rojo aparece **una sola vez por imagen**, en el único elemento que es nuevo en ese paso. Todo lo demás va en grises. Si en un paso hay varios elementos nuevos, se elige el más relevante para remarcar en rojo. El rojo nunca se usa para flechas, cotas, etiquetas ni cualquier elemento que no sea la geometría del objeto principal.

---

## 4. Estilo de trazo y técnica

- Trazo a mano, con ligera irregularidad natural. No debe parecer generado por ordenador ni perfectamente geométrico.
- Grosor de trazo uniforme y visible, suficientemente grueso para leerse en pantalla de móvil.
- Las superficies se rellenan con acuarela suelta en los grises de la paleta, con variación de densidad para dar volumen. No hay rellenos planos y uniformes.
- Las sombras proyectadas son ligeras, en gris medio, sin efectos de desenfoque ni gradientes digitales.
- El espacio vacío dentro del encuadre es siempre fondo blanco. Nunca se rellena con elementos decorativos, vegetación, texturas de suelo ni patrones.

---

## 5. Punto de vista

Cada viñeta usa el punto de vista que mejor explica ese paso concreto. Los más habituales son:

- **Perspectiva axonométrica o isométrica:** para mostrar conjuntos constructivos y relaciones entre elementos. Es el punto de vista más frecuente.
- **Sección transversal:** para mostrar el interior de un elemento (zapata, solape de tablas, unión de piezas).
- **Detalle en perspectiva:** para mostrar una unión, un nudo o una acción manual con precisión.
- **Vista en planta:** para mostrar distribuciones, replanteos o relaciones entre ejes.

El punto de vista se especifica en cada `<!-- PROMPT: -->` del documento Markdown.

---

## 6. Representación de personas

Cuando aparecen personas en la ilustración, se representan con rasgos físicos propios de la población de Guinea Ecuatorial ecuatorial africana. La piel se resuelve con acuarela en gris oscuro `#5a5a5a`, nunca blanca. Las figuras son simplificadas pero reconocibles — no son cartoons ni retratos. La ropa es sencilla y sin detalle decorativo.

---

## 7. Imágenes de referencia de estilo

Las imágenes de referencia se cargan de forma fija en el Gem. Su función es anclar el estilo visual antes de cualquier generación. No es necesario describirlas en el prompt individual.

### Cuántas y de qué tipo

El set de referencia debe cubrir los **cuatro tipos de encuadre** que aparecen en la guía. Un set incompleto hace que el modelo improvise en los tipos no cubiertos, generando inconsistencias.

| Tipo de encuadre | Descripción | ¿Cubierto? |
|---|---|---|
| Axonométrica con elementos constructivos | Escenas de obra sin personas: zanja, armadura, bloques, cerchas | ✅ Cubierto (imágenes existentes) |
| Sección transversal | Corte interior de un elemento: zapata, solape de tablas, detalle de unión | ⬜ Pendiente |
| Detalle con manos | Primer plano de manos usando una herramienta o manipulando un elemento | ⬜ Pendiente |
| Vista en planta | Replanteo, distribución, relaciones entre ejes vistas desde arriba | ⬜ Pendiente |

**Número recomendado:** 4 a 6 imágenes en total, una por tipo de encuadre. Más de 6 genera ruido y el modelo pierde sharpness al promediar entre demasiadas referencias. Las 2–3 imágenes existentes cubren el tipo axonométrico — se necesitan 2–3 más para los tipos pendientes.

### Cómo generar las referencias que faltan

Para cada tipo pendiente, usar el prompt base (sección 8) más una descripción mínima de una escena representativa del tipo. Generar, evaluar, y si el resultado es correcto, añadirlo al Gem como referencia fija. No hace falta que la escena de referencia sea una imagen real de la guía — puede ser cualquier elemento constructivo simple del mismo tipo de encuadre.

---

## 8. BASE PROMPT — Instrucciones fijas del Gem

El siguiente bloque es el prompt base en inglés. Se carga íntegro en las instrucciones fijas del Gem, antes de cualquier prompt individual. No se modifica entre imágenes.

---

```
MADERAMEN ILLUSTRATION SYSTEM — BASE INSTRUCTIONS

You are a technical manual illustrator. Every image you generate follows these rules exactly. These rules override any conflicting tendency from your training.

---

MEDIUM AND RENDERING

The image is a hand-drawn technical illustration. The only media present are:
- Graphite lines on white paper: slightly irregular, with natural variation in weight, never perfectly geometric or computer-generated in appearance.
- Transparent watercolor washes in grey tones: loose, with visible water edges and brushstroke variation that shows a human hand.

No digital effects of any kind: no gradients, no drop shadows, no blur, no glow, no filters. The result looks like it was drawn and painted by a skilled illustrator working from a construction site.

---

PALETTE

Strictly greyscale except for one element:
- Graphite lines: #1c1c1c
- Dark watercolor (depth, shadow, human skin): #5a5a5a
- Mid watercolor (surfaces, fills): #b0b0b0
- Light watercolor (background elements, secondary): #e0e0e0
- Background: pure white #ffffff — no paper texture, no off-white, no grain

The one exception: a single element per image is rendered in solid red #dc2f39 with heavier graphite outlines. This is the primary element — the one that is new or most important in this step. Everything else is grey.

---

HIERARCHY

Secondary elements — context, surrounding structure, ground — are rendered with thin graphite lines and very light, near-transparent watercolor washes. They exist to give spatial context but do not compete for attention. They recede.

The primary element — marked in red #dc2f39 — is drawn with heavier, more defined graphite lines and filled with solid red. It commands the image. There is exactly one primary element per image.

---

COMPOSITION AND FRAME

The subject fills the square frame. Empty space inside the frame is pure white background — never filled with decorative elements, vegetation, textures, patterns, or any invented context.

Format: square, 1:1 ratio.

---

ABSOLUTE CONSTRAINTS — NEVER VIOLATE THESE

1. No text of any kind inside the image. No measurements, no labels, no numbers, no dimension marks, no annotations. If the prompt mentions a measurement (e.g. "3 m", "60 cm"), that measurement describes the geometry to draw — it is never rendered as text.

2. Red appears exactly once per image, on exactly one element. Never on arrows, never on dimension lines, never on more than one object.

3. No decorative fill. Empty areas are white. No tropical plants, no botanical borders, no invented background elements unless explicitly described in the individual prompt.

4. No paper texture. Background is pure white #ffffff.

5. No digital effects. No gradients, no blur, no drop shadows.

---

PEOPLE

When people appear, they have the physical features of equatorial African people from Guinea. Skin is rendered with dark grey watercolor wash #5a5a5a, never left white. Figures are simplified but recognizable — not cartoons, not portraits. Clothing is plain with no decorative detail. It should be randomly chose between male or female.

---

SHOT TYPE

The shot type (axonometric, section, close-up detail, plan view) and the exact framing are always specified in the individual prompt. Never assume a shot type. Never add elements not described in the individual prompt.
```

---

## 9. Cómo usar el prompt base con el prompt individual

El prompt base ya está cargado en el Gem. El prompt individual **no debe repetir ninguna instrucción del base**: ni la paleta, ni el estilo, ni las restricciones. Solo añade lo que el base no puede saber:

1. El tipo de encuadre y la distancia aproximada
2. El estado exacto del proceso en el momento de la imagen
3. Qué elemento es el rojo y qué parte concreta de ese elemento
4. Qué queda fuera o se simplifica

El formato de los prompts individuales se define en `criterio_prompts_imagen.md`.

---

## 10. Lo que no se usa

- Sin texto, números ni flechas dentro de la imagen
- Sin fondos de color, marcos ni bordes decorativos
- Sin efectos digitales: sin degradados, sin sombras difusas, sin desenfoque
- Sin más de un elemento en rojo por imagen
- Sin colores adicionales fuera de la paleta definida
- Sin vegetación decorativa ni elementos de contexto no descritos en el prompt individual

---

*Revisado · Mayo 2025 · Pendiente de validación por el equipo técnico*
