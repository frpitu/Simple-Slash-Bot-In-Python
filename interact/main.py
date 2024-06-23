import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
    async def on_ready():
        # Mensagem
        print('Bot está online.')
        
        # Registrar O Comando
        await bot.tree.sync()

# Comando
@bot.tree.command(description="Receba Um Olá Do Bot")
async def hello(interact:discord.Interaction):
    await interact.response.send_message(f"Hello {interact.user.name}")
    
# Roda O BOT
bot.run('YOUR_TOKEN_HERE')