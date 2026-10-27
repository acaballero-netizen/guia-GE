// Lee content/** y genera datos.js con los elementos publicados.
// Lo ejecuta GitHub Actions cada vez que el panel guarda un cambio; en local: node scripts/build-datos.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const base = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const leer = dir => {
  const d = path.join(base, 'content', dir);
  if (!fs.existsSync(d)) return [];
  return fs.readdirSync(d).filter(f => f.endsWith('.json')).map(f => {
    try {
      return { slug: f.replace(/\.json$/, ''), ...JSON.parse(fs.readFileSync(path.join(d, f), 'utf8')) };
    } catch (e) {
      console.warn(`Aviso: ${dir}/${f} no es JSON válido y se omite (${e.message})`);
      return null;
    }
  }).filter(Boolean);
};
const publicado = x => (x.estado || 'publicado') === 'publicado';
const categoria = p => p < 25 ? 'puntual' : p < 50 ? 'hibrida' : p < 75 ? 'mayoritaria' : 'integral';
const es = (a, b) => String(a).localeCompare(String(b), 'es');

const proyectos = leer('proyectos').filter(publicado)
  .filter(p => {
    const ok = Number.isFinite(+p.lat) && Number.isFinite(+p.lng) && p.lat !== null && p.lng !== null;
    if (!ok) console.warn(`Aviso: el proyecto «${p.titulo}» no tiene coordenadas y no se muestra`);
    return ok;
  })
  // originales_drive y notas_internas son de uso interno: no se publican en la web
  .map(({ originales_drive, notas_internas, ...p }) => ({
    ...p,
    autores: Array.isArray(p.autores) ? p.autores : p.autores ? [p.autores] : [],
    elementos_madera: p.elementos_madera || [],
    porcentaje_madera: +p.porcentaje_madera || 0,
    categoria: categoria(+p.porcentaje_madera || 0),
  }))
  .sort((a, b) => es(a.titulo, b.titulo));

const autores = leer('autores').sort((a, b) => es(a.nombre, b.nombre));

const apuntes = leer('apuntes').filter(publicado)
  .sort((a, b) => (b.anio || 0) - (a.anio || 0) || es(a.titulo, b.titulo));

const datos = { generado: new Date().toISOString(), proyectos, autores, apuntes };
fs.writeFileSync(path.join(base, 'datos.js'),
  '// Archivo generado automáticamente desde content/. No editar a mano.\nwindow.MAPA=' + JSON.stringify(datos) + ';\n');
console.log(`datos.js: ${proyectos.length} proyectos, ${autores.length} autores, ${apuntes.length} apuntes`);
