#!/bin/sh
source .venv/bin/activate
python UIII_Hospital_0777/manage.py makemigrations
python UIII_Hospital_0777/manage.py migrate