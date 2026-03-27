import psycopg2
from config import params

def test_connection():
    conn = None
    try:
        # Пытаемся подключиться
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        # Создаем курсор (инструмент для выполнения команд)
        cur = conn.cursor()
        
        # Выполняем тестовый запрос
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        
        print(f"Success! Database version: {db_version}")
        
        # Закрываем соединение
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Connection failed: {error}")
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    test_connection()