"""
compilar_guia.py
────────────────
Genera un único archivo Markdown compilado a partir de los capítulos
individuales de la guía MADERAMEN, filtrando secciones, comentarios
y notas internas.

Uso:
    python compilar_guia.py

Salida:
    guia_completa.md  (en el mismo directorio donde se ejecuta el script)

Ajusta las constantes de configuración según necesites.
"""

import re
from pathlib import Path


# ══════════════════════════════════════════════════════════════════
# CONFIGURACIÓN — edita aquí
# ══════════════════════════════════════════════════════════════════

# Ruta base del repo (relativa al script o absoluta)
# Si el script está en la raíz del repo, déjalo como "."
BASE = Path(".")

# Archivos fuente, en el orden en que deben aparecer en el compilado
ARCHIVOS = [
    BASE / "docs" / "outline.md",
    BASE / "docs" / "paso01_pasos_previos.md",
    BASE / "docs" / "paso02_cimentacion.md",
    BASE / "docs" / "paso03_cerramiento.md",
    BASE / "docs" / "paso04_cubierta.md",
    BASE / "docs" / "paso05_carpinterias.md",
    BASE / "docs" / "paso99_mantenimiento.md",
]

# Archivo de salida
SALIDA = BASE / "guia_completa.md"

# Títulos de sección (## o ###) que se excluyen completamente.
# El filtro elimina el encabezado y todo su contenido hasta la siguiente
# sección del mismo nivel o superior.
# La comparación ignora mayúsculas/minúsculas y espacios extra.
SECCIONES_EXCLUIR = [
    # Secciones finales o de navegación que no deben aparecer en el PDF.
    "Siguiente paso",
]

# Bloques completos de texto que se eliminan aunque no sean secciones:
# - Comentarios HTML <!-- ... --> (PROMPT, TODO, NEW, etc.)
# - Líneas de navegación entre capítulos  [← Paso X] | [Paso Y →]
# - Líneas de metadatos al final de cada archivo (itálica con "Versión de trabajo")
ELIMINAR_COMENTARIOS_HTML = True
ELIMINAR_NAVEGACION = True
ELIMINAR_METADATOS_PIE = True

# Separador visual entre capítulos en el documento compilado.
SEPARADOR_CAPITULOS = "\n\n---\n\n"

# Salto de página adicional solo en el Markdown compilado para separar cada capítulo nuevo.
SALTO_PAGINA_TITULO = "<div style=\"page-break-before: always;\"></div>\n\n"

# Contraportada que aparecerá como página previa al índice (personalizable)
CONTRAPORTADA = """
#### Créditos
Proyecto MADERAMEN · ADSIDEO Cooperación 2024

Equipo: Cátedra MADERAMEN, UPV

Diseño y edición: Equipo MADERAMEN

"""

# Segunda página de contraportada (p. ej. agradecimientos, licencias)
CONTRAPORTADA_2 = """
#### Agradecimientos
Entidades colaboradoras...

Licencia: CC BY-SA 4.0

"""

# ══════════════════════════════════════════════════════════════════
# LÓGICA DE FILTRADO
# ══════════════════════════════════════════════════════════════════

def normalizar(texto: str) -> str:
    """Elimina espacios extra, emojis decorativos y pasa a minúsculas."""
    # Quitar emojis y símbolos Unicode no-ASCII frecuentes en los títulos
    texto = re.sub(r'[^\x00-\x7FáéíóúüñÁÉÍÓÚÜÑ¿¡·]', '', texto)
    # Ignorar marcadores de formato Markdown como negritas o cursivas
    texto = re.sub(r'[\*_`~\[\]]', '', texto)
    return texto.strip().lower()


def nivel_heading(linea: str) -> int:
    """Devuelve el nivel de heading (1-6) o 0 si no es heading."""
    m = re.match(r'^(#{1,6})\s', linea)
    return len(m.group(1)) if m else 0


def titulo_heading(linea: str) -> str:
    """Extrae el texto del heading sin los # iniciales."""
    return re.sub(r'^#{1,6}\s*', '', linea).strip()


def filtrar_secciones(lineas: list[str], excluir: list[str]) -> list[str]:
    """
    Elimina del texto las secciones cuyos títulos están en `excluir`,
    incluyendo todo el contenido hasta la siguiente sección de igual
    o mayor jerarquía.
    """
    excluir_norm = [normalizar(t) for t in excluir]
    resultado = []
    saltando = False
    nivel_salto = 0

    for linea in lineas:
        nivel = nivel_heading(linea)

        if saltando:
            # Seguimos saltando mientras no aparezca un heading del mismo
            # nivel o superior que cierre la sección excluida
            if nivel > 0 and nivel <= nivel_salto:
                saltando = False
                # Comprobamos si este nuevo heading también hay que excluir
                titulo = normalizar(titulo_heading(linea))
                if any(
                    titulo == excl or titulo.startswith(excl + " ") or titulo.startswith(excl + ":")
                    for excl in excluir_norm
                ):
                    nivel_salto = nivel
                    continue
                else:
                    resultado.append(linea)
            # Si nivel == 0 o nivel > nivel_salto, seguimos saltando
            continue

        if nivel > 0:
            titulo = normalizar(titulo_heading(linea))
            if any(
                titulo == excl or titulo.startswith(excl + " ") or titulo.startswith(excl + ":")
                for excl in excluir_norm
            ):
                saltando = True
                nivel_salto = nivel
                continue

        resultado.append(linea)

    return resultado


