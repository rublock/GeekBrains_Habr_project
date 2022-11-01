import psycopg2
import json

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

search_query = '''
    SELECT * FROM mainapp_post
'''

cursor.execute(search_query)

# переменная с найденными значениями
rows = cursor.fetchall()
for row in rows:
    print(row)

if connection:
    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")