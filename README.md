# codeBusters

## Stack:
- Python 3.10.7
- Django 4.1.1
- Postgres 14
- BootStrap 5
- Django Rest Framework

## Config:
1. Copy `example.env` to `.env`
2. Optionally make and activate python virtual environment `python3.10 -m venv venv && ./venv/bin/activate` or with alternative method
3. Install rerequirements if need `pip install -r ./requirements.txt`
4. Up DB:
    - locally
        or
    - in docker container `docker-compose -f dev-docker-compose.yml up -d`
5. Optionally from `app/` `python manage.py makemigrations && python manage.py migrate`
6. If you needed to download data to your database, make next command from `app/` `python manage.py loaddata database.json` 
7. If you made point 6 login and password to superuser is:
   - login - `admin`
   - password - `admin`
8. If you don't do the point 6, you mast create the superuser to login in Django Administration page. 
   
To create superuser from `app/` execute `python manage.py createsuperuser`

## Deploy to VPS:
1. Ubuntu 22.04 LTS
2. apt update && apt install git-core docker-compose
3. git clone https://github.com/krlvn/codeBusters
4. cd CodeBusters
5. cp example.env .env
6. make DEBUG=False, email settings in .env
7. docker-compose up
