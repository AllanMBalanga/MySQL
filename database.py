import mysql.connector
from mysql.connector import Error
from config import database

class Database:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host=database["host"],
                user=database["user"],
                password=database["password"],
                database=database["database"]
            )
            self.mycursor = self.db.cursor()
            print("Database successfully connected!")
        except Error as e:
            print(f"Database error connection: {e}")
            raise

    def execute_query(self, query, values=None):
        try:
            self.mycursor.execute(query, values)
            self.db.commit()
            print("Successful query!")
        except Error as e:
            print(f"Query error: {e}")
            raise

    def fetch_all(self, query, values=None):
        try:
            self.mycursor.execute(query, values)
            return self.mycursor.fetchall()
        except Error as e:
            print(f"Data error: {e}")
            raise

    def __del__(self):
        if self.db.is_connected():
            self.mycursor.close()
            self.db.close()
            print("Database connection closed.")

