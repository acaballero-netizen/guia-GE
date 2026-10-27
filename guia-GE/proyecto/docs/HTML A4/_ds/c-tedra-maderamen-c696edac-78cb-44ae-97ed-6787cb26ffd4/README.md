# Cátedra Maderamen — Design System

A design system for **Cátedra Maderamen**, an initiative of the **ETSA (Escuela Técnica Superior de Arquitectura)** at the **Universitat Politècnica de València (UPV)** focused on **innovation, sustainability, and timber construction in architecture**.

This system codifies the visual language used across the chair's communications: lectures, papers, presentations, event posters, and any web/digital surface produced under the Maderamen identity.

---

## Source materials provided

| File | Notes |
|---|---|
| `uploads/MADERAMEN_Rojo.png` | Full lockup, brand red on transparent |
| `uploads/MADERAMEN_Blanco.png` | Full lockup, white on transparent (use on red) |
| `uploads/MADERAMEN_Negro.png` | Full lockup, near-black on transparent (mono fallback) |
| `uploads/MADERAMEN_Marrón_Oscuro.png` | Full lockup, Marrón Oscuro `#423024` (secondary/warm) |
| `uploads/MADERAMEN_Marrón_Claro.png` | Full lockup, Marrón Claro `#DEC09C` (use on dark/brown bg) |
| `uploads/PLANTILLA Maderamen.pptx` | Official 16:9 slide template (3 layouts: cover, content, closing/partners) |

The PPTX shipped with Century Gothic baked into the text frames, but the **official written brief mandates Montserrat** — this system follows the brief. The full Montserrat family (Thin → Black, with italic variants) is bundled locally in `fonts/` and wired via `@font-face` in `colors_and_type.css` — no Google Fonts dependency.

---

## Context — what is Maderamen?

**Cátedra Maderamen** is a university chair (*"cátedra"*) hosted at ETSA-UPV, in Valencia, Spain. It is a teaching and research platform that broadens architecture education around **timber as a primary construction material**, **sustainability**, and **building innovation**.

