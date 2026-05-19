# Simple To-Do List Program

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()

    choice = input("Enter your choice: ")

    # Add task
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            number = int(input("Enter task number to remove: "))

            if number > 0 and number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(removed, "removed successfully!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Exiting program...")
        break

    # Invalid choice
    else:
        print("Invalid choice. Try again.")