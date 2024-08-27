import hikari
import lightbulb
from dotenv import load_dotenv
import os

# Sprawdź, który plik .env istnieje i załaduj go
if os.path.exists('.env.dev'):
    load_dotenv('.env.dev')
elif os.path.exists('.env.prod'):
    load_dotenv('.env.prod')
else:
    raise FileNotFoundError('Brak pliku .env.dev lub .env.prod')

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = lightbulb.BotApp(token = BOT_TOKEN, intents = hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT, default_enabled_guilds = (1166065898369589258))

bot.load_extensions_from('./commands')

bot.run()