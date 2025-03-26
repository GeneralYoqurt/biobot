import asyncio
import hikari
import lightbulb
from config import DISCORD_BOT_TOKEN
from controllers.youtube_watch import youtube_listener

bot = lightbulb.BotApp(
    token=DISCORD_BOT_TOKEN,
    intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT
)

bot.load_extensions_from('./commands')

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    asyncio.create_task(youtube_listener(bot))

bot.run()
