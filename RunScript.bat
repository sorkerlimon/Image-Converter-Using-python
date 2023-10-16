@echo off

echo Activating the virtual environment...
call env\Scripts\activate.bat

echo Running your Python script...
python Image-Converter-v5.py

echo Deactivating the virtual environment...
deactivate

echo Script execution completed.
pause
