import discord
import datetime
import random
import json
from discord.ext import commands

jobs = [
    {
        'description': 'You helped an old women cross the street!',
        'salary': 43
    },
    {
        'description': 'You taught a class about crypto!',
        'salary': 54
    },
    {
        'description': 'You traded an NFT!',
        'salary': 73
    },
    {
        'description': 'You defended an innocent person in court!',
        'salary': 67
    },
    {
        'description': 'You delivered mail to 31 apartments!',
        'salary': 31
    },
    {
        'description': 'You won a raffle!',
        'salary': 100
    },
    {
        'description': 'You developed a smart contract!',
        'salary': 83
    },
]

def worked_embed(user, total, description, salary):
    embed = discord.Embed(
        title = description,
        colour = discord.Colour.gold(),
    )

    embed.set_author(
        name=user,
        url=user.avatar_url,
        icon_url=user.avatar_url
    )

    embed.add_field(name="Earned", value=":coin: {}".format(salary), inline=True)
    embed.add_field(name="Total", value=":coin: {}".format(total), inline=True)

    return embed

def wait_embed(user, timeout, time_passed):
    embed = discord.Embed(
        title = 'You can work again in {} seconds!'.format(timeout - time_passed),
        colour = discord.Colour.red(),
    )

    embed.set_author(
        name=user,
        url=user.avatar_url,
        icon_url=user.avatar_url
    )

    return embed

def balance_embed(user, balance):
    embed = discord.Embed(
        title = 'Your current balance: {} :coin:'.format(balance),
        colour = discord.Colour.green(),
    )

    embed.set_author(
        name=user,
        url=user.avatar_url,
        icon_url=user.avatar_url
    )

    return embed


class PointsCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("PointsCog loaded.")

    @commands.command()
    async def work(self, ctx):
        user = ctx.message.author
        channel = ctx.message.channel
        users = json.load(open('./data/points.json', 'r'))
        timeout = 10

        if not str(user.id) in users:
            users[str(user.id)] = {
                'balance': 0,
                'updated': datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
            }

        data = users[str(user.id)]
        updated = datetime.datetime.fromisoformat(data['updated'])
        time_passed = (datetime.datetime.now() - updated).total_seconds()

        if time_passed > timeout:
            job = random.choice(jobs)
            data['balance'] += job['salary']
            data['updated'] = datetime.datetime.now().isoformat()
            with open('./data/points.json', 'w') as f:
                json.dump(users, f)
            await channel.send(embed=worked_embed(user, data['balance'], job['description'], job['salary']))
        else:
            await channel.send(embed=wait_embed(user, timeout, time_passed))

    @commands.command()
    async def bal(self, ctx):
        users = json.load(open('./data/points.json', 'r'))
        await ctx.message.channel.send(embed=balance_embed(
            ctx.message.author, 
            users[str(ctx.message.author.id)]['balance']
        ))

def setup(client):
    client.add_cog(PointsCog(client))