Audience is bilingual (Spanish/Valencian/English at times), academic but outward-facing: students, faculty, professional architects, public-policy stakeholders, and partner institutions (Generalitat Valenciana, IVE — Institut Valencià de l'Edificació).

The visual register is therefore **academic yet contemporary** — closer to a contemporary architecture studio's portfolio than to a traditional university bulletin.

---

## Index

```
.
├── README.md                  ← you are here
├── SKILL.md                   ← machine-readable skill manifest
├── colors_and_type.css        ← all design tokens (color, type, spacing, shadow, motion)
│
├── assets/                    ← logos, slide backgrounds, partner logos
│   ├── logo-rojo.png          ← primary lockup, brand red
│   ├── logo-blanco.png        ← lockup, white (use on red bg)
│   ├── logo-negro.png         ← lockup, near-black (mono fallback)
│   ├── logo-marron-oscuro.png ← lockup, Marrón Oscuro #423024 (warm/secondary)
│   ├── logo-marron-claro.png  ← lockup, Marrón Claro #DEC09C (on dark/brown bg)
│   ├── slide-cover-red.jpg    ← reference: title-slide background w/ giant M
│   ├── slide-content-frame.jpg← reference: content-slide frame
│   └── slide-closing-partners.jpg ← reference: partner-logos closing slide
│
├── preview/                    ← Design System tab cards (tokens & components only)
│   ├── colors-primary.html
│   ├── colors-secondary.html
│   ├── colors-neutrals.html
│   ├── type-scale.html
│   ├── type-contrast.html
│   ├── spacing.html
│   ├── radii.html
│   ├── shadows.html
│   ├── buttons.html
│   ├── form-inputs.html
│   ├── badges.html
│   ├── cards.html
│   ├── logos.html
│   ├── logo-clearspace.html
│   └── iconography.html
│
└── templates/                  ← THE single "Templates" section — see norm below
    ├── presentacion/           ← Presentación 16:9 (deck, one file, all layouts)
    ├── documento/              ← Documento Editorial A4 (8 páginas, un archivo)
    ├── guia-autoconstruccion/  ← Guía de Autoconstrucción A4
    └── hoja-firmas/            ← Hoja de Firmas A4
```

### Norma — dónde viven las plantillas

Hay una única sección de plantillas: la carpeta `templates/`. Cada plantilla es una
subcarpeta `templates/<slug>/` con un Design Component `<Slug>.dc.html` marcado con
`@template` (igual que `guia-autoconstruccion/` y `hoja-firmas/`). Esa es la sección
correcta — **cualquier plantilla nueva (documento, presentación, hoja imprimible,
lo que sea) se añade ahí**, nunca como una card `@dsCard group="Templates"` suelta en
`preview/` u otra carpeta: eso duplica la sección en el picker.

Una plantilla con varias páginas o diapositivas se entrega como **un único archivo**
con todo el contenido dentro (secciones/slides internas) — no se fragmenta en un
archivo por página o por tipo de layout (portada, contenido, cierre…).

---

## VISUAL FOUNDATIONS

The Maderamen brand is built on three pillars, in this order: **white space**, **dense red moments**, **typographic contrast**.

### Color

- **Primary accent** — `#DC2F39` (Brand Red). Used for the M-flag icon, the wordmark, primary CTAs, accent rules, and **full-bleed cover/closing surfaces**. Never softened into pink, never warmed into orange.
- **Secondary — gama de marrones (madera).** A warm brown family added for variability, anchored on the two brown logo lockups: **Marrón Oscuro `#423024`** and **Marrón Claro `#DEC09C`**, plus a mid tone (`#7A5C44`) and two warm tints (`#ECDCC4`, `#F7F0E6`). It is a **support** colour — used for warm surfaces, alternating section bands, and "moment" panels where a full-red surface would be too much. The brown **never replaces the red** as the primary accent and is never mixed into the same element as a gradient. Flat fills only.
- **Neutrals** — pure white `#FFFFFF` is the canvas. Text is set in **dark warm-cool grey** (`#1F2123`), **never pure black**, because the brand red would clash against pure `#000` on co-located surfaces.
- **No gradients.** Color is always flat. The only "tonal" variation is `--color-brand-red-soft` / `--color-brand-red-tint` used sparingly for badge fills and section bands.
- **Imagery** is expected to be photography of timber buildings, structural details, students-at-work, and study models — warm-leaning, naturally lit, **never** desaturated to b&w as a stylistic choice. Treat color photos at full saturation.

### Typography

- **One typeface only: Montserrat.** Everything from a 12px caption to a 104px display word lives in this family.
- **Weight is the design system.** The brand thrives on the extreme delta between `Light (300)` body copy and `ExtraBold (800)` titulars. Avoid the middle weights for headlines — `Medium (500)` and `SemiBold (600)` exist for UI affordances (buttons, labels) but not for editorial titulars.
- **Uppercase for display.** Cover-slide titulars, section dividers and the wordmark itself are SET IN CAPS with a subtle positive tracking (`--ls-tight` keeps headlines tight; long all-caps phrases get `--ls-wide`).
- **Italic = quotation only.** Don't use italics for emphasis in body copy — let the weight contrast do that work.
- **Highlighted keywords** within a black headline can shift to brand red (`.ds-key`) — this is the signature move from the wordmark itself ("CÁTEDRA" Light, "MADERAMEN" ExtraBold, both red).

### Spacing & layout

- **4px base grid.** Tokens go from `--s-1` (4px) to `--s-10` (128px). Editorial pages should breathe — section gaps usually `--s-8` (64px) or `--s-9` (96px).
- **Generous outer margins.** Architectural plans use white margin as composition. Web/print layouts mirror this: minimum 64px outer gutter on desktop, never edge-to-edge text.
- **A horizontal red rule** (1px–4px depending on scale, brand red) is the workhorse divider — used to separate the masthead from content, section headers from body, and is visible across the PPTX template as the 4-px top band of content slides.
- **Fixed elements** are minimal: a thin top red rule plus the small "M" icon at the corner are the only chrome. No floating widgets.

### Backgrounds

- **Default:** pure white.
- **Section accent:** the brand red, full-bleed — used for cover slides, section dividers, and "moment" panels.
- **No textures, patterns, photo overlays, or gradients.** If a photograph is the background, it is the full canvas with text resting either inside a white card or directly on the photo with a top-aligned brand-red bar above it.

### Corners & borders

- **Radii are near-zero.** `--r-none` (0) and `--r-xs` (2px) cover 90 % of cases — the brand is architectural and orthogonal. `--r-sm` (4px) for buttons and inputs. `--r-pill` reserved for tiny badges/tags.
- **Borders** are 1px `--color-line` (#E5E5E5) — hairline, never heavy. The only "heavy" line is brand-red.

### Shadows

- **Three-step elevation, all subtle.** `--shadow-1` is hover/lift, `--shadow-2` is for cards floating over content, `--shadow-3` is reserved for modal/dropdown moments. The brand reads as paper-on-paper — shadows are almost mistakable for the page edge.
- **No glow, no neon.** No coloured shadows. Focus rings use a translucent brand-red.

### Motion

- Movement is restrained: 120–360ms with `--ease-out` for entrances and `--ease-std` for state changes. Avoid bounces, spring physics, or anything theatrical.
- **Hover states:** colour shift on text/links (red → red-deep), 6 % darken on buttons, opacity 0.85 on photographs.
- **Pressed states:** swap to `--color-brand-red-deep`, no scale-down, no shadow. Architectural surfaces don't squish.
- **Transparency / blur:** essentially unused. The brand prefers opaque planes meeting at hard edges.

### Cards

- White background (`--color-paper`).
- 1px `--color-line` border **or** `--shadow-1`, never both at once.
- Radius `--r-sm` (4 px).
- Internal padding `--s-5` (24 px) minimum, `--s-6` (32 px) for content-rich cards.
- A card may have a **flush brand-red top stripe** (2–4 px) as an accent — this echoes the slide template.

---

## CONTENT FUNDAMENTALS

### Language

- **Primary language: Castilian Spanish.** Valencian/Catalan may appear for partner names and official titles (e.g. *"Institut Valencià de l'Edificació"*). English used when addressing international academic audiences.
- Always use the proper diacritics: **CÁTEDRA** (with acute), never "CATEDRA".

### Voice and tone

- **Academic but contemporary.** Sentences are clear and well-formed, not floral. No marketing-speak, no exclamation points, no rhetorical questions.
- **First-person plural** ("nosotros / la Cátedra") for institutional voice. **Third person** for technical descriptions and case studies. Direct second-person ("tú") is avoided — too informal for the register; "usted" is too stiff; the chair speaks *about* its work, not *to* the reader.
- **Specific, never vague.** Prefer "construcción con CLT (madera contralaminada)" over "soluciones sostenibles".

### Casing

- **Titulars and section labels:** UPPERCASE.
- **Body copy:** sentence case.
- **Buttons & UI labels:** Title Case in Spanish (first word capitalised) — e.g. *"Inscribirse al seminario"*, *"Descargar la memoria"*.
- **Wordmark:** always rendered as the official lockup; never typed inline. If unavoidable in plain text, write **Cátedra Maderamen** (acute on the Á, both words capitalised).

### Copy examples

> **CONSTRUIR CON MADERA**
> Una nueva agenda formativa para la arquitectura sostenible en la Comunitat Valenciana.

> **Inscribirse al ciclo →**

> **Memoria 2024 — Cátedra Maderamen**
> Resumen anual de actividades formativas, líneas de investigación y publicaciones.

> *"La madera no es un material del pasado; es la herramienta más contemporánea para una arquitectura responsable."* — Ponente invitado, Ciclo 2024

### Emoji & symbols

- **No emoji.** Anywhere. The register doesn't accommodate them.
- **Arrows** (`→`, `←`) are welcome as CTA tails and as inline directional cues, set in Montserrat at the same weight as the surrounding text.
- **Bullet character** is a thin en-dash `–` or a 4 px brand-red square, not `•`.

---

## ICONOGRAPHY

Maderamen does **not** have a proprietary icon set. The provided assets are limited to the wordmark lockup and the M-flag mark.

### Recommendation

Adopt **[Lucide Icons](https://lucide.dev/)** as the working icon system (CDN-available, MIT licensed, stroke-based, architectural feel). Default stroke weight **1.5px**, default size **20px** in UI / **24px** in editorial. Render in `currentColor` so icons inherit text colour.

> **Substitution flag for the user:** No proprietary icon set was supplied. Lucide is a placeholder match — clean line geometry, low visual noise, plays well with Montserrat. **If the chair has an institutional icon set or preferred library, please share so we can swap it in.**

CDN snippet:

```html
<script src="https://unpkg.com/lucide@latest"></script>
<i data-lucide="leaf" style="width:20px;height:20px;stroke-width:1.5;"></i>
<script>lucide.createIcons();</script>
```

### Brand mark — the "M"

The **M-flag** (white M-mountain on red, looks like a pennant with two triangular cutouts) is the sole brand glyph. Treat it as a logo, not an icon:

- Don't recolour it outside the red/white/near-black trio.
- Minimum 24 px tall on screen.
- Clear-space: at least the height of one "M-mountain" peak on every side.
- Pair with the wordmark above ~40 px; below 40 px, the M-flag alone is fine.

### Photography vs illustration

- **Photography is the primary visual asset class.** Timber buildings, structural details, students/lectures, scale models.
- **Illustrations** are not part of the current language. If diagrams are needed, draw them as architectural line diagrams (1px black or red strokes on white) — never the cartoon/spot-illustration style.

### Emoji & unicode

- Not used. See *Content fundamentals → Emoji & symbols*.

---

## What's intentionally NOT included

- A full component library (composer, file panels, complex tables, etc.) — Maderamen has no product app surface today. The system covers **identity + editorial + slides**, which is what the chair actually publishes.
- A motion library — animation is restrained enough that the CSS variables cover the entire vocabulary.
- A grid / breakpoint system specific to a product — defer to the host project (the system is layout-agnostic).
