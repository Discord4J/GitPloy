#!/usr/bin/env bash

pip3 install -r requirements.txt
gunicorn --bind 0.0.0.0:7777 --workers 1 --threads 1 app:app