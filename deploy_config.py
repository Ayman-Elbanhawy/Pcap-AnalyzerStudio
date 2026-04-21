# coding: utf-8
# Pcap Analyzer Studio Gunicorn settings.
# Copyright (c) Ayman Elbanhawy (Softwaremile.com)

bind = '0.0.0.0:8000'  # Local bind address for reverse-proxy or test runs.
workers = 1  # A single worker matches the lightweight desktop-style workload.
backlog = 2048
debug = True
proc_name = 'gunicorn.pid'
pidfile = '/var/log/gunicorn/debug.log'
loglevel = 'debug'
