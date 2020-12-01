#!/bin/bash

cd /code/mysite


python manage.py collectstatic --no-input

gunicorn --bind 0.0.0.0:8001 --workers=2 --timeout 60 mysite.wsgi:application
