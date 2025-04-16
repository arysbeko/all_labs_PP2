import psycopg2
import csv

conn = psycopg2.connect(
    dbname="lab10",  # Используем твою БД
    user="postgres",
    password="Makaron99",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

def insert_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row['name'], row['phone']))
    conn.commit()
    print("Inserted from CSV.")


def insert_from_input():
    name = input("Insert name: ")
    phone = input("Insert phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Inserted.")


def update_data():
    name = input("Enter name to update: ")
    new_name = input("New name: ")
    new_phone = input("New phone: ")
    cur.execute("UPDATE phonebook SET name = %s, phone = %s WHERE name = %s", (new_name, new_phone, name))
    conn.commit()
    print("Updated")


def search_data():
    filter_name = input("Search by name: ")
    cur.execute("SELECT * FROM phonebook WHERE name LIKE %s OR phone LIKE %s", (f'%{filter_name}%', f'%{filter_name}%'))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")


def delete_data():
    name = input("Enter name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    print("Deleted.")


def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def menu():
    while True:
        print("\nPhoneBook Menu")
        print("1. Insert from CSV")
        print("2. Insert from input")
        print("3. Update data")
        print("4. Search data")
        print("5. Delete data")
        print("6. Show all data")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            insert_from_csv('C:/Users/user/Desktop/all_labs_PP2/labs/lab10/asd.csv')
        elif choice == '2':
            insert_from_input()
        elif choice == '3':
            update_data()
        elif choice == '4':
            search_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            show_all()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Try again!")

    cur.close()
    conn.close()


if __name__ == '__main__':
    menu()
