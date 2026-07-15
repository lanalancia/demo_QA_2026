@echo off
cd /d "%~dp0"

echo ====================================================
echo   STARTING PLAYWRIGHT PROJECT INSTALLATION
echo ====================================================
echo.

:: 1. Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! 
    echo Please install Python 3.8+ and check "Add Python to PATH".
    echo.
    pause
    exit /b
)

:: 2. Create virtual environment if it doesn't exist
if not exist .venv (
    echo [1/4] Creating virtual environment .venv...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create .venv!
        pause
        exit /b
    )
) else (
    echo [1/4] .venv already exists. Skipping creation...
)

:: 3. Activate venv and upgrade pip
echo [2/4] Upgrading pip...
call .venv\Scripts\activate && python -m pip install --upgrade pip

:: 4. Install dependencies from requirements.txt
if exist requirements.txt (
    echo [3/4] Installing dependencies from requirements.txt...
    call .venv\Scripts\activate && pip install -r requirements.txt
) else (
    echo [WARNING] requirements.txt not found! Skipping installation...
)

:: 5. Install Playwright system browsers
echo [4/4] Downloading Playwright browsers...
call .venv\Scripts\activate && playwright install

echo.
echo ====================================================
echo   INSTALLATION COMPLETED SUCCESSFULLY!
echo   You can now use project with start.bat
echo ====================================================
echo.
pause