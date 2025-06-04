import hikari
from config import CHANNEL_INTRODUCE_ID
from state import bot

@bot.listen(hikari.MemberCreateEvent)
async def on_member_create(event: hikari.MemberCreateEvent) -> None:
    """Event handler for when a member joins the server."""
    try:
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
        try:
            await member.send(attachment="images/weryfikacja.png")
            await member.send(welcome_message(member=member, guild=guild, channel=channel))
        except hikari.ForbiddenError:
            # User has DMs disabled
            print(f"Nie można wysłać DM do użytkownika {member.id}")
        except Exception as e:
            print(f"Błąd przy wysyłaniu DM: {e}")

        if channel:
            try:
                # Use display_name which is safer than mention for users with special characters
                safe_mention = f"<@{member.id}>"  # Direct ID mention is safer than member.mention
                message = await channel.send(f"Witamy {safe_mention} na serwerze!", user_mentions=True)
            except Exception as e:
                print(f"Błąd przy wysyłaniu wiadomości powitalnej: {e}")
            finally:
                await message.delete()  # Delete the message after 5 seconds
    except Exception as e:
        print(f"Główny błąd w event handlerze on_member_create: {e}")
