import hikari
import lightbulb
from config import DISCORD_BOT_TOKEN
from controllers.youtube_watch import youtube_listener
from async_tasks import AsyncTasks
import state

bot = lightbulb.BotApp(
    token=DISCORD_BOT_TOKEN,
    intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT
)

bot.load_extensions_from('./commands')

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    state.async_tasks = AsyncTasks(variables={'bot': bot})
    state.async_tasks.run_tasks([youtube_listener])

bot.run(status=hikari.Status.ONLINE, activity=hikari.Activity(name="Check bio", type=hikari.ActivityType.CUSTOM))