# Simple To-Do List in Python

tasks = []  # List to store tasks

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return
    display_tasks()
    try:
        task_no = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_no < len(tasks):
            removed_task = tasks.pop(task_no)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
