class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            return "Task cannot be empty"
        self.tasks.append({"task": task, "completed": False})
        return "Task added"

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            return "Invalid index"
        self.tasks[index]["completed"] = True
        return "Task completed"

    def get_tasks(self):
        return self.tasks

    def delete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            return "Invalid index"
        self.tasks.pop(index)
        return "Task deleted"