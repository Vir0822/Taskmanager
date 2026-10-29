from task_manager import TaskManager


def print_menu():
        print("\n--- Smart Task Manager ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

def main():
    manager = TaskManager()

    while True:

        print_menu()


        choice = input("Choose an option: ")

        match choice:
            case "1":
                description = input("Description of the task: ")
                if description.strip():
                    manager.add_task(description)
                else:
                    print("The description cannot be empty.")
            case "2":
                manager.list_tasks()
            case "3":
                id = input("ID of the task to complete: ")
                if id.isdecimal():
                    manager.complete_task(int(id))
                else:
                    print("Invalid ID, please enter a number.")
            case "4":
                id = input("ID of the task to delete: ")
                if id.isdecimal():
                    manager.delete_task(int(id))
                else:
                    print("Invalid ID, please enter a number.")
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid option, please select another.")


if __name__ == "__main__":
    main()