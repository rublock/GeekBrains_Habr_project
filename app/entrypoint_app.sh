#!/usr/bin/env sh
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py createadmin

if [ "$LOCALMODE" = 1 ]; then
    python manage.py runserver 0:8000
else
    hypercorn config.asgi:application --workers 2 --bind 0.0.0.0
fi