#!/bin/sh

echo "Making migrations and migrating the database."

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Starting Django server on 0.0.0.0:8000"

exec python manage.py runserver 0.0.0.0:8000