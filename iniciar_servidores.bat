@echo off
title Panel REDstampacion - Servidores
color 0b

echo ==========================================
echo   INICIANDO PROYECTO CRUD-DJANGO + 3D
echo ==========================================

:: 1. Iniciar Django (Backend)
echo [+] Iniciando Django desde la raiz...
start "BACKEND - Django" cmd /k "call venv\Scripts\activate && python manage.py runserver"

:: 2. Iniciar Vite (Frontend 3D)
echo [+] Entrando a 3d-model e iniciando Vite...
start "FRONTEND - Vite" cmd /k "cd 3d-model && npm run dev"

echo.
echo ------------------------------------------
echo   Servidores en marcha. 
echo   Si algo falla, revisa las nuevas ventanas.
echo ------------------------------------------
echo.
pause