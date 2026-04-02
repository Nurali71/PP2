import psycopg2
from config import params

def connect():
    """ Устанавливает соединение с сервером PostgreSQL """
    conn = None
    try:
        # Читаем параметры подключения из config.py
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка при подключении к базе: {error}")
        return None