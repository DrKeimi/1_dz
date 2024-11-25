import os
from zipfile import ZipFile

filepath = "test.zip"
user = "admin"
computer = "test_computer"
name_of_system = "Linux"
# Simulate present working directory (initially root "/")
current_dir = "/"


# Function to display current working directory
def get_current_dir():
    return current_dir


def reverse_readline(filename1):
    lines = []
    # Открываем zip-файл
    with ZipFile(filepath, 'r') as z:
        # Читаем содержимое нужного файла
        with z.open(filename1) as f:
            # Читаем файл построчно и добавляем строки в массив
            for line in f:
                lines.append(line.decode('utf-8').strip())  # Декодируем строку и убираем лишние пробелы

    # Переворачиваем массив строк
    lines.reverse()
    result = '\n'.join(lines)

    return result



def change_directory(new_dir, zip_file):
    global current_dir

    # Ensure directory starts from root if it begins with '/'
    if new_dir.startswith("/"):
        temp_dir = new_dir
    else:
        # Otherwise, navigate relative to the current directory
        temp_dir = f"{current_dir}/{new_dir}".strip("/")

    # Check if the directory exists in the zip file
    possible_dirs = [
        file
        for file in zip_file.namelist()
        if file.startswith(temp_dir.strip("/") + "/")
    ]

    if possible_dirs:
        # Update current directory if it exists
        current_dir = "/" + temp_dir.strip("/")
    else:
        print(f"cd: no such directory: {new_dir}")


# Open the ZIP file (virtual file system)
with ZipFile(filepath, "r") as zip_file:
    while True:
        command = input(f"{user}:{computer}${current_dir} ")
        command1 = command.split()

        if command == "exit":
            break

        elif command == "ls":
            print(zip_file.namelist())

        elif command1[0] == "cd":
            # Extract the target directory from the command
            _, new_dir = command.split(" ", 1)
            print(new_dir)
            change_directory(new_dir, zip_file)


        elif command1[0] == "tac":
            t = reverse_readline(command1[1])
            print(t)

        elif command == "who":
            print(user)

        elif command == "exit":
            break

        else:
            print("Enter a valid command (ls, pwd, exit)")
