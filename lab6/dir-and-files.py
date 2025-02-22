print("---------------------------Task1:---------------------------\n")

import os

path = r"C:\Users\user\Documents"
all = os.listdir(path)
print("Содержимое папки Documents:")
all = list(os.listdir(path))
print(all)



print("\n-------------------------Task2:---------------------------\n")

def check_access(path):
    if not os.path.exists(path):
        print("path doesn't exist")
        return
    else:
        print('path does exist')
        if os.access(path, os.R_OK):
            print("readable")
        else:
            print("don't readable")
        if os.access(path, os.W_OK):
            print("writable")
        else:
            print("don't writable")
        if os.access(path, os.X_OK):
            print("executable")
        else:
            print("don't executable")

if __name__ == "__main__":
    path_to_check = r"C:\Users\user\Documents"
    check_access(path_to_check)



print("\n-------------------------Task3:---------------------------\n")


def checker(path):
    if os.path.exists(path):
        print("File name:", os.path.basename(path))
        print("Directory name:", os.path.dirname(path))
    else:
        print("Path does not exist.")

checker(path)



print("\n-------------------------task4:---------------------------\n")

with open("sometext.txt") as f:
    data = f.read()

lines = data.split("\n")
if lines[-1] == "":
    lines = lines[:-1]

print("Number of lines:", len(lines))



print("\n-------------------------task5:---------------------------\n")

def list_to_file(filename, list):
    with open(filename, "a") as f:
        f.write(f"\n")
        for item in list:
            f.write(f"{item}\n")

my_list = ["Apple", "Banana", "Cherry", "Date"]
list_to_file("sometext.txt", my_list)



print("\n-------------------------task6:---------------------------\n")

import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("hello world")

if __name__ == "__main__":
    generate_files()



print("\n-------------------------task7:---------------------------\n")

with open('sometext.txt','r') as f1,open('destination.txt','w') as f2:
    f2.write(f1.read())



print("\n-------------------------task8:---------------------------\n")

import os

def delete_file(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"The file '{file_path}' does not exist.")
            return
        
        if not os.access(file_path, os.W_OK):
            print(f"No permission to delete the file '{file_path}'.")
            return
        
        os.remove(file_path)
        print(f"The file '{file_path}' has been deleted successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = r'C:\Users\user\PycharmProjects\Lab4\Task7.py'  
delete_file(file_path)