#!/bin/bash

pip install --upgrade pip
pip install -r /app/requirements.txt

gunicorn app:api -c /app/conf/gunicorn_conf.py --reload