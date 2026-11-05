@echo off
cd /d "%~dp0"
where node >nul 2>nul
if errorlevel 1 (
  echo Node.js non trovato. Installa Node.js LTS oppure usa Python come indicato nel README.
  pause
  exit /b 1
)
start "" http://localhost:4173/it/
node preview.mjs
pause
