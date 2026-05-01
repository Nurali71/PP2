import psycopg2
from config import params

def get_conn():
    return psycopg2.connect(**params)

# 1. Вызов функции поиска (Practice 8.1)
def search_pattern():
    pattern = input("Search for: ")
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
            for row in cur.fetchall():
                print(row)

# 2. Вызов Upsert процедуры (Practice 8.2)
def upsert():
    name = input("Name: ")
    phone = input("Phone: ")
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
            conn.commit()
    print("✅ Done!")

# 3. Пагинация (Practice 8.4)
def show_paginated():
    limit = int(input("How many rows? "))
    offset = int(input("Skip how many rows? "))
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            for row in cur.fetchall():
                print(row)

# 4. Удаление (Practice 8.5)
def delete_v2():
    target = input("Enter name or phone to delete: ")
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact_v2(%s)", (target,))
            conn.commit()
    print("✅ Deleted!")