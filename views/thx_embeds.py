import hikari

async def send_success_respond(ctx, option_user):
    embed = hikari.Embed(title="📤 Podziękowanie wysłane", description=f"Twoje podziękowanie dla {option_user} zostało wysłane.")
    embed.set_thumbnail(option_user.avatar_url or option_user.default_avatar_url)
    await ctx.respond(embed, flags=hikari.MessageFlag.EPHEMERAL)