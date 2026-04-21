# coding: utf-8
"""
Pcap Analyzer Studio Flask application bootstrap.

Copyright (c) Ayman Elbanhawy (Softwaremile.com)
Code updates and documentation improvements for the public
Pcap-AnalyzerStudio repository.
"""

from flask import Flask


# Create the shared Flask application object before importing any route modules.
app = Flask(__name__)
app.config.from_object("config")

# Import routes only after configuration is loaded so handlers can read settings.
from app import views
