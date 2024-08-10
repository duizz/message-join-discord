import os
import discord
from discord.ext import commands
from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default() #set default permissions
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        msg = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(msg)

@bot.event
async def on_ready():
    print(f"{bot.user} inicializated!")

bot.run(TOKEN)
