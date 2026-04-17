import psycopg2
import csv
from config import params

def create_table():
    """Создает таблицу, если её нет"""
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(20) UNIQUE NOT NULL
            )
        """)
        conn.commit()
        print(" Таблица 'phonebook' готова к работе!")
    except Exception as e:
        print(f" Ошибка при создании: {e}")
    finally:
        if conn: conn.close()

def import_csv(filename):
    """Загружает данные из CSV"""
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # На Windows важно указывать encoding='utf-8'
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # Пропускаем заголовок
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                    (row[0], row[1])
                )
        conn.commit()
        print(f" Данные из {filename} загружены.")
    except FileNotFoundError:
        print(f" Файл {filename} не найден! Создай его в этой же папке.")
    except Exception as e:
        print(f" Ошибка импорта: {e}")
    finally:
        if conn: conn.close()

def add_contact():
    """Добавляет контакт через консоль"""
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print(f"Контакт {name} сохранен.")
    except Exception as e:
        print(f"Ошибка добавления: {e}")
    finally:
        if conn: conn.close()

def show_all():
    """Показывает все записи"""
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook ORDER BY id")
        rows = cur.fetchall()
        print("\n--- СПИСОК КОНТАКТОВ ---")
        for row in rows:
            print(f"ID: {row[0]} | Имя: {row[1]} | Тел: {row[2]}")
    except Exception as e:
        print(f"Ошибка поиска: {e}")
    finally:
        if conn: conn.close()

if __name__ == "__main__":
    create_table()
    while True:
        print("\nМЕНЮ: 1-CSV, 2-Добавить, 3-Показать, 0-Выход")
        choice = input("Выбор: ")
        if choice == "1": import_csv("contacts.csv")
        elif choice == "2": add_contact()
        elif choice == "3": show_all()
        elif choice == "0": break