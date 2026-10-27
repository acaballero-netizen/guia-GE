# Web de la Cátedra MADERAMEN

Repositorio de la web publicada en **maderamen.calab.es** (GitHub Pages, rama `main`).

Mientras la web esté en pruebas, todas las páginas llevan `<meta name="robots" content="noindex, nofollow">` con el comentario «QUITAR al lanzar la web».

## Estructura

```
/                           → maderamen.calab.es
├── index.html              → portada (de momento redirige a /mapa/)
├── assets/                 → recursos comunes a toda la web
│   ├── css/                  colores, tipografía y estilos base
│   ├── fonts/                Montserrat
│   └── img/                  logo
├── mapa/                   → /mapa/  Mapa de la madera
│   ├── content/              proyectos, autores y apuntes (los edita el panel)
│   ├── media/                imágenes subidas desde el panel
│   ├── datos.js              generado automáticamente desde content/
│   ├── scripts/              build-datos.mjs y servidor-local.mjs
│   └── editar-2c3bb9b1/      panel de edición oculto (Sveltia CMS)
├── guia-GE/                → /guia-GE/  Guía de autoconstrucción en Guinea Ecuatorial
│   ├── index.html, …         versión web de la guía
│   └── proyecto/             material de trabajo: textos (docs/), PDF, script de compilación…
├── .github/workflows/      → acción que regenera mapa/datos.js
└── ver-en-local.bat        → abre la web en http://localhost:8787
```

Cada nueva sección de la web va en su propia carpeta y usa los recursos de `assets/`.

## Ver la web en local

Doble clic en `ver-en-local.bat`, o bien:

```
node mapa/scripts/servidor-local.mjs
```

## Mapa de la madera

- Panel: `maderamen.calab.es/mapa/editar-2c3bb9b1/`.
- Al guardar desde el panel, la acción «Mapa · actualizar datos» regenera `mapa/datos.js`. Haz `pull` antes de subir cambios desde tu ordenador.
- Requiere en GitHub: Settings → Actions → General → Workflow permissions → **Read and write permissions**.
