# Project Name : To-Do Console App
# Author : Roman Zapatmar
# Date : 10 June 2025

# Show menu
def show_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No Task Found")
    else:
        for index, task in enumerate(tasks, 1):
            status = "Complete" if task["done"] else "Incomplete"
            print(f"{index}. {task['name']} [{status}]")

# Add task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title != "":  # or simply: if title:
        tasks.append({"name": title, "done": False})
        print(f"Task '{title}' added.")
    else:
        print("Task title cannot be empty.")

# Mark task complete
def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Task '{tasks[index]['name']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"Deleted task: {deleted['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        int(print("Please enter a valid number."))

# Main app loop
def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main()
