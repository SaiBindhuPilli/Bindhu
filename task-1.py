class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the list.")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
