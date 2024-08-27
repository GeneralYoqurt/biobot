import lightbulb

plugin = lightbulb.Plugin('Developer Commands')

@plugin.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.checks.owner_only
@lightbulb.checks.guild_only
@lightbulb.checks.human_only
@lightbulb.implements(lightbulb.SlashCommand)

async def ping(ctx):
    await ctx.respond('Pong!')

def load(bot):
    bot.add_plugin(plugin)