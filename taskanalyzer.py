class TaskAnalyzer:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self,description,priority,status):
        if not description:
            print("Error: Task description cannot be empty!")
            return 
        if priority not in ["Low","Medium","High"]:
            print("Error: Priority must be Low,  Medium or High.")
            return 
        if status not in ["Pending","In Progress","Completed"]:
            print("Error: Status must be Pending,In Progress, or Completed!")
            return 
        task = {
            "id" : self.next_id ,
            "description" : description,
            "priority" : priority,
            "status" : status
        } 
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task {task['id']} added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return 
        print("\nTasks:")
        for task in self.tasks:
            print(f"ID:{task["id"]} | Description: {task["description"]} | Priority: {task['priority']} | Status: {task['status']}")

    def update_task(self,task_id,description,priority,status):
        if not task:
            print(f"Error: Task ID {task_id} not found!")
        if not description:
            print("Error: Task description cannot be empty!")
            return
        if priority not in ["Low", "Medium", "High"]:
            print("Error: Priority must be Low, Medium, or High!")
            return
        if status not in ["Pending", "In Progress", "Completed"]:
            print("Error: Status must be Pending, In Progress, or Completed!")
            return
        task["description"] = description
        task["priority"] = priority
        task["status"] = status
        print(f"Task {task_id} updated successfully!")

    def delete_task(self,task_id):
        task = next((t for t in self.tasks if t['id'] == task_id),None)
        if not task:
            print(f"Error: Task ID {task_id} not found!")
            return
        self.tasks.remove(task)
        print(f"Task {task_id} deleted successfully!")

    def analyze_tasks(self):
        if not self.tasks:
            print("No tasks to analyze.")
            return 
        priority_counts = {"Low":0 , "Medium":0, "High": 0}
        status_counts = {"Pending": 0, "In Progress": 0, "Completed": 0}
        for task in self.tasks:
            priority_counts[task["priority"]] += 1
            status_counts[task["status"]] += 1
        print("\nTask Analysis:")
        print("Priority Counts:")
        for priority, count in priority_counts.items():
            print(f"{priority}: {count}")
        print("Status Counts:")     
        for status, count in status_counts.items():
            print(f"{status}:{count}")

def main():
    analyzer = TaskAnalyzer()
    while True:
        print("\nTaskAnalyzer Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Analyze Tasks")
        print("6. Exit")
        choice = (input("Enter your choice (1-6): "))

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (Low/Medium/High): ")
            status = input("Enter status (Pending/In Progress/Completed ")
            analyzer.add_task(description,priority,status)
        elif choice == "2":
            analyzer.view_task()
        elif choice == "3":
            try:
                task_id = int(input("Enter task id to update: "))
                description = input("Enter new description: ")
                priority = input("Enter new priority (Low/Medium/High): ")
                status = input("Enter new status (Pending/In Progress/Completed): ")
                analyzer.update_task(task_id,description,priority,status)
            except ValueError:
                print("Error: ID must be a number!")
        elif choice == "4":
            try:
                task_id = int(input("Enter task id to delete"))
            except ValueError:
                print("Error: ID must be a number!")
        elif choice == "5":
            analyzer.analyze_tasks()
        elif choice == "6":
            print("Exiting Task Analyzer!")
            break
        else:
            print("Invalid choice! Please select 1-6.")
if __name__ == "__main__":
    main()