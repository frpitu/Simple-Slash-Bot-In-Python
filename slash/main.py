import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

# Variáveis
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)
slash = SlashCommand(bot, sync_commands=True)

# Eventos
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Comando
@slash.slash(name="hello", description="Diz olá!")

# Def & Resposta
async def hello(ctx: SlashContext):
    await ctx.send(content="Olá! Como vai?")

bot.run('YOUR_BOT_TOKEN')