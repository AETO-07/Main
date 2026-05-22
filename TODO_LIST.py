import json
tasks = []

def save_tasks():
    with open("tasks.json", "w") as myfile:
        json.dump(tasks, myfile)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as myfile:
            tasks = json.load(myfile)
    except FileNotFoundError:
        tasks = []

load_tasks()


while True:
    print("\n--- TODO MENU ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    takeResponse = input("Choose an Option: ")

    if takeResponse == "1":
        task = input("Enter task: ")
        tasks.append({"text" : task, "done" : False})
        save_tasks()

    elif takeResponse == "2":
        if not tasks:
            print("No tasks yet")

        else:
            for i, task in enumerate(tasks):
                status = "✔️" if task["done"] else "❌"
                print(f"{i}: {task['text']} [{status}]")

    elif takeResponse == "3":
        try:
            position = int(input("Enter task number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if 0 <= position < len(tasks):
            tasks[position]["done"] = True
            save_tasks()
        else:
            print("Invalid Index")

    elif takeResponse == "4":
        try:
            position = int(input("Enter Task number to delete: "))
        except ValueError:
            print("Enter a valid number!")

        if 0 <= position < len(tasks):
            tasks.pop(position)
            save_tasks()
        else:
            print("Invalid index")

    elif takeResponse == "5":
        break