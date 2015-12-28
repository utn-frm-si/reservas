#!/bin/bash

python manage.py migrate
python manage.py bower install -- --allow-root
python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8000
