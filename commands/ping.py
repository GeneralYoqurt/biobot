import lightbulb

plugin = lightbulb.Plugin('Developer Commands')

@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)

async def ping(ctx):
    await ctx.respond('Pong!')

def load(bot):
    bot.add_plugin(plugin)