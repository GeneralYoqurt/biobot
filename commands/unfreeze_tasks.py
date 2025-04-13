import hikari
import lightbulb
import state

plugin = lightbulb.Plugin("unfreeze")

@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)  # tylko właściciel może używać tej komendy
@lightbulb.command("unfreeze", "Odmróż zadania bota i ustaw status na Online", ephemeral=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def freeze_command(ctx: lightbulb.Context) -> None:
    """Zamraża zadania bota i ustawia status DND."""
    # Zatrzymujemy wszystkie zadania
    if state.async_tasks:
        state.async_tasks.unfreeze_tasks()
    # Zmieniamy obecność bota
    await ctx.bot.update_presence(
        status=hikari.Status.ONLINE
    )
    await ctx.respond("Odmrożono zadania bota i ustawiono status na Online.")

def load(bot):
    bot.add_plugin(plugin)