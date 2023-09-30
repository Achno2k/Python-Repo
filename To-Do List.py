# Define a Task class to represent individual tasks.
# Each task has a description, completion status, and an optional due date.
class Task:
    def __init__(self, task_text, completed=False, due_date=None):
        self.task_text = task_text
        self.completed = completed
        self.due_date = due_date


# Define a ToDoList class to manage a list of tasks.
class ToDoList:
    def __init__(self):
        self.tasks = []


# Add a new task to the to-do list.
    def add_task(self, task_text):
        task = Task(task_text)
        self.tasks.append(task)
        print("Task added successfully!")


# View all tasks in the to-do list.
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTasks:")
            for i, task in enumerate(self.tasks, 1):
                status = " [X]" if task.completed else " [ ]"
                due_date = f" (Due: {task.due_date})" if task.due_date else ""
                print(f"{i}.{status} {task.task_text}{due_date}")


# Mark a task as complete.
    def mark_task_complete(self, task_number):
        task_number -= 1
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].completed = True
            print("Task marked as complete!")
        else:
            print("Invalid task number. Please select a valid task.")


# Edit a task.
    def edit_task(self, task_number, new_task_text):
        task_number -= 1
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].task_text = new_task_text
            print("Task edited successfully!")
        else:
            print("Invalid task number. Please select a valid task.")


# Set a due date for a task.
    def set_due_date(self, task_number, due_date):
        task_number -= 1
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].due_date = due_date
            print("Due date set successfully!")
        else:
            print("Invalid task number. Please select a valid task.")


# Delete completed tasks from the list.
    def delete_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]
        print("Completed tasks deleted!")


# Save tasks to a file.
    def save_tasks_to_file(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                completed = "1" if task.completed else "0"
                due_date = task.due_date if task.due_date else ""
                file.write(f"{completed}|{task.task_text}|{due_date}\n")
        print(f"Tasks saved to '{filename}'")


# Load tasks from a file.
    def load_tasks_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.tasks = []
                for line in file:
                    completed, task_text, due_date = line.strip().split("|")
                    completed = bool(int(completed))
                    self.tasks.append(Task(task_text, completed, due_date if due_date else None))
            print(f"Tasks loaded from '{filename}'")
        except FileNotFoundError:
            print("No saved tasks found.")


# This function is the main entry point for the program.
# It creates a to-do list object and then enters a loop, 
# where it prompts the user to select a menu option. 
# The function then performs the selected operation, 
# such as adding a new task, viewing the list of tasks, 
# or saving the tasks to a file.
#  The loop repeats until the user selects the "Exit" option.
def main():
    todo_list = ToDoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Edit Task")
        print("5. Set Due Date for Task")
        print("6. Delete Completed Tasks")
        print("7. Save Tasks to File")
        print("8. Load Tasks from File")
        print("9. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            task_text = input("Enter a task: ")
            todo_list.add_task(task_text)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as complete: "))
            todo_list.mark_task_complete(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to edit: "))
            new_task_text = input("Enter the new task text: ")
            todo_list.edit_task(task_number, new_task_text)
        elif choice == "5":
            task_number = int(input("Enter the task number to set a due date for: "))
            due_date = input("Enter the due date (e.g., YYYY-MM-DD): ")
            todo_list.set_due_date(task_number, due_date)
        elif choice == "6":
            todo_list.delete_completed_tasks()
        elif choice == "7":
            filename = input("Enter the filename to save tasks to (e.g., tasks.txt): ")
            todo_list.save_tasks_to_file(filename)
        elif choice == "8":
            filename = input("Enter the filename to load tasks from (e.g., tasks.txt): ")
            todo_list.load_tasks_from_file(filename)
        elif choice == "9":
            print("Exiting the Todo List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7/8/9).")

if __name__ == "__main__":
    main()


