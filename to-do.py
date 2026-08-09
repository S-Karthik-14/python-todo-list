tasks = []

def display_menu():
    print("====================================================\n")
    print("------------------TO-DO-LIST------------------\n")
    print("====================================================\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Search Tasks")
    print("7. Exit\n")
    print("====================================================\n")
    
def add_tasks():
    while True: 
        add = str(input("Enter the task to be added :")).strip()
        if add == "":
            print("Task cannot be empty!")
            print("Try again...")
            continue
        else:
            tasks.append(add)
            print(f" '{add}' has been successfully added into the list! ")
            break
    
def view_tasks():
    if tasks == [] :
        print("No tasks available!")
    else:
        print("This is the list of tasks in your TO-DO list: ")
        for index, task in enumerate(tasks,1) :
            print(f"{index}.  {task}")

def complete_tasks():
    while True:
        if tasks == []:
            print("No tasks available!")
            return
        else:
            view_tasks()
        try:
            task_number = int(input("Enter the number of the task that you have completed: "))
        except ValueError:
            print("Invalid input!")
            print (f"Please enter a task number between 1 and {len(tasks)}.")
            print("Decimals, special characters,letters and blank input not permitted")
            print("Try again...")
            continue
            
        if task_number < 1 or task_number > len(tasks):
            print("Invalid input!")
            print(f"Please enter a task number between 1 and {len(tasks)}.")
            print("Try again...")
            continue
        else:
            current_task = tasks[task_number - 1]
            if "✓" in current_task:
                 print("Task has already been completed!")
                 continue
            tasks[task_number - 1] = f"✓ {current_task}"
            print("Task marked as completed!")
            break
    
def delete_tasks():
    while True:
        if tasks == []:
            print("No tasks available!")
            return
        else:
            try:
                view_tasks()
                task_number = int(input("Enter the number of the task that you want to delete: "))
            except ValueError:
                print("Invalid input!")
                print (f"Please enter a task number between 1 and {len(tasks)}.")
                print("Decimals, special characters,letters and blank input not permitted")
                print("Try again...") 
                continue
            if task_number < 1 or task_number > len(tasks):
                print("Invalid input!")
                print (f"Please enter a task number between 1 and {len(tasks)}.")
                print("Try again...")
                continue
            else:
                tasks.pop(task_number - 1)
                print("Task deleted successfully!")
                break
            
def edit_tasks():
     while True:
        if tasks == []:
            print("No tasks available!")
            return
        else:
            try:
                view_tasks()
                task_number = int(input("Enter the number of the task that you want to edit: "))
            except ValueError:
                print("Invalid input!")
                print (f"Please enter a task number between 1 and {len(tasks)}.")
                print("Decimals, special characters,letters and blank input not permitted")
                print("Try again...") 
                continue
            if task_number < 1 or task_number > len(tasks):
                print("Invalid input!")
                print (f"Please enter a task number between 1 and {len(tasks)}.")
                print("Try again...")
                continue  
            current_task = tasks[task_number - 1] 
            while True:
                new_task = input("Enter the new task: ").strip()
                if new_task == "":
                    print("Task cannot be empty!")
                    print("Try again...")
                    continue
                break
            if "✓" in current_task:
                    new_task = "✓ " + new_task
            tasks[task_number - 1] = new_task
            print("Task edited successfully!")
            print("You can view the new list by clicking view list")
            break




def search_tasks():
    if tasks == []:
        print("No tasks available!")
        return

    search_term = input("Enter the term you want to search: ").strip()

    found = False

    for task in tasks:
        if search_term in task:
            print(task)
            found = True

    if not found:
        print("Task not found!")
 
 
 
    
def exit():
    return
    
def main():
    while True: 
        display_menu()
        try:
            user_input = int(input("Choose an option in number: "))
        except ValueError:
            print("Invalid Input!")
            print("Only numbers 1 to 7 are allowed.")
            print("Decimals, special characters,letters and blank input not permitted")
            print("Try again...")
            continue
        if user_input < 1 or user_input > 7:
            print("Invalid input choose from (1 to 7)! ")
            print("Try again...")
            continue
        elif user_input == 7:
           print("Thank you for using the TO-DO list")
           break
        check_opt(user_input)


def check_opt(user_input):
    if user_input == 1 :
        add_tasks()
    elif user_input == 2 :
        view_tasks()
    elif user_input == 3:
        complete_tasks()
    elif user_input == 4:
        delete_tasks()
    elif user_input == 5:
        edit_tasks()
    elif user_input == 6:
        search_tasks()
    else:
        print("Invalid option!")


main()
