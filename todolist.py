import json

file_name = "tasks.json"#it is the file name where the tasks will be stored in JSON format


def load_tasks():#function to load the tasks from file 
    try:
        with open(file_name, "r") as file:#try to open the file in read mode
            tasks = json.load(file)
    except:#if file does not exist return empty list of tasks
        tasks = []
    return tasks


def save_tasks(tasks):#function to save the tasks to file
    with open(file_name, "w") as file:#open file in write mode
        json.dump(tasks, file)


def add_task(tasks):#function to add task 
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})#take input from user, append and then save
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):#function to view tasks

    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")

        for i in range(len(tasks)):

            status = "Done" if tasks[i]["done"] else "Not Done"

            print(i + 1, ".", tasks[i]["task"], "-", status)


def delete_task(tasks):#function to delete task from file 

    view_tasks(tasks)

    num = int(input("Enter task number to delete: "))

    if num <= len(tasks):

        tasks.pop(num - 1)

        save_tasks(tasks)

        print("Task deleted!")


def mark_done(tasks):#function to mark as done

    view_tasks(tasks)

    num = int(input("Enter task number to mark done: "))

    if num <= len(tasks):

        tasks[num - 1]["done"] = True

        save_tasks(tasks)

        print("Task marked as done!")


tasks = load_tasks()#main program 

while True:
    #tasks menu will be displayed 
    print("\n===== TO DO LIST MENU =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Done")
    print("5. Exit")

    choice = input("Enter choice: ")#user selects an option from menu and perfoms the operation 

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        mark_done(tasks)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

