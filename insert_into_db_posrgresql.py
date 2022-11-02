import psycopg2
import json
import datetime
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print('Ошибка импорта переменных окружения')

# создаю подключение к базе данных
connection = psycopg2.connect(
    user=os.environ['DB_USER'],
    # пароль, который указали при установке PostgreSQL
    password=os.environ['DB_PASSWORD'],
    host=os.environ['DB_HOST'],
    port=os.environ['DB_PORT'],
    database=os.environ['DB_NAME'])

# переменная для обращения к базе данных
cursor = connection.cursor()

# Распечатать сведения о PostgreSQL
print("Информация о сервере PostgreSQL")
print(connection.get_dsn_parameters(), "\n")

# Выполнение SQL-запроса
cursor.execute("SELECT version();")

# Получить результат
record = cursor.fetchone()

print("Вы подключены к - ", record, "\n")

# создаю список кортежей данных для внесения в таблицу
tuple_quotes = []
with open('articles_20.json', 'r', encoding='utf-8') as file_quotes:
    a = json.load(file_quotes)
    for i in a:
        tuple_quotes.append(tuple(i.values()))

# переменная с командой внесения данных в таблицу
insert_query = '''
    INSERT INTO mainapp_post(
        user_id,
        title,
        description,
        category_id,
        active,
        is_deleted,
        created_at,
        updated_at,
        image,
        content
        )
    VALUES(
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
        )
'''
cursor.executemany(insert_query, tuple_quotes)
# cursor.execute(insert_query, abc)
connection.commit()

if connection:
    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")
