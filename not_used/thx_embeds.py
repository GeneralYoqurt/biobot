import hikari
from controllers import get_config

async def send_success_respond(ctx, option_user):
    embed = hikari.Embed(title="📤 Podziękowanie wysłane", description=f"<@{option_user.id}> dostaje podziękowanie", color=hikari.Color(0x86d173))
    embed.set_thumbnail(option_user.avatar_url or option_user.default_avatar_url)

    await ctx.respond(embed)


async def send_log_message(ctx, option_user, channel_function = 'log_reputation'):
    embed = hikari.Embed(title="➕ Nowe podziękowanie")
    embed.add_field(name="Dostający", value=f'\n<@{option_user.id}>', inline=False)
    embed.add_field(name='\u200B', value='---------------------', inline=False)
    embed.add_field(name="Wysyłający", value=f'<@{ctx.author.id}>', inline=False)
    embed.set_thumbnail(option_user.avatar_url or option_user.default_avatar_url)

    # TODO: Dodać przyciski
    
    # TODO: Dodać obsługę przycisków w "events"

    channel = await get_config.channel(ctx, channel_function)
    if channel:
        await ctx.app.rest.create_message(channel.id, embed=embed)
