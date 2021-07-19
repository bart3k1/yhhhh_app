#!/bin/bash
set -e
# systemctl enable nginx
service nginx start
uwsgi -c /app/src/uwsgi.ini