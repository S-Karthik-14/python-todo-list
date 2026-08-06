tasks = []


def display_menu():
    print("------------------TO-DO-LIST------------------\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def add_tasks():
    add = str(input("Enter the task to be added :"))
    tasks.append(add)
    print(f" '{add}' has been successfully added into the list! ")


def view_tasks():
    print("This is the list of tasks in your TO-DO list: ")
    for task in tasks:
        print(task)


def complete_tasks():
    view_tasks()
    task_number = int(input("Enter the number of the task that you have completed: "))
    current_task = tasks[task_number - 1]
    tasks[task_number - 1] = f"✓ {current_task}"
    print("Task marked as completed!")


def delete_tasks():
    view_tasks()
    task_number = int(input("Enter the number of the task that you want to delete: "))
    tasks.pop(task_number - 1)
    print("Task deleted successfully!")


def exit():
    return


def main():
    while True:
        display_menu()
        user_input = int(input("Choose an option in number: "))
        if user_input == 5:
            print("Thank you for using the To-Do List!")
            break
        check_opt(user_input)


def check_opt(user_input):
    if user_input == 1:
        add_tasks()
    elif user_input == 2:
        view_tasks()
    elif user_input == 3:
        complete_tasks()
    elif user_input == 4:
        delete_tasks()
    else:
        print("Invalid option!")


main()






