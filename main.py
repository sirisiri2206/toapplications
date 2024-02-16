def print_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Remove Task")
    print("4. View Tasks")
    print("5. Exit")

def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({"description": description, "status": "Incomplete"})
    print("Task added successfully!")

def complete_task(tasks):
    print("Incomplete Tasks:")
    for i, task in enumerate(tasks):
        if task["status"] == "Incomplete":
            print(f"{i + 1}. {task['description']}")

    task_number = int(input("Enter the task number to mark as complete (or 0 to cancel): "))

    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "Complete"
        print("Task marked as complete!")
    elif task_number != 0:
        print("Invalid task number.")

def remove_task(tasks):
    print("All Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['description']} (Status: {task['status']})")

    task_number = int(input("Enter the task number to remove (or 0 to cancel): "))

    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['description']}' removed successfully!")
    elif task_number != 0:
        print("Invalid task number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nAll Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['description']} (Status: {task['status']})")

def main():
    tasks = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            complete_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            view_tasks(tasks)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
