# codeBusters

## Stack:
- Python 3.10.7
- Django 4.1.1
- Postgres 14

## Config:
1. Copy `example.env` to `.env`
2. Optionally make and activate python virtual environment `python3.10 -m venv venv && ./venv/bin/activate` or with alternative method
3. Up DB:
    - locally
        or
    - in docker container `docker-compose -f dev-docker-compose.yml up -d`
4. Optionally from `app/` `python manage.py makemigrations && python manage.py migrate`
5. To login in Django Administration page create superuser from `app/` execute `python manage.py createsuperuser`
