import hikari
import lightbulb
from utils import load_dotenv
import os

# Załaduj plik env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = lightbulb.BotApp(token = BOT_TOKEN, intents = hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT, default_enabled_guilds = (1166065898369589258))

bot.load_extensions_from('./commands')

bot.run()