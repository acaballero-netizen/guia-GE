@echo off
rem Abre la web en local (http://localhost:8787/) como se vera publicada.
rem Cierra esta ventana para parar el servidor.
cd /d "%~dp0"
start "" http://localhost:8787/mapa/
node mapa\scripts\servidor-local.mjs
pause
