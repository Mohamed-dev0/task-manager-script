def load_tasks_from_file(filename):
    import json, os
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        print("The file exists but the content is not a valid JSON.")
        return []
    except Exception as e:
        print(f"Error when reading file: {e}")
        return []

def save_tasks_to_file(filename, tasks):
    import json
    try:
        with open(filename, 'w') as f:
            json.dump(tasks, f)
    except Exception as e:
        print(f"Error writing file : {e}")



class Menu:

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = load_tasks_from_file(self.filename)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def show_menu(self):
        print("\n=== MENU ===")
        print("0. Add a task")
        print("1. List the tasks")
        print("2. Marked a task as completed")
        print("3. Delete the task")
        print("4. Leave")

    def add_task(self):
        name_task = input("Type the name task: ")
        self.tasks.append(name_task)
        save_tasks_to_file(self.filename, self.tasks)
        return f"Task '{name_task}' has been added."

    def mark_task_as_completed(self):
        number_task = input("Enter the number of the task to be marked as completed: ")
        try:
            index = int(number_task)
        except ValueError:
            return "Invalid input. Please enter a number."

        if 0 <= index < len(self.tasks):
            self.tasks[index] += " (completed)"
            save_tasks_to_file(self.filename, self.tasks)
            return "This task is completed"
        else:
            return "This task doesn't exist."


    def delete_task(self):
        number_task = input("Enter the number of the task to be delete:")
        try:
            index = int(number_task)
        except ValueError:
            return "Invalid input. Please enter a number."


        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            save_tasks_to_file(self.filename, self.tasks)
            return f"This task is deleted."
        else:
            return f"This task doesn't exist."


    def exit_menu(self):
        return "You left the menu"






m = Menu()

while True:

    m.show_menu()
    user_choice = input("Enter your choice : ")

    if user_choice == "0":
        print(m.add_task())
    elif user_choice == "1":
        m.list_tasks()
    elif user_choice == "2":
        print(m.mark_task_as_completed())
    elif user_choice == "3":
        print(m.delete_task())
    elif user_choice == "4":
        print(m.exit_menu())
        break
    else:
        print("Invalid choice, try again.")
