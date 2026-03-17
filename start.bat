@echo off
echo ===================================================
echo  B2B Fleet Aggregator - Smart Boot Sequence
echo ===================================================

echo [1/4] Checking if Docker daemon is running...
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo [ALERT] Docker is not running. Attempting to wake up Docker Desktop...
    start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"

    echo [WAIT] Waiting for Docker engine to initialize (this may take a minute)...
    :check_docker
    timeout /t 5 /nobreak > NUL
    docker info >nul 2>&1
    if %errorlevel% neq 0 goto check_docker
    echo [SUCCESS] Docker engine is now online!
) else (
    echo [SUCCESS] Docker is already running.
)

echo.
echo [2/4] Starting PostgreSQL Database Container...
docker compose up -d

echo.
echo [3/4] Allowing database connections to open...
timeout /t 3 /nobreak > NUL

echo.
echo [4/4] Booting FastAPI Application...
uvicorn main:app --reload