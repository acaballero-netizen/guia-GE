// Sirve la web en http://localhost:8787/mapa/ tal como se verá publicada.
// Uso: node mapa/scripts/servidor-local.mjs   (desde la raíz del repositorio)
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const port = +process.argv[2] || 8787;
const types = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.yml': 'text/yaml; charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.ttf': 'font/ttf', '.pdf': 'application/pdf' };

http.createServer((req, res) => {
  const p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  // En local, datos.js se regenera en cada carga para ver al momento lo guardado desde el panel
  if (p === '/mapa/datos.js') spawnSync(process.execPath, [path.join(root, 'mapa', 'scripts', 'build-datos.mjs')], { stdio: 'inherit' });
  if (p === '/') { res.writeHead(302, { Location: '/mapa/' }); return res.end(); }
  let f = path.join(root, p);
  if (!f.startsWith(root)) { res.writeHead(403); return res.end(); }
  if (fs.existsSync(f) && fs.statSync(f).isDirectory()) {
    if (!p.endsWith('/')) { res.writeHead(301, { Location: p + '/' }); return res.end(); }
    f = path.join(f, 'index.html');
  }
  fs.readFile(f, (e, d) => {
    if (e) { res.writeHead(404); return res.end('No encontrado'); }
    res.writeHead(200, { 'Content-Type': types[path.extname(f).toLowerCase()] || 'application/octet-stream', 'Cache-Control': 'no-store' });
    res.end(d);
  });
}).listen(port, () => console.log(`Mapa de la madera en http://localhost:${port}/mapa/  (Ctrl + C para parar)`));
