import psycopg2
import json
import datetime

# создаю подключение к базе данных
connection = psycopg2.connect(
    user="postgres",
    # пароль, который указали при установке PostgreSQL
    password="2414",
    host="127.0.0.1",
    port="5432",
    database="my_database")

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
