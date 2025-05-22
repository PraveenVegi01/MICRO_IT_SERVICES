tasks = []

def show_menu():
    print("\n----- To-Do List -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")

    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
            try:
                delete_index = int(input("Enter task number to delete: ")) - 1
                if 0 <= delete_index < len(tasks):
                    deleted = tasks.pop(delete_index)
                    print(f"Deleted: {deleted}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
