from dotenv import load_dotenv as load
import os

# Sprawdź, który plik ".env" istnieje i załaduj go.
def load_dotenv():
        if os.path.exists('.env.dev'):
            print('Aplikacja działa na zmiennych DEV')
            load('.env.dev')
        elif os.path.exists('.env.prod'):
            print('Aplikacja działa na zmiennych PROD')
            load('.env.prod')
        else:
            raise FileNotFoundError('Brak pliku .env.dev lub .env.prod')
        
import pyodbc
import time

class Database:
    def __init__(self):
        
        
        # Wczytaj zmienne środowiskowe z pliku .env.(konfiguracja).
        load_dotenv()

        # Uzyskaj wartości zmiennych.
        driver = os.getenv('DRIVER')
        server = os.getenv('SERVER')
        database = os.getenv('DATABASE')
        user = os.getenv('USER')
        password = os.getenv('PASSWORD')
        port = os.getenv('PORT')

        # Connection string.
        conn_str = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={user};"
            f"PWD={password};"
            f"PORT={port};"
        )

        self.connection = None
        self.cursor = None

        # Ponów próbę połączenia określoną liczbę razy.
        retries = 2
        attempt = 0
        while attempt < retries:
            try:
                # Stwórz połączenie z bazą SQL.
                self.connection = pyodbc.connect(conn_str)
                self.cursor = self.connection.cursor()
                print("Connection successful.")
                break  # Przerwij pętlę jeśli połączenie się udało.

            except pyodbc.Error as e:
                print(f"Error occurred: {e}")
                attempt += 1
                print(f"Retrying {attempt}/{retries}...")
                time.sleep(1)  # Opóźnienie przed ponowną próbą.

        if not self.connection or not self.cursor:
            print("Operation failed after multiple attempts.")
            raise Exception("Could not establish database connection.")

    def get_cursor(self):
        if not self.connection or not self.cursor:
            raise Exception("No active database connection.")
        return self.cursor

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Database connection closed.")