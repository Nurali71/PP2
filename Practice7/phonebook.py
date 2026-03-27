import psycopg2
from config import params

def create_tables():
    """Создает таблицу phonebook в базе данных"""
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        contact_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        phone_number VARCHAR(20) UNIQUE NOT NULL
    )
    """
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Выполняем команду создания таблицы
        cur.execute(command)
        # Закрываем курсор
        cur.close()
        # Сохраняем изменения (COMMIT)
        conn.commit()
        print("Table 'phonebook' created successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()