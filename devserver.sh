#!/bin/sh
source .env
source .venv/bin/activate
python -m flask --app main run -p $PORT --debug