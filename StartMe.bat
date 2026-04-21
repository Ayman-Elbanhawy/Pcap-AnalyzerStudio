@echo off
REM Pcap Analyzer Studio bootstrap script.
REM Copyright (c) Ayman Elbanhawy (Softwaremile.com)
setlocal

set "ROOT=%~dp0"
set "VENV=%ROOT%.venv"
set "PY=%VENV%\Scripts\python.exe"
set "APP_PORT="
set "APP_URL="

cd /d "%ROOT%"

echo [Pcap-AnalyzerStudio] Project folder: %ROOT%

if not exist "%PY%" (
    echo [Pcap-AnalyzerStudio] Creating Python virtual environment...
    python -m venv "%VENV%"
    if errorlevel 1 (
        echo [Pcap-AnalyzerStudio] Failed to create the virtual environment.
        echo [Pcap-AnalyzerStudio] Make sure Python 3 is installed and available as "python".
        pause
        exit /b 1
    )
)

echo [Pcap-AnalyzerStudio] Installing/updating Python dependencies...
"%PY%" -m pip install --index-url https://pypi.org/simple --upgrade pip Flask Flask-WTF geoip2 pyx requests scapy
if errorlevel 1 (
    echo [Pcap-AnalyzerStudio] Dependency installation failed.
    pause
    exit /b 1
)

echo [Pcap-AnalyzerStudio] Creating runtime folders...
if not exist "%ROOT%runtime\PCAP" mkdir "%ROOT%runtime\PCAP"
if not exist "%ROOT%runtime\Files\All" mkdir "%ROOT%runtime\Files\All"
if not exist "%ROOT%runtime\Files\FTP" mkdir "%ROOT%runtime\Files\FTP"
if not exist "%ROOT%runtime\Files\Mail" mkdir "%ROOT%runtime\Files\Mail"
if not exist "%ROOT%runtime\Files\Web" mkdir "%ROOT%runtime\Files\Web"
if not exist "%ROOT%runtime\Files\PDF" mkdir "%ROOT%runtime\Files\PDF"

for /f %%P in ('powershell -NoProfile -Command "$start=8000; foreach ($p in $start..($start+19)) { $listener = [System.Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback, $p); try { $listener.Start(); $listener.Stop(); Write-Output $p; break } catch { if ($listener) { try { $listener.Stop() } catch {} } } }"') do set "APP_PORT=%%P"
if "%APP_PORT%"=="" set "APP_PORT=8000"
set "APP_URL=http://127.0.0.1:%APP_PORT%/"
set "PCAP_ANALYZER_PORT=%APP_PORT%"

echo [Pcap-AnalyzerStudio] Starting server at %APP_URL%
start "Pcap-AnalyzerStudio Server" /d "%ROOT%" cmd /k ""%PY%" "%ROOT%run.py""

echo [Pcap-AnalyzerStudio] Waiting for the server to start...
timeout /t 4 /nobreak >nul

echo [Pcap-AnalyzerStudio] Opening browser...
start "" "%APP_URL%"

echo [Pcap-AnalyzerStudio] Done. Close the "Pcap-AnalyzerStudio Server" window to stop the app.
endlocal
