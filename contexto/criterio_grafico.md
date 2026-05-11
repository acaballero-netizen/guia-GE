# Criterio gráfico · Ilustraciones de la guía
## Proyecto MADERAMEN · Autoconstrucción sostenible en Guinea Ecuatorial

Este documento define el estilo visual de todas las ilustraciones de la guía. Su objetivo es garantizar que todas las imágenes tengan coherencia entre sí, independientemente de cuándo o con qué herramienta se generen.

---

## 1. Concepto visual

Las ilustraciones siguen el modelo de un **manual técnico a mano**. El referente es doble: la cercanía y legibilidad de guías como *The Barefoot Architect* de Johan van Lengen, y la secuencialidad paso a paso de los manuales de montaje de Ikea. El resultado es un dibujo que parece hecho a mano, con trazos limpios pero no perfectos, que cualquier persona puede entender sin formación técnica.

Cada imagen muestra **un único paso**. No hay viñetas compuestas ni secuencias dentro de una misma imagen. La secuencia la construye el documento, no la ilustración.

---

## 2. Formato

- **Proporción:** cuadrada, 1:1
- **Fondo:** blanco puro, sin textura de papel ni márgenes de color
- **Sin texto dentro de la imagen.** Los títulos y explicaciones van en el documento Markdown. Las ilustraciones funcionan solas, sin rótulos ni leyendas.

---

## 3. Paleta de color

La paleta es intencionalmente mínima. Menos colores significa más coherencia y más fuerza para el rojo.

### Grises · toda la ilustración

| Nombre | Hex | Uso |
|---|---|---|
| Trazo | `#1c1c1c` | Contornos, líneas de trazo, bordes de todos los elementos |
| Sombra | `#5a5a5a` | Sombras proyectadas, profundidad, acuarela oscura |
| Relleno | `#b0b0b0` | Relleno de superficies, acuarela media |
| Claro | `#e0e0e0` | Rellenos ligeros, zonas en segundo plano |
| Fondo | `#ffffff` | Fondo de la imagen, siempre blanco puro |

### Rojo · un único uso

| Nombre | Hex | Uso |
|---|---|---|
| Rojo MADERAMEN | `#dc2f39` | El elemento que se incorpora en ese paso |

**Regla absoluta:** el rojo aparece **una sola vez por imagen**, en el único elemento que es nuevo en ese paso. Todo lo demás va en grises. Si en un paso hay varios elementos nuevos, se elige el más relevante para remarcar en rojo.

---

## 4. Estilo de trazo

- Trazo a mano, con ligera irregularidad natural. No debe parecer generado por ordenador ni perfectamente geométrico.
- Grosor de trazo uniforme y visible, suficientemente grueso para leerse en pantalla de móvil.
- Las superficies se rellenan con acuarela suelta en los grises de la paleta, con variación de densidad para dar volumen. No hay rellenos planos y uniformes.
- Las sombras proyectadas son ligeras, en gris medio, sin efectos de desenfoque.

---

## 5. Punto de vista

Cada viñeta usa el punto de vista que mejor explica ese paso concreto. Los más habituales son:

- **Perspectiva axonométrica o isométrica:** para mostrar conjuntos constructivos y relaciones entre elementos. Es el punto de vista más frecuente.
- **Sección transversal:** para mostrar el interior de un elemento (zapata, solape de tablas, unión de piezas).
- **Detalle en perspectiva:** para mostrar una unión, un nudo o una acción manual con precisión.

El punto de vista se especifica en cada `<!-- PROMPT: -->` del documento Markdown.

---

## 6. Prompt base

El siguiente prompt base debe incluirse al inicio de cada prompt específico. Define el estilo visual fijo del proyecto. A continuación se añade únicamente la descripción de lo que hay que mostrar en ese paso.

```
Ilustración técnica a mano para una guía de autoconstrucción. Estilo de dibujo manual con trazos limpios pero con ligera irregularidad natural, similar a The Barefoot Architect. Escala de grises: trazo en #1c1c1c, sombras en #5a5a5a, rellenos en #b0b0b0 y #e0e0e0, fondo blanco puro #ffffff. Acuarela suelta en grises para dar volumen a las superficies. El único elemento en color es [ELEMENTO], remarcado en rojo #dc2f39. Sin texto, sin rótulos, sin leyendas dentro de la imagen. Formato cuadrado 1:1. [PUNTO DE VISTA: perspectiva axonométrica / sección transversal / detalle en perspectiva].
```

**Cómo usar el prompt base:**

1. Copiar el bloque completo.
2. Sustituir `[ELEMENTO]` por el nombre del elemento nuevo que aparece en ese paso.
3. Sustituir `[PUNTO DE VISTA]` por el que corresponda y eliminar las otras opciones.
4. Añadir a continuación la descripción específica del paso, copiada del `<!-- PROMPT: -->` del documento Markdown.

**Ejemplo completo:**

```
Ilustración técnica a mano para una guía de autoconstrucción. Estilo de dibujo manual con trazos limpios pero con ligera irregularidad natural, similar a The Barefoot Architect. Escala de grises: trazo en #1c1c1c, sombras en #5a5a5a, rellenos en #b0b0b0 y #e0e0e0, fondo blanco puro #ffffff. Acuarela suelta en grises para dar volumen a las superficies. El único elemento en color es la varilla de espera vertical, remarcada en rojo #dc2f39. Sin texto, sin rótulos, sin leyendas dentro de la imagen. Formato cuadrado 1:1. Perspectiva axonométrica.

La imagen muestra una zanja de cimentación excavada en el terreno, vista en perspectiva axonométrica. En el interior de la zanja se ve la parrilla de armadura horizontal apoyada sobre calzos, en grises. Tres varillas verticales sobresalen hacia arriba desde la parrilla, remarcadas en rojo. El terreno que rodea la zanja se representa con acuarela suelta en gris oscuro.
```

<!-- TODO: Cuando se disponga de una imagen de referencia generada y validada por el equipo, adjuntarla aquí como ejemplo visual del estilo conseguido. -->

---

## 7. Lo que no se usa

- Sin texto, números ni flechas dentro de la imagen
- Sin fondos de color, marcos ni bordes decorativos
- Sin efectos digitales: sin degradados, sin sombras difusas, sin desenfoque
- Sin más de un elemento en rojo por imagen
- Sin colores adicionales fuera de la paleta definida

---

*Borrador · Mayo 2025 · Pendiente de validación por el equipo técnico*