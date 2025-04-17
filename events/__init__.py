import lightbulb
import hikari
from config import CHANNEL_INTRODUCE_ID, LOGGING_VERIFICATION_CHANNEL_ID, ROLE_VERIFIED_USER
from state import bot, client

@bot.listen(hikari.MemberUpdateEvent)
async def on_member_create(event: hikari.MemberCreateEvent) -> None:
    """Event handler for when a member joins the server."""
    from views.welcome_message import welcome_message
    # Get the member who joined
    member = event.member
    # Get the guild (server) where the member joined
    guild = event.get_guild()

    channel = guild.get_channel(CHANNEL_INTRODUCE_ID)

    # Check if the member is a bot
    if member.is_bot:
        return  
    
    # Send a welcome message to the member in their DMs
    await member.send(attachment="images/weryfikacja.png")
    await member.send(welcome_message(member=member, guild=guild, channel=channel))


    if channel:
        message = await channel.send(f"Witamy {member.mention} na serwerze!", user_mentions=True)
        await message.delete()  # Delete the message after 5 seconds


@bot.listen(hikari.MessageCreateEvent)
async def on_message_create(event: hikari.MessageCreateEvent) -> None:
    """Event handler for when a message is created on introduce channel."""
    from views.verification import verification_message, VerificationView
    # Check if the message is in a guild (server)
    if event.is_human and event.channel_id == CHANNEL_INTRODUCE_ID:
        event.message.add_reaction("❤️")

        # Get the member who sent the message
        member = event.member
        guild = event.get_guild()
        channel = guild.get_channel(LOGGING_VERIFICATION_CHANNEL_ID)
        content  = event.content

        view = VerificationView()
        content = verification_message(member=member, guild=guild, channel=channel, content=event)
        message = await channel.send(content, components=view)
        client.start_view(view)
        await view.wait()  # Wait for the view to finish
        if view.answer == "accept":
            await member.add_role(role=ROLE_VERIFIED_USER)
            await message.edit(content=f"**Użytkownik {member.mention} został zweryfikowany.**", components=[])
        elif view.answer == "deny":
            await member.send(content="Weryfikacja została odrzucona. Spróbuj ponownie.")
            await event.message.delete()
            await message.edit(content=f"**Użytkownik {member.mention} został odrzucony.**", components=[])
        elif view.answer == "delete":
            await event.message.delete()
            await message.edit(content=f"**Wiadomość użytkownika {member.mention} została usunięta.**", components=[])