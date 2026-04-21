# coding: utf-8
"""
Development entry point for Pcap Analyzer Studio.

Copyright (c) Ayman Elbanhawy (Softwaremile.com)
Code updates and documentation improvements for the public
Pcap-AnalyzerStudio repository.
"""

from pathlib import Path
import os
import socket

from app import app


def ensure_runtime_folders() -> None:
    """Create the local runtime folders expected by uploads, exports, and PDFs."""
    runtime_root = Path(app.config["UPLOAD_FOLDER"]).resolve().parent
    file_root = Path(app.config["FILE_FOLDER"]).resolve()
    pdf_root = Path(app.config["PDF_FOLDER"]).resolve()
    for path in (
        runtime_root,
        Path(app.config["UPLOAD_FOLDER"]).resolve(),
        file_root,
        pdf_root,
        file_root / "All",
        file_root / "FTP",
        file_root / "Mail",
        file_root / "Web",
    ):
        path.mkdir(parents=True, exist_ok=True)


def resolve_port(start_port: int = 8000, max_attempts: int = 20) -> int:
    """Return the first free localhost port starting at ``start_port``."""
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(("127.0.0.1", port)) != 0:
                return port
    raise RuntimeError("Unable to find a free local port for Pcap Analyzer Studio.")


if __name__ == "__main__":
    ensure_runtime_folders()
    requested_port = int(os.getenv("PCAP_ANALYZER_PORT", "8000"))
    port = resolve_port(start_port=requested_port)
    print(f"Pcap Analyzer Studio is starting on http://127.0.0.1:{port}/")
    app.run(host="0.0.0.0", port=port)
