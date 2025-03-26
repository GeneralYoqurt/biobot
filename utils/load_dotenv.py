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