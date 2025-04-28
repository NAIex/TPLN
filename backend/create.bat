@echo off
REM Step 1: Create virtual environment
python -m venv .venv

REM Step 2: Activate virtual environment
call .venv\Scripts\activate.bat

REM Step 3: Install requirements
pip install -r requirements.txt

echo.
echo Setup complete!
pause