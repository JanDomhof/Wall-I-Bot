import os
import discord
import json
from discord.ext.commands import Bot

import MemeBot
import PointsBot
import MessageBot

client = Bot('!')

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.command()
async def embed(ctx):
  embed = discord.Embed(
    title = 'Title',
    description = 'This is the description',
    colour = discord.Colour.blue(),
  )

  embed.set_footer(
    text="This is the footer.", 
    icon_url='https://pbs.twimg.com/media/CmnU0PGWIAE857G.jpg')
  embed.set_image(url='https://cdn.dribbble.com/users/226242/screenshots/2767743/wall_e.png')
  embed.set_author(
    name=ctx.message.author,
    url=ctx.message.author.avatar_url,
  icon_url=ctx.message.author.avatar_url)

  await ctx.send(embed=embed)

@client.command()
async def work(ctx):
  with open('users.json', 'r') as f:
    users = json.load(f)

  await PointsBot.add_work(users, ctx.message.author, ctx.message.channel, 10)

  with open('users.json', 'w') as f:
    json.dump(users, f)

@client.event
async def on_member_join(member):
  with open('users.json', 'r') as f:
    users = json.load(f)

  await PointsBot.updata_data(users, member)

  with open('users.json', 'w') as f:
    json.dump(users, f)
    
    
  

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

client.run(os.environ['envDiscord'])