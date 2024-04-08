import os
import csv
from tabulate import tabulate

def createregister_file():
    header = ["user_name", "password", "foreign_key"]
    with open("register.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)

def create_user_task_file(foreign_key):
    task_file_name = f"tasks{foreign_key}.csv"
    header = ["task", "date"]
    with open(task_file_name, "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)

def get_next_foreign_key():
    if not os.path.isfile("register.csv"):
        return "0"
    with open("register.csv", "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        return str(len(list(csv_reader)))


def check_user(username):
    with open("register.csv", "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if row["user_name"] == username:
                return row["password"], row["foreign_key"]
    return None, None


def register_user(username, new_password, foreign_key):
    with open("register.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([username, new_password, foreign_key])
    print("Regidtration successful!")
    create_user_task_file(foreign_key)
    print(f"Task file is created for {username}.")

def addtask(username):
    foreignkey = check_user(username)
    task_file_name = f"tasks{foreignkey}.csv"

    task = input("Task description: ")
    date = input("Entrer execution date: (dd/mm/yyyy) ")

    with open(task_file_name, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([task, date])
    print("Task added!")


def display_tasks(username):
    foreignkey = check_user(username)
    task_file_name = f"tasks{foreignkey}.csv"
    with open(task_file_name, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        sorted_tasks = sorted(csv_reader, key=lambda x: x['date'])

        if sorted_tasks:
            headers = ["Task", "Date"]
            task_table = [[task["task"], task["date"]] for task in sorted_tasks]
            print(tabulate(task_table, headers=headers, tablefmt="grid"))
        else:
            print("No tasks to display.")

def main():
    if not os.path.isfile("register.csv"):
        createregister_file()

    username = input("Enter user_name: ")
    password_in_file, foreignkey = check_user(username)

    if password_in_file:
        entered_password = input("Enter password: ")
        if password_in_file == entered_password:
            print("Access granted")

            task_option = input("Add task? (yes/no) ")
            if task_option.lower() == "yes":
                addtask(username) 

            display_option = input("Display tasks? (yes/no) ")
            if display_option.lower() == "yes":
                display_tasks(username)

        else:
            print("Wrong password!")
    else:
        next_foreign_key = get_next_foreign_key()
        register_option = input("Do you want to register? (yes/no) ")
        if register_option.lower() == "yes":
             
            newpassword = input("Enter your password for registation: ")
            register_user(username, newpassword, next_foreign_key)
            addtask(username)
        else:
            print("Access denied. User not registered.")

if __name__ == "__main__":
    main()