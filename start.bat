@echo off
cd /d "%~dp0"

echo [START] Activating venv
cmd /k ".venv\Scripts\activate"
pip install -r requirements.txt
playwright install

pause