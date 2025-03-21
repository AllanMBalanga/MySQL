from task import Task
from database import Database

#add_task, list_tasks, update_task, delete_task, and mark_task_completed using database.py functionalities

class TaskManager:
    def __init__(self):
        """sets db as an object to represent Database class to handle interaction with the database such as executing queries, fetching all rows"""

        self.db = Database()


    def add_task(self, title, description, due_date, priority_level, status):
        """handles the adding of tasks in the table"""

        if not title or not priority_level or not status:
            raise ValueError("Title, priority level, and status are required.")
        query = "INSERT INTO tasks (title, description, due_date, priority_level, status) VALUES (%s, %s, %s, %s, %s)"
        values = (title, description, due_date, priority_level, status)
        self.db.execute_query(query, values)                                   #executes query (insert) and replaces %s with values tuple


    def list_tasks(self, filter_by=None, filter_value=None):
        """returns tasks based on the lists inside valid_filters"""

        valid_options = ["priority_level", "status", "due_date"]
        if filter_by and filter_by not in valid_options:                       #checks first if filter_by is not None, then checks whether filter_by is not in valid_options
            raise ValueError(f"Invalid filter. Allowed filters: {valid_options}")
        query = "SELECT * FROM tasks"
        if filter_by and filter_value:
            query += f" WHERE {filter_by} = %s"                                #becomes SELECT * FROM tasks WHERE (priority_level/status/due_date) = %s
            tasks = self.db.fetch_all(query, (filter_value,))           #fetches query and replacing %s with the filter value as tuples
        else:
            tasks = self.db.fetch_all(query)

        #unpacks each tuple to insert into Task class from task.py
        return [Task(*task) for task in tasks]


    def update_task(self, task_id, **kwargs):
        """Updates a specific task depending on the task_id and the column/s to be updated in the task_id. **kwargs is key-value pairs"""

        if not task_id:
            raise ValueError("Task ID is required.")
        valid_options = ["title", "description", "due_date", "priority_level", "status"]
        for key in kwargs:
            if key not in valid_options:
                raise ValueError(f"Invalid field: {key}. Allowed fields: {valid_options}")
        keys = ", ".join([f"{key} = %s" for key in kwargs])                 #replaces f-string with each key from kwargs and separates each by comma
        query = f"UPDATE tasks SET {keys} WHERE task_id = %s"               #becomes UPDATE tasks SET (title = %s, description = %s,...) WHERE task_id = %s
        values = list(kwargs.values()) + [task_id]                          #gets the values from kwargs and task_id as a list
        self.db.execute_query(query, values)                                #executes the function, taking the statements (query) and replacing {keys} & %s using the values list


    def delete_task(self, task_id):
        if not task_id:
            raise ValueError("Task ID is required.")
        query = "DELETE FROM tasks WHERE task_id = %s"
        self.db.execute_query(query, (task_id,))                     #executes the query (delete) based from the task_id


    def mark_task_completed(self, task_id):
        if not task_id:
            raise ValueError("Task ID is required.")
        self.update_task(task_id, status="Completed")                      #executes the query (update as "Completed") based from the task_id