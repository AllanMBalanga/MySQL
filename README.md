# MySQL
Task Manager Database
an application that allows user to interact with a MySQL database. The functionalities of the application include:

adding - add new task with title, description, due date, priority level (low, medium, high), and status(pending, in progress, completed), 
listing - lists tasks with optional filtering (due date, priority, status), 
updating - update task details(title, description, due date, priority, status), 
marking tasks as completed, and 
deleting tasks.

**Setup Instructions**
1. Prerequisites:
Python 3.x
MySQL

2. Clone Repository
git clone https://github.com/your-username/task-management-app.git
cd task-management-app

3. Install on Bash
pip install mysql-connector-python

4. Run on Bash
mysql -u root -p < schema.sql

5. Update config.py with your database information

database = {
"host": "localhost",
"user": "root",
"password": "your_password",
"database": "TaskManagement"
}

6. Run the Application on Bash
python main.py
 
