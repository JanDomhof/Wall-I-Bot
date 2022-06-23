import os
import discord
from replit import db

import MemeBot
import PointsBot
import MessageBot

client = discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # messages that start with '$' are commands related to the MemeBot
    if message.content.startswith("$"):
        MemeBot.handle_message()

    # messages that start with '!' are commands related to the PointsBot
    if message.content.startswith('!'):
        PointsBot.handle_message()

    # messages that start with '#' are commands related to the MessageBot
    if message.content.startswith('#'):
        MessageBot.handle_message()
    
client.run(os.environ['envDiscord'])
