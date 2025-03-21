class Task:
    def __init__(self, task_id, title, description, due_date, priority_level, status, creation_timestamp):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority_level = priority_level
        self.status = status
        self.creation_timestamp = creation_timestamp

    def __str__(self):
        return f"Task ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority_level}\nStatus: {self.status}\nCreated: {self.creation_timestamp}\n"