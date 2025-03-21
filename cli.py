from taskmanager import TaskManager

class CLI:
    def __init__(self):
        """sets manager as an object representing TaskManager class"""
        self.manager = TaskManager()

    def run(self):
        while True:
            print("\nTask Manager")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Update Task")
            print("4. Mark Task as Completed")
            print("5. Delete Task")
            print("6. Exit")
            choice = input("Choose an option (1-6):")

            try:
                if choice == "1":
                    self.add_task()
                elif choice == "2":
                    self.list_tasks()
                elif choice == "3":
                    self.update_task()
                elif choice == "4":
                    self.mark_task_completed()
                elif choice == "5":
                    self.delete_task()
                elif choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    def add_task(self):
        try:
            priority_values = ["Low", "Medium", "High"]
            status_values = ["Pending", "In Progress", "Completed"]
            title = input("\nEnter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority_level = input("Enter priority level (Low/Medium/High): ").title()
            status = input("Enter status (Pending/In Progress/Completed): ").title()

            if priority_level not in priority_values:
                raise ValueError("Priority level must be Low, Medium, or High.")
            if status not in status_values:
                raise ValueError("Status must be Pending, In Progress, or Completed.")

            self.manager.add_task(title, description, due_date, priority_level, status)
            print("Task added successfully!")
        except Exception as e:
            print(f"Error adding task: {e}")

    def list_tasks(self):
        try:
            filter_by = input("\nFilter by (priority_level/status/due_date) or leave blank for all tasks: ")

            if filter_by:
                if filter_by == "priority_level":
                    filter_value = input(f"Enter {filter_by} (Low/Medium/High): ").title()
                elif filter_by == "status":
                    filter_value = input(f"Enter {filter_by} (Pending/In Progress/Completed): ").title()
                else:
                    filter_value = input(f"Enter {filter_by}: ")
            else:
                filter_value = None

            tasks = self.manager.list_tasks(filter_by, filter_value)
            for task in tasks:
                print(task)
        except Exception as e:
            print(f"Error listing tasks: {e}")

    def update_task(self):
        try:
            task_id = int(input("\nEnter task ID to update: "))
            title = input("Enter new title (leave blank to skip): ")
            description = input("Enter new description (leave blank to skip): ")
            due_date = input("Enter new due date (YYYY-MM-DD, leave blank to skip): ")
            priority_level = input("Enter new priority level (Low/Medium/High, leave blank to skip): ").title()
            status = input("Enter new status (Pending/In Progress/Completed, leave blank to skip): ").title()

            updates = {}
            if title: updates["title"] = title
            if description: updates["description"] = description
            if due_date: updates["due_date"] = due_date
            if priority_level: updates["priority_level"] = priority_level
            if status: updates["status"] = status

            self.manager.update_task(task_id, **updates)       #makes it so that **kwargs from update_task can accept the updates dictionary
            print("Task updated successfully!")
        except Exception as e:
            print(f"Error updating task: {e}")

    def mark_task_completed(self):
        try:
            task_id = int(input("\nEnter task ID to mark as completed: "))
            self.manager.mark_task_completed(task_id)
            print("Task marked as completed!")
        except Exception as e:
            print(f"Error marking task as completed: {e}")

    def delete_task(self):
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            self.manager.delete_task(task_id)
            print("Task deleted successfully!")
        except Exception as e:
            print(f"Error deleting task: {e}")