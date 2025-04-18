import psycopg2
import csv
from tabulate import tabulate


conn = psycopg2.connect(
    dbname="lab10", 
    user="postgres",
    password="Makaron99",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

conn.commit()


def insert_data():
    method = input('Type "csv" or "con": ').lower()
    if method == "con":
        name = input("Name: ")
        phone = input("Phone: ")
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    elif method == "csv":
        filepath = input("Enter CSV file path: ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Пропустить заголовок
            for row in reader:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", tuple(row))
    conn.commit()
    print("Data inserted.\n")

def update_data():
    phone = input("Enter phone number to update: ")
    new_name = input("New name: ")
    new_phone = input("New phone: ")
    cur.execute("UPDATE phonebook SET name = %s, phone = %s WHERE phone = %s", (new_name, new_phone, phone))
    conn.commit()
    print("Data updated.\n")

def delete_data():
    phone = input("Enter phone number to delete: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    print("Data deleted.\n")

def query_data():
    col = input("Search by (id/name/phone): ").lower()
    val = input(f"Enter value for {col}: ")
    cur.execute(f"SELECT * FROM phonebook WHERE {col} = %s", (val,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Phone"], tablefmt='fancy_grid'))

def display_data():
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Phone"], tablefmt='fancy_grid'))

while True:
    print("""
    ┌────────────────────────────────────┐
    │        PhoneBook Menu             │
    ├────────────────────────────────────┤
    │ 1. Insert data (CSV or Console)   │
    │ 2. Update data                    │
    │ 3. Search data                    │
    │ 4. Delete data                    │
    │ 5. Show all data                  │
    │ 6. Exit                           │
    └────────────────────────────────────┘
    """)

    cmd = input("Choose option (1-6): ").strip()

    if cmd == "1":
        insert_data()
    elif cmd == "2":
        update_data()
    elif cmd == "3":
        query_data()
    elif cmd == "4":
        delete_data()
    elif cmd == "5":
        display_data()
    elif cmd == "6":
        break
    else:
        print("Invalid choice. Try again.")

cur.close()
conn.close()
