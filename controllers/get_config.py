from utils import Database
import pyodbc

async def channel(ctx, channel_function):
    try:
        # Stwórz połączenie
        db = Database()
        # Pobierz kursor z utworzonego połączenia
        cursor = db.get_cursor()

        cursor.execute(f'SELECT channel_id FROM {ctx.guild_id}_CONFIG_CHANNELS WHERE function = ?', (channel_function))
        result = cursor.fetchone()

        if not result[0]:
            print(f'Kanał o funkcji {channel_function} nie został ustawiony')
            return

        channel_id = result[0]

        channel = await ctx.app.rest.fetch_channel(channel_id)

        return channel
    
    except pyodbc.Error as e:
        print(e)

    finally:
        if db:
            db.close()