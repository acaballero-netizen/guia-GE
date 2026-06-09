# Sistema de prompts de imagen
## Proyecto MADERAMEN · Autoconstrucción sostenible en Guinea Ecuatorial

Este documento complementa `criterio_grafico.md` y define cómo redactar los prompts particulares de cada imagen. El criterio gráfico define el estilo visual. Este documento define cómo describir el contenido concreto de cada viñeta.

---

## El problema que resuelve este documento

El prompt base ya cubre el estilo: escala de grises, trazos a mano, acuarela, paleta, formato 1:1, sin texto, sin flechas. Repetir esas instrucciones en cada prompt particular añade ruido sin aportar información nueva.

Lo que el generador no puede inferir son tres cosas que solo el redactor conoce:

- El encuadre exacto: qué entra en el cuadrado y qué queda fuera.
- El estado preciso del proceso: en qué momento del paso está la imagen.
- Qué es el rojo: con suficiente detalle para que no haya ambigüedad.

El prompt particular solo debe añadir lo que el prompt base no puede saber.

---

## Lo que el prompt particular NO debe incluir

Todo lo que ya está en el prompt base:

- Escala de grises, paleta de color, uso del rojo
- Trazos a mano, acuarela, irregularidad natural
- Formato cuadrado 1:1
- Sin texto, sin flechas, sin rótulos dentro de la imagen
- Representación de personas con rasgos de Guinea Ecuatorial

---

## Lo que el prompt particular SÍ debe especificar

### 1. Punto de vista y encuadre

No basta con "sección transversal" o "perspectiva". Hay que decir desde dónde se mira y qué ocupa el cuadro.

- *"Sección transversal centrada en la junta entre dos tablas. El cuadro muestra aproximadamente 30 cm de ancho y 20 cm de alto."*
- *"Vista frontal desde 1 metro de distancia. Aparecen dos manos y la herramienta. Nada más."*

### 2. El estado exacto del proceso

El generador no sabe en qué momento del paso está la imagen.

| Evitar | Usar |
|---|---|
| "Una persona dobla una varilla" | "La varilla ya está doblada en L. Se ve el resultado: el tubo metálico todavía en la mano, el ángulo de 90° ya formado. No hay acción en curso." |
| "Se colocan bloques sobre el mortero" | "El primer bloque de esquina está colocado. El nivel de burbuja apoya encima. La mano izquierda sujeta el nivel; la derecha no aparece." |

### 3. El elemento rojo: qué es, dónde está, cuánto ocupa

| Evitar | Usar |
|---|---|
| "La espera vertical remarcada en rojo" | "La espera vertical que sobresale por encima del bloque: solo la porción que asoma, unos 15 cm. El resto de la varilla, dentro del bloque, va en gris." |
| "Los clavos en diagonal remarcados en rojo" | "Los dos clavos ya clavados en diagonal en la cara del montante. Las cabezas de los clavos y los últimos 3 cm de caña visible son el único rojo." |

### 4. Lo que debe quedar fuera o simplificarse

Si el contexto es complejo, indicar qué no se muestra.

- *"El resto de la zapata no aparece. Solo el extremo de la zanja con la capa de limpieza."*
- *"No hay entorno. Solo el tarro, centrado, sin manos ni superficie de apoyo."*

---

## Plantilla

```
<!-- PROMPT:
ENCUADRE: [punto de vista · distancia aproximada · qué entra en el cuadro]
ESTADO: [qué ha pasado ya / qué está pasando / qué resultado se ve]
ROJO: [nombre exacto del elemento · qué parte concreta · cuánto ocupa en el cuadro]
SIMPLIFICAR: [qué queda fuera o se muestra esquemático]
-->
```

---

## Ejemplos comparativos

### Prueba del tarro (paso0 · análisis de suelo)

