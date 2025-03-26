import os
import pyodbc
from utils.load_dotenv import load_dotenv
from config import *

class Database:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.connection = None
        self.cursor = None

    def __enter__(self):
        conn_str = (
            f"DRIVER={{{DB_DRIVER}}};"
            f"SERVER={DB_SERVER};"
            f"DATABASE={DB_DATABASE};"
            f"UID={DB_USER};"
            f"PWD={DB_PASSWORD};"
            f"PORT={DB_PORT};"
        )
        try:
            self.connection = pyodbc.connect(conn_str)
            self.cursor = self.connection.cursor()
            print("Connection successful.")
        except pyodbc.Error as e:
            print("Error occurred:", e)
            raise e
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Database connection closed.")

    def get_cursor(self):
        if not self.connection or not self.cursor:
            raise Exception("No active database connection.")
        return self.cursor