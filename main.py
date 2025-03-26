import asyncio
import hikari
import lightbulb
from config import DISCORD_BOT_TOKEN
from controllers.youtube_watch import youtube_listener

bot = lightbulb.BotApp(
    token=DISCORD_BOT_TOKEN,
    intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT,
    default_enabled_guilds=(1166065898369589258,)
)

bot.load_extensions_from('./commands')

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    asyncio.create_task(youtube_listener(bot))

bot.run()