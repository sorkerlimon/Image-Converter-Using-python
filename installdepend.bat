@echo off

echo Creating a Python virtual environment...
call python -m venv env

echo Activating the virtual environment...
call env\Scripts\activate.bat

echo Installing Python dependencies from requirements.txt...
pip install -r requirments.txt

echo Virtual environment setup is complete.
pause
