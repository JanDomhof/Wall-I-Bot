import os
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = commands.Bot('!')

@client.event
async def on_ready():
  print("Main Bot Loaded.".format(client))
    
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('WALL_I_TOKEN'))