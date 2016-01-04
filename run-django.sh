#!/bin/bash

# Función que espera a que PostgreSQL haya sido inicializado.
function pg_wait {
  while : ; do
    pg_isready --host db --user postgres
    sleep 5
    if [ $? == 0 ]; then
      break
    else
      sleep 0.1
    fi
  done
}

pg_wait

python manage.py migrate
python manage.py bower install -- --allow-root
python manage.py collectstatic --noinput

gunicorn reservas.wsgi:application -b :8000
