import discord
import json
import os
from discord.ext import commands

def wrong_name_embed(user, meme):
  embed = discord.Embed(
    title = 'There is no meme named {}!'.format(meme),
    colour = discord.Colour.red(),
  )

  embed.set_author(
    name=user,
    url=user.avatar_url,
    icon_url=user.avatar_url
  )

  return embed

def error_embed(user, error):
  embed = discord.Embed(
    title = error,
    colour = discord.Colour.red(),
  )

  embed.set_author(
    name=user,
    url=user.avatar_url,
    icon_url=user.avatar_url
  )

  return embed

class MemeCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
      print("MemeCog Loaded.")

  @commands.command()
  async def meme(self, ctx, meme):
    file = None
    for filename in os.listdir('./memes'):
      if filename[:-4] == meme:
        file = filename
    if file is not None:
      await ctx.message.channel.send(file=discord.File('./memes/{}'.format(file)))
    else:
      await ctx.message.channel.send(embed=wrong_name_embed(ctx.message.author, meme))

  @meme.error
  async def missing_argument(self, ctx, error):
    await ctx.message.channel.send(embed=error_embed(ctx.message.author, error))


def setup(client):
  client.add_cog(MemeCog(client))