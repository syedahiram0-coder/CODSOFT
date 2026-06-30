tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["done"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append({"task": new_task, "done": False})
        print("Task added successfully!")

    elif choice == "3":
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            updated_task = input("Enter updated task: ")
            tasks[index]["task"] = updated_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    elif choice == "6":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")