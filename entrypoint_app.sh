#!/usr/bin/env sh

python manage.py collectstatic --noinput
python manage.py migrate --noinput

if [ "$LOCALMODE" = 1 ]; then
    python manage.py runserver 0:8000
else
    hypercorn backend.asgi:application --workers 2 --bind 0.0.0.0
fi