def limpiar_comentarios_html(texto: str) -> str:
    """Elimina todos los bloques <!-- ... --> sean de una o varias líneas."""
    return re.sub(r'<!--[\s\S]*?-->', '', texto)


def limpiar_navegacion(texto: str) -> str:
    """
    Elimina las líneas de navegación entre capítulos del tipo:
    [← 00. Pasos previos](paso0_pasos_previos.md) | [02. Cerramiento →](paso2_cerramiento.md)
    """
    # Línea con dos enlaces de navegación separados por |
    texto = re.sub(
        r'\[←[^\]]*\]\([^)]*\)\s*\|\s*\[[^\]]*→\]\([^)]*\)\n?',
        '', texto
    )
    # Línea con solo el enlace "anterior"
    texto = re.sub(r'\[← [^\]]*\]\([^)]*\)\n?', '', texto)
    # Línea con solo el enlace "siguiente"
    texto = re.sub(r'\[[^\]]*→\]\([^)]*\)\n?', '', texto)
    return texto


def limpiar_metadatos_pie(texto: str) -> str:
    """
    Elimina las líneas de metadatos al pie de cada capítulo, del tipo:
    *Guía elaborada para el proyecto ADSIDEO...*
    *UPV · Cátedra MADERAMEN*
    *Versión de trabajo — pendiente de validación técnica y revisión de campo*
    """
    texto = re.sub(r'\*Guía elaborada para[^\n]*\n?', '', texto)
    texto = re.sub(r'\*UPV · Cátedra MADERAMEN\*\n?', '', texto)
    texto = re.sub(r'\*Versión de trabajo[^\n]*\n?', '', texto)
    texto = re.sub(r'\*Borrador[^\n]*\n?', '', texto)
    return texto


def limpiar_lineas_vacias_excesivas(texto: str) -> str:
    """Reduce más de dos líneas en blanco consecutivas a dos."""
    return re.sub(r'\n{3,}', '\n\n', texto)


def ajustar_rutas_imagenes(texto: str) -> str:
    """Convierte las rutas de imágenes para el documento compilado en la raíz del repo."""
    texto = re.sub(
        r'(<img[^>]+src=["\"])(?!https?:|/|data:|docs/)(imagenes/)',
        r'\1docs/\2',
        texto,
    )
    texto = re.sub(
        r'(!\[[^\]]*\]\()(?!https?:|/|data:|docs/)(imagenes/)',
        r'\1docs/\2',
        texto,
    )
    return texto


def tiene_salto_pagina_inicio(texto: str) -> bool:
    """Comprueba si el texto empieza con un salto de página HTML."""
    return bool(re.match(r'^\s*<div[^>]*page-break', texto, re.IGNORECASE))


def procesar_archivo(ruta: Path) -> str:
    """Lee un archivo .md y aplica todos los filtros configurados."""
    if not ruta.exists():
        print(f"  [WARN] No encontrado: {ruta} - se omite")
        return ""

    texto = ruta.read_text(encoding="utf-8")

    # 1. Eliminar comentarios HTML (PROMPT, TODO, NEW…)
    if ELIMINAR_COMENTARIOS_HTML:
        texto = limpiar_comentarios_html(texto)

    # 2. Eliminar líneas de navegación entre capítulos
    if ELIMINAR_NAVEGACION:
        texto = limpiar_navegacion(texto)

    # 3. Eliminar metadatos de pie
    if ELIMINAR_METADATOS_PIE:
        texto = limpiar_metadatos_pie(texto)

    # 4. Filtrar secciones excluidas
    lineas = texto.splitlines(keepends=True)
    lineas = filtrar_secciones(lineas, SECCIONES_EXCLUIR)
    texto = "".join(lineas)


    # 5. Ajustar rutas de imágenes para el documento compilado.
    texto = ajustar_rutas_imagenes(texto)

    # 6. Limpiar líneas vacías excesivas que dejan los filtros
    texto = limpiar_lineas_vacias_excesivas(texto)

    return texto


# ══════════════════════════════════════════════════════════════════
# EJECUCIÓN PRINCIPAL
# ══════════════════════════════════════════════════════════════════

def main():
    print("Compilando guia MADERAMEN...\n")

    bloques = []

    for ruta in ARCHIVOS:
        print(f"  -> {ruta.name}")
        contenido = procesar_archivo(ruta)
        if contenido:
            if bloques and not tiene_salto_pagina_inicio(contenido):
                contenido = SALTO_PAGINA_TITULO + contenido
            bloques.append(contenido)

    # Preparar portada HTML si existe
    portada_texto = ""
    # Insertar solo las dos páginas de contraportada antes del contenido.
    partes = [
        CONTRAPORTADA,
        SALTO_PAGINA_TITULO,
        CONTRAPORTADA_2,
        SALTO_PAGINA_TITULO,
        SEPARADOR_CAPITULOS.join(bloques),
    ]

    compilado = "".join(partes)

    SALIDA.write_text(compilado, encoding="utf-8")
    print(f"\n[OK] Generado: {SALIDA}")

    # Estadísticas rápidas
    palabras = len(compilado.split())
    lineas   = compilado.count('\n')
    print(f"   {lineas} lineas . {palabras} palabras . {len(compilado):,} caracteres")


if __name__ == "__main__":
    main()