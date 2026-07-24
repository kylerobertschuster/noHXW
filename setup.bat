@echo off
REM setup.bat — Bootstrap noHXW on Windows without requiring pip pre-installed.
REM
REM Usage:
REM   setup.bat

echo ============================================
echo    noHXW — Setup Bootstrap (Windows)
echo    No Hardware, No Problem
echo ============================================
echo.

REM ── Step 1: Find Python ───────────────────────────────────────────
echo [1/5] Looking for Python 3.10+...

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python --version
    goto :check_pip
)

where python3 >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python3 --version
    set PYTHON=python3
    goto :check_pip
)

echo  [ERROR] Python 3.10+ not found!
echo  Download it from: https://www.python.org/downloads/
echo  Make sure to check "Add Python to PATH" during installation.
pause
exit /b 1

:check_pip
echo [2/5] Making sure pip is available...

python -m pip --version >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo   pip is available
) else (
    echo   Installing pip via ensurepip...
    python -m ensurepip --upgrade
)

REM ── Step 3: Create virtual environment ──────────────────────────
echo [3/5] Creating virtual environment...

if exist .venv (
    echo   .venv already exists
) else (
    python -m venv .venv
    echo   Virtual environment created
)

set PIP=.venv\Scripts\pip

REM ── Step 4: Install dependencies ────────────────────────────────
echo [4/5] Installing dependencies...

%PIP% install --upgrade pip setuptools wheel -q
%PIP% install -e . -q

echo   Dependencies installed

REM ── Step 5: Done ────────────────────────────────────────────────
echo [5/5] Setup complete!
echo.
echo ============================================
echo    noHXW is ready to rock! ^(^)
echo ============================================
echo.
echo   Start the server:
echo     .venv\Scripts\activate
echo     noxhw
echo.
echo   Or directly:
echo     .venv\Scripts\noxhw
echo.
echo   Then open:
echo     http://localhost:3000
echo.
pause
