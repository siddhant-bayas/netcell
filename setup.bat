@echo off
SETLOCAL EnableDelayedExpansion

echo ========================================
echo       NetCell Global Installer
echo ========================================

:: 1. Check for Python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python not found. Please install Python and add it to your PATH.
    pause
    exit /b
)

:: 2. Get the Site-Packages path
for /f "tokens=*" %%i in ('python -c "import site; print(site.getsitepackages()[0])"') do set "SITE_PACKAGES=%%i"

echo [1/3] Target: %SITE_PACKAGES%

:: 3. Download netcell.py directly to Site-Packages
echo [2/3] Downloading NetCell to Python library...
python -c "import urllib.request; urllib.request.urlretrieve('https://raw.githubusercontent.com/siddhant-bayas/netcell/refs/heads/main/netcell.py', 'netcell.py')"
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to download. Try running this script as Administrator.
    pause
    exit /b
)

:: 4. Install dependencies
echo [3/3] Installing dependencies...
python -m pip install zstandard openpyxl --quiet

echo.
echo ========================================
echo [SUCCESS] NetCell is now global!
echo ========================================
pause