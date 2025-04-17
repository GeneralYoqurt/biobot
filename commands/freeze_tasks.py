import hikari
import lightbulb
from config import MODERATOR_ROLE_ID
import state

plugin = lightbulb.Plugin("freeze")

@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(role1=MODERATOR_ROLE_ID))
@lightbulb.command("freeze", "Zamroź zadania bota i ustaw status DND (NA RAZIE ZAMRAŻA TYLKO TASK YOUTUBE_WATCH)", ephemeral=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def freeze_command(ctx: lightbulb.Context) -> None:
    """Zamraża zadania bota i ustawia status DND. (NA RAZIE ZAMRAŻA TYLKO TASK YOUTUBE_WATCH)"""
    # Zatrzymujemy wszystkie zadania
    if state.async_tasks:
        state.async_tasks.freeze_tasks()
    # Zmieniamy obecność bota
    await ctx.bot.update_presence(
        status=hikari.Status.IDLE
    )
    await ctx.respond("Zatrzymano zadania i ustawiono status DND.")

def load(bot):
    bot.add_plugin(plugin)