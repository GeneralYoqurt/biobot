import hikari
import lightbulb
from config import DISCORD_BOT_TOKEN, DEFAULT_ENABLED_GUILD_ID
from youtube_watch import youtube_listener
from controllers.async_tasks import AsyncTasks
import miru
import state

bot = lightbulb.BotApp(
    token=DISCORD_BOT_TOKEN,
    intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT | hikari.Intents.GUILD_MEMBERS,
    owner_ids={398152024014716938},
    default_enabled_guilds=DEFAULT_ENABLED_GUILD_ID
)

client = miru.Client(bot)

bot.load_extensions_from('./commands')

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    state.async_tasks = AsyncTasks(variables={'bot': bot})
    state.async_tasks.run_tasks([youtube_listener])
    state.bot = bot
    state.client = client

    import events

bot.run(status=hikari.Status.ONLINE, activity=hikari.Activity(name="Check bio", type=hikari.ActivityType.CUSTOM))