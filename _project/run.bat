@echo off
rem Step 1: Start Django development server using NirCmd to hide the window
start "" nircmd.exe exec hide cmd /c python manage.py runserver

rem Step 2: Open a browser and visit the local server in a new tab
start "" http://127.0.0.1:8000/
