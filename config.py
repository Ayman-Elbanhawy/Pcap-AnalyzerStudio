# coding: utf-8
"""
Runtime configuration for Pcap Analyzer Studio.

Copyright (c) Ayman Elbanhawy (Softwaremile.com)
Code updates and documentation improvements for the public
Pcap-AnalyzerStudio repository.
"""

from pathlib import Path


# Resolve runtime folders relative to this repository so local runs, screenshots,
# and packaged builds all use the same predictable folder layout.
PROJECT_ROOT = Path(__file__).resolve().parent
RUNTIME_ROOT = PROJECT_ROOT / "runtime"
UPLOAD_PATH = RUNTIME_ROOT / "PCAP"
FILE_PATH = RUNTIME_ROOT / "Files"
PDF_PATH = FILE_PATH / "PDF"

DEBUG = True
WTF_CSRF_ENABLED = False
SECRET_KEY = "!@#$%8F6F98EC3684AECA1DC44E1CB816E4A5^&*()"

UPLOAD_FOLDER = str(UPLOAD_PATH) + "/"
FILE_FOLDER = str(FILE_PATH) + "/"
PDF_FOLDER = str(PDF_PATH) + "/"
GITHUB_REPOSITORY = "https://github.com/Ayman-Elbanhawy/Pcap-AnalyzerStudio"
