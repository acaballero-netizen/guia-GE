# Guía de tono y estilo · Proyecto MADERAMEN
## Autoconstrucción sostenible en Guinea Ecuatorial

---

## 1. Contexto de uso

Los contenidos de este proyecto están destinados a ser consultados a través de un código QR que enlaza a una web. El público lector es diverso y no necesariamente tiene formación técnica:

- Comunidades locales de la etnia fang
- Carpinteros y constructores locales con saber práctico empírico
- Estudiantes de arquitectura de la UNGE y AAUCA
- Técnicos e investigadores del equipo

El contenido debe funcionar para todos estos perfiles simultáneamente: accesible para quien no tiene formación técnica, pero riguroso para quien sí la tiene. La claridad es prioritaria sobre la exhaustividad.

---

## 2. Registro y tono

El texto tiene un registro **técnico-divulgativo**: preciso en los datos, comprensible sin formación especializada. Se explica con claridad sin presuponer conocimientos previos.

- Cuando aparece un término técnico, se define en la misma frase o en la frase siguiente.
- Las frases son cortas y directas.
- El texto es impersonal y descriptivo, como una entrada de wiki o un manual de referencia. No aparecen pronombres de segunda persona ("tú", "usted") ni referencias a interlocutores.

**Reformulaciones de referencia:**

| Evitar | Usar |
|---|---|
| "Tienes que nivelar el terreno antes de excavar" | "El terreno se nivela antes de excavar." |
| "Debes asegurarte de que no haya burbujas" | "La manguera no debe contener burbujas de aire." |
| "Os recomendamos usar madera local" | "Se recomienda el uso de madera local." |
| "Como comentabas, el bloque de hormigón..." | "El bloque de hormigón..." |

---

## 3. Estructura del contenido

Cada sección de la guía sigue esta estructura:

```
## Nombre del paso o elemento constructivo

Introducción breve: qué es, para qué sirve, por qué es importante.

### Materiales

Lista de materiales. Cuando existe una alternativa local viable,
se indica entre paréntesis o en una línea de nota.

### Paso a paso

Secuencia numerada. Cada paso que introduce un elemento nuevo
o una acción espacial va acompañado de un bloque de imagen (ver apartado 4).

### A tener en cuenta

Avisos, errores frecuentes, condiciones especiales del clima o del terreno.
```

**Sobre la longitud:** no hay un límite fijo por sección, ya que algunas partes del proceso (como la cimentación) requieren más desarrollo que otras. Cuando una sección crece mucho, es preferible dividirla en subsecciones con título propio antes que comprimirla y perder claridad.

**Sobre los materiales:** la lista es única por sección. Cuando un material tiene una alternativa local o de menor coste, se indica de forma simple:

```markdown
- Manguera transparente de al menos 10 m *(alternativa: tubo de PVC fino translúcido)*
- Pisón manual *(puede fabricarse con un tronco pesado y dos palos como mangos)*
```

---

## 4. Imágenes

### 4.1 Cuándo incluir una imagen

Se incluye una imagen en cada paso que:

- Introduce un nuevo elemento constructivo
- Describe una acción con componente espacial o gestual
- Implica medidas, disposición de piezas o relaciones entre partes

En la práctica, la mayoría de pasos de la sección "Paso a paso" llevarán imagen. El criterio es: si alguien que no ha visto nunca ese proceso puede entender el paso solo con el texto, no es necesaria; si necesita ver cómo queda, sí lo es.

### 4.2 Estilo visual

Las ilustraciones siguen un estilo de **dibujo técnico a mano con trazos limpios**, en escala de grises. El elemento constructivo que se añade o que tiene mayor relevancia en ese paso se remarca en rojo.

<!-- TODO: Adjuntar imagen de referencia de estilo cuando esté disponible para completar el prompt base. -->

### 4.3 Prompt base de imagen

Cuando esté definida la imagen de referencia de estilo, se establecerá un prompt base que fije el lenguaje visual del proyecto. Cada imagen concreta heredará ese prompt base y añadirá únicamente la descripción de lo que hay que mostrar en ese paso.

Estructura prevista:

```
[PROMPT BASE · estilo visual fijo del proyecto]
+ [descripción específica del paso: qué se muestra, desde qué ángulo, qué elemento va en rojo]
```

<!-- TODO: Redactar el prompt base en cuanto se disponga de la imagen de referencia. -->

### 4.4 Cómo se marca en el documento

Hasta que el flujo de generación de imágenes esté definido, cada imagen se indica con el siguiente comentario en el punto exacto donde debe aparecer:

```markdown
<!-- PROMPT: Esta imagen tiene que representar [qué se muestra · desde qué ángulo · qué elemento va remarcado en rojo · contexto visual]. -->
```

**Ejemplo:**

```markdown
<!-- PROMPT: Esta imagen tiene que representar dos personas trabajando con una manguera transparente para nivelar estacas en un solar de tierra. Una persona sostiene un extremo a la altura de una marca en la estaca maestra. La otra, a unos 6 metros, marca su estaca donde el agua se detiene. La manguera va remarcada en rojo. Vista lateral, entorno tropical, luz de mediodía. Dibujo técnico a mano, escala de grises. -->
```

### 4.5 Lo que no se usa

- No se insertan diagramas con letras, flechas o símbolos generados en texto
- No se usan caracteres ASCII para representar secciones o geometrías
- No se usan tablas para representar relaciones espaciales

---

## 5. Tareas pendientes

Las tareas pendientes se marcan con el siguiente comentario en el punto del documento donde son relevantes:

```markdown
<!-- TODO: [descripción de la tarea] -->
```

Los TODO se van añadiendo a lo largo del texto a medida que surgen. Periódicamente se puede pedir a la IA que los recoja todos en orden y los exporte como lista con casillas de seguimiento.

---

## 6. Instrucciones internas para la IA

Antes de entregar cualquier sección, la IA verifica internamente los siguientes puntos. Esta lista no aparece en el documento generado:

- [ ] El texto no contiene pronombres de segunda persona ni referencias a personas concretas
- [ ] Los términos técnicos están explicados en la misma frase en que aparecen
- [ ] La lista de materiales incluye alternativas locales donde las hay
- [ ] Cada paso con componente espacial o gestual tiene un bloque `<!-- PROMPT: -->`
- [ ] No hay diagramas, tablas espaciales ni ASCII en el texto
- [ ] Las tareas pendientes están marcadas con `<!-- TODO: -->`
- [ ] El contenido es claro para alguien sin formación técnica

---

*Borrador · Mayo 2025 · Pendiente de validación por el equipo técnico*