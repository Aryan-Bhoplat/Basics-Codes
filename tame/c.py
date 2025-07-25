import os
import json
from datetime import datetime

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from file if it exists"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                print("Error loading tasks file. Starting with empty task list.")
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, description, priority="medium"):
        """Add a new task to the list"""
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "completed": False,
            "priority": priority,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {description}")

    def view_tasks(self, show_completed=False):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n===== YOUR TO-DO LIST =====")
        
        # Filter tasks based on completion status
        filtered_tasks = self.tasks
        if not show_completed:
            filtered_tasks = [task for task in self.tasks if not task["completed"]]
            
        if not filtered_tasks:
            print("No tasks to display.")
            return
            
        # Sort tasks by priority
        priority_order = {"high": 1, "medium": 2, "low": 3}
        filtered_tasks.sort(key=lambda x: priority_order.get(x["priority"], 4))
        
        for task in filtered_tasks:
            status = "✓" if task["completed"] else "□"
            priority_symbol = {
                "high": "!!! ",
                "medium": "!! ",
                "low": "! "
            }.get(task["priority"], "")
            
            print(f"{task['id']}. [{status}] {priority_symbol}{task['description']}")
            
        print("==========================\n")

    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task from the list"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()
                print(f"Task deleted: {deleted_task['description']}")
                return
        print(f"Task with ID {task_id} not found.")

    def update_task(self, task_id, new_description=None, new_priority=None):
        """Update task description or priority"""
        for task in self.tasks:
            if task["id"] == task_id:
                if new_description:
                    task["description"] = new_description
                if new_priority:
                    task["priority"] = new_priority
                self.save_tasks()
                print(f"Task {task_id} updated successfully!")
                return
        print(f"Task with ID {task_id} not found.")


def main():
    app = TodoApp()
    
    while True:
        print("\n==== TO-DO APP ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. View All Tasks (including completed)")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Update Task")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (high/medium/low) [default: medium]: ").lower()
            if priority not in ["high", "medium", "low"]:
                priority = "medium"
            app.add_task(description, priority)
            
        elif choice == '2':
            app.view_tasks()
            
        elif choice == '3':
            app.view_tasks(show_completed=True)
            
        elif choice == '4':
            app.view_tasks(show_completed=True)
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                app.complete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID (number).")
                
        elif choice == '5':
            app.view_tasks(show_completed=True)
            try:
                task_id = int(input("Enter task ID to delete: "))
                app.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID (number).")
                
        elif choice == '6':
            app.view_tasks(show_completed=True)
            try:
                task_id = int(input("Enter task ID to update: "))
                new_description = input("Enter new description (leave empty to keep current): ")
                new_priority = input("Enter new priority (high/medium/low) (leave empty to keep current): ").lower()
                
                if new_priority and new_priority not in ["high", "medium", "low"]:
                    new_priority = None
                    
                app.update_task(task_id, 
                               new_description if new_description else None,
                               new_priority if new_priority else None)
            except ValueError:
                print("Please enter a valid task ID (number).")
                
        elif choice == '7':
            print("Thank you for using the To-Do App. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()