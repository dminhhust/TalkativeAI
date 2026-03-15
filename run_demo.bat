@echo off
setlocal

REM Change to project directory
cd /d "%~dp0TalkativeAI"

REM Build and start all services (database, backend microservices, gateway, frontend)
docker-compose up --build -d

REM Open the frontend in the default browser
start http://localhost:3000

endlocal
