from utils import Database
import pyodbc

async def channel(ctx, channel_function):
    try:
        # Stwórz połączenie.
        db = Database()
        # Pobierz kursor z utworzonego połączenia.
        cursor = db.get_cursor()

        cursor.execute(f'SELECT channel_id FROM {ctx.guild_id}_CONFIG_CHANNELS WHERE function = ?', (channel_function))
        result = cursor.fetchone()

        # Jeżeli nie znaleziono w DB kanału o tej funkcji albo jeżeli nie znaleziono id przy kanale z daną funkcją.
        if not result or not result[0]:
            print(f'Kanał o funkcji "{channel_function}" nie został ustawiony')
            return

        channel_id = result[0]

        channel = await ctx.app.rest.fetch_channel(channel_id)

        return channel
    
    except pyodbc.Error as e:
        print(e)

    finally:
        if db:
            db.close()