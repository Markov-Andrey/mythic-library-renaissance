@echo off

echo Starting frontend...
cd frontend
start cmd /k "npm run dev"
cd ..

echo Starting backend...
cd backend
call .\venv\Scripts\activate
cd ..
start cmd /k "cd backend && call ..\backend\venv\Scripts\activate && cd .. && python main.py"
