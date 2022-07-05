import os
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

import MemeBot
import MessageBot

load_dotenv(find_dotenv())
client = commands.Bot('!')

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')

@client.command()
async def embed(ctx):
  print('displayembed')
  embed = discord.Embed(
    title = 'Title',
    description = 'This is the description',
    colour = discord.Colour.blue(),
  )
  embed.set_footer(
    text="This is the footer.", 
    icon_url='https://pbs.twimg.com/media/CmnU0PGWIAE857G.jpg'
  )
  embed.set_image(url='https://cdn.dribbble.com/users/226242/screenshots/2767743/wall_e.png')
  embed.set_author(
    name=ctx.message.author, 
    url=ctx.message.author.avatar_url,
    icon_url=ctx.message.author.avatar_url
  )
  await ctx.send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)

    # messages that start with '$' are commands related to the MemeBot
    if message.content.startswith('$'):
        await MemeBot.handle_message(message, client)

    # messages that start with '#' are commands related to the MessageBot
    if message.content.startswith('#'):
        await MessageBot.handle_message(message, client)
    
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('WALL_I_TOKEN'))