**Antes:**
```
<!-- PROMPT: Esta imagen tiene que representar un tarro de vidrio transparente con agua
y tierra en reposo, mostrando claramente tres capas de sedimento diferenciadas: grava
y arena gruesa en el fondo, arena fina en el medio, y arcilla y limo en la parte superior,
con una capa de agua turbia o clara encima. Se indica con flechas o cotas en rojo
el nombre de cada capa y su grosor relativo. Dibujo técnico a mano alzada, escala
de grises, las cotas de las capas remarcadas en rojo. Vista frontal del tarro. -->
```

**Después:**
```
<!-- PROMPT:
ENCUADRE: Vista frontal de un tarro de vidrio cilíndrico de tamaño mediano.
El tarro ocupa casi todo el cuadro, centrado, con algo de espacio arriba y abajo.
ESTADO: El sedimento lleva 24 horas reposando. Las capas ya están completamente
formadas y el agua superior está casi clara. De abajo a arriba: capa gruesa de
grava y arena (~40% del sedimento), capa media de arena fina (~35%), capa fina
de arcilla y limo (~25%). La tapa está quitada.
ROJO: Las dos líneas horizontales que separan las tres capas entre sí. Solo las
líneas de separación, no las capas completas.
SIMPLIFICAR: No hay manos ni entorno. Solo el tarro.
-->
```

---

### Compactación con pisón (paso0 · nivelación)

**Antes:** sin prompt (paso no ilustrado).

**Después:**
```
<!-- PROMPT:
ENCUADRE: Vista lateral a media altura. Se ven dos piernas desde la rodilla
hacia abajo y el pisón en acción. El cuadro muestra unos 60 cm de ancho.
ESTADO: El pisón acaba de golpear la capa de tierra. El operario tiene el peso
del cuerpo cargado sobre el pisón en el momento del impacto. La tierra de
alrededor está ya compactada; solo la zona bajo el pisón muestra tierra suelta.
ROJO: El pisón completo: el tronco vertical y los dos palos transversales
que hacen de mangos.
SIMPLIFICAR: No se muestra el solar completo. Solo el suelo inmediato
y las piernas. El pie de la persona va descalzo.
-->
```

---

### Doblar varilla en L (paso1 · fundación)

**Antes:**
```
<!-- PROMPT: Esta imagen tiene que representar la operación de doblar una varilla
de acero corrugado en forma de "L" usando un tubo metálico hueco como palanca.
Se ven las manos sujetando el tubo, la varilla atravesándolo y el ángulo de 90°
resultante. El tubo y el ángulo formado están remarcados en rojo. Vista en
perspectiva, dibujo técnico a mano alzada, escala de grises. -->
```

**Después:**
```
<!-- PROMPT:
ENCUADRE: Vista en perspectiva a la altura de la cintura. El cuadro muestra
las dos manos, el tubo metálico y el extremo doblado de la varilla.
ESTADO: La operación ha terminado. La varilla ya tiene el ángulo de 90°.
El tubo metálico sigue en la mano derecha, que empuja hacia abajo.
La mano izquierda sujeta la varilla horizontal para que no se mueva.
ROJO: El codo de la varilla: el punto exacto donde se forma el ángulo de 90°,
unos 5 cm a cada lado de la curva.
SIMPLIFICAR: No se muestra el suelo ni el contexto de obra. Solo las manos,
el tubo y el extremo de la varilla.
-->
```

---

## Dónde vive este documento

Este archivo va en `contexto/` junto con `criterio_grafico.md` y `tono_estilo.md`.
Es un documento de uso interno del equipo: no forma parte de la guía que
consultan las comunidades.

---

## Relación con otros documentos

- `criterio_grafico.md` — define el estilo visual y el prompt base. Leer antes de generar cualquier imagen.
- `tono_estilo.md` — define cómo marcar los prompts en el documento Markdown (`<!-- PROMPT: -->`).
- Este documento — define cómo redactar el contenido de cada prompt particular.

---

*Borrador · Mayo 2025 · Pendiente de validación por el equipo*
