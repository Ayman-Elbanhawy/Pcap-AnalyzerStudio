@echo off
REM Pcap Analyzer Studio Windows EXE build script.
REM Copyright (c) Ayman Elbanhawy (Softwaremile.com)
setlocal

set "ROOT=%~dp0"
set "VENV=%ROOT%.venv"
set "PY=%VENV%\Scripts\python.exe"
set "APP=pcap_analyzer_exe.py"

cd /d "%ROOT%"

if not exist "%PY%" (
    echo Creating Python virtual environment...
    python -m venv "%VENV%"
    if errorlevel 1 exit /b 1
)

echo Installing build dependencies...
"%PY%" -m pip install --index-url https://pypi.org/simple --upgrade pip Flask Flask-WTF geoip2 pyx requests scapy pyinstaller
if errorlevel 1 exit /b 1

echo Building PcapAnalyzer.exe...
"%PY%" -m PyInstaller --noconfirm --clean --onefile --console ^
  --name PcapAnalyzer ^
  --add-data "app\templates;app\templates" ^
  --add-data "app\static;app\static" ^
  --add-data "app\utils\protocol;app\utils\protocol" ^
  --add-data "app\utils\warning;app\utils\warning" ^
  --add-data "app\utils\GeoIP;app\utils\GeoIP" ^
  --hidden-import scapy.layers.l2 ^
  --hidden-import scapy.layers.inet ^
  --hidden-import scapy.layers.inet6 ^
  --hidden-import scapy.layers.dns ^
  "%APP%"
if errorlevel 1 exit /b 1

echo.
echo Build complete: %ROOT%dist\PcapAnalyzer.exe
echo Run it with: "%ROOT%dist\PcapAnalyzer.exe"
endlocal
