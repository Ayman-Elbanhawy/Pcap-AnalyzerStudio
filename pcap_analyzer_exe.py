# coding: utf-8
"""
Windows EXE launcher for Pcap Analyzer Studio.

Copyright (c) Ayman Elbanhawy (Softwaremile.com)
Code updates and packaging support for the public
Pcap-AnalyzerStudio repository.
"""

import os
import socket
import sys
import threading
import time
import webbrowser
from pathlib import Path


def application_dir() -> Path:
    """Return the folder that contains either the script or the frozen EXE."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def configure_runtime(app) -> None:
    """Point the Flask app at runtime folders beside the executable."""
    runtime = application_dir() / "runtime"
    upload = runtime / "PCAP"
    files = runtime / "Files"
    pdf = files / "PDF"

    for path in [upload, files, pdf, files / "All", files / "FTP", files / "Mail", files / "Web"]:
        path.mkdir(parents=True, exist_ok=True)

    app.config.update(
        UPLOAD_FOLDER=str(upload) + os.sep,
        FILE_FOLDER=str(files) + os.sep,
        PDF_FOLDER=str(pdf) + os.sep,
    )


def open_browser_later(url: str) -> None:
    """Delay browser launch slightly so the local server is ready to accept requests."""
    time.sleep(1.5)
    webbrowser.open(url)


def resolve_port(start_port: int = 8000, max_attempts: int = 20) -> int:
    """Find an available local HTTP port so the EXE does not fail on a busy 8000."""
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(("127.0.0.1", port)) != 0:
                return port
    raise RuntimeError("Unable to find a free local port for Pcap Analyzer Studio.")


def main() -> None:
    """Configure the packaged app runtime and start the local Flask server."""
    from app import app

    configure_runtime(app)
    requested_port = int(os.getenv("PCAP_ANALYZER_PORT", "8000"))
    port = resolve_port(start_port=requested_port)
    url = f"http://127.0.0.1:{port}/"
    threading.Thread(target=open_browser_later, args=(url,), daemon=True).start()
    print(f"Pcap Analyzer is running at {url}")
    print("Close this window to stop the application.")
    app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)


if __name__ == "__main__":
    main()
