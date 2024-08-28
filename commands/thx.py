import hikari
import lightbulb
from views import thx_embeds

plugin = lightbulb.Plugin('Thanks Command')

@plugin.command
@lightbulb.option("użytkownik", "Wybierz komu chcesz podziękować", type=hikari.User, required=True)
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.command('thx', 'Obdaruj kogoś punktami reputacji za pomoc')
@lightbulb.implements(lightbulb.SlashCommand)

async def thx(ctx):
    option_user = ctx.options.użytkownik

# Sprawdź czy użytkownik dziękuję samemu sobie, jeżeli tak to odrzuć.
    if option_user.id == ctx.author.id:
        await ctx.respond(
        f"**Nie możesz podziękować samemu sobie**",
        flags=hikari.MessageFlag.EPHEMERAL
    )
        
    # Odpowiedz, że udało się wysłać podziękowanie.
    await thx_embeds.send_success_respond(ctx, option_user)

    # Wyślij na kanał do logowania wiadomość dla moderacji o wysłanym podziękowaniu.
    await thx_embeds.send_log_message(ctx, option_user)


def load(bot):
    bot.add_plugin(plugin)