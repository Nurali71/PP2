import psycopg2
import json
import csv
from config import params

def get_conn():
    return psycopg2.connect(**params)


def show_paginated_ui():
    page = 0
    limit = 5
    while True:
        offset = page * limit
        with get_conn() as conn:
            with conn.cursor() as cur:
                # Using a stored procedure for pagination
                cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
                rows = cur.fetchall()
                
                print(f"\n--- Page {page + 1} ---")
                for r in rows: print(r)
                
                cmd = input("\n[n] Next, [p] Prev, [q] Quit: ").lower()
                if cmd == 'n' and len(rows) == limit: page += 1
                elif cmd == 'p' and page > 0: page -= 1
                elif cmd == 'q': break

def advanced_search():
    query = input("Search (name/email/phone): ")
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts_ext(%s)", (query,))
            for row in cur.fetchall(): print(row)

# --- 3.3 Import / Export JSON ---
def export_to_json():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.name, c.email, c.birthday, g.name as group, 
                       array_agg(p.phone || ':' || p.type) as phones
                FROM contacts c
                LEFT JOIN groups g ON c.group_id = g.id
                LEFT JOIN phones p ON c.id = p.contact_id
                GROUP BY c.id, g.name
            """)
            data = []
            for row in cur.fetchall():
                data.append({
                    "name": row[0], "email": row[1], 
                    "birthday": str(row[2]), "group": row[3], "phones": row[4]
                })
            
            with open("contacts.json", "w") as f:
                json.dump(data, f, indent=4)
    print("✅ Exported to contacts.json")

def import_from_json():
    filename = input("Enter JSON filename: ")
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            
        with get_conn() as conn:
            for item in data:
                with conn.cursor() as cur:
                    # Check for duplicate
                    cur.execute("SELECT id FROM contacts WHERE name = %s", (item['name'],))
                    exists = cur.fetchone()
                    
                    if exists:
                        choice = input(f"Contact {item['name']} exists. Overwrite? (y/n): ")
                        if choice.lower() != 'y': continue
                        cur.execute("DELETE FROM contacts WHERE name = %s", (item['name'],))

                    # Insert contact
                    cur.execute("INSERT INTO contacts (name, email, birthday) VALUES (%s, %s, %s) RETURNING id", 
                                (item['name'], item.get('email'), item.get('birthday')))
                    c_id = cur.fetchone()[0]
                    
                    # Insert phones
                    for p_entry in item.get('phones', []):
                        if p_entry:
                            p_num, p_type = p_entry.split(':')
                            cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)", 
                                        (c_id, p_num, p_type))
            conn.commit()
        print("✅ Import finished!")
    except Exception as e: print(f"❌ Error: {e}")

# --- Main Menu ---
def menu():
    while True:
        print("\n--- TSIS 1 Phonebook ---")
        print("1. Advanced Search")
        print("2. Paginated View (Navigable)")
        print("3. Export to JSON")
        print("4. Import from JSON")
        print("5. Add Phone (Procedure)")
        print("6. Change Group (Procedure)")
        print("0. Exit")
        
        choice = input("Select: ")
        if choice == '1': advanced_search()
        elif choice == '2': show_paginated_ui()
        elif choice == '3': export_to_json()
        elif choice == '4': import_from_json()
        elif choice == '5':
            name = input("Contact Name: ")
            phone = input("Phone: ")
            ptype = input("Type (home/work/mobile): ")
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
                    conn.commit()
        elif choice == '6':
            name = input("Contact Name: ")
            grp = input("New Group Name: ")
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute("CALL move_to_group(%s, %s)", (name, grp))
                    conn.commit()
        elif choice == '0': break

if __name__ == "__main__":
    menu()