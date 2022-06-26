import datetime
import random
import discord

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

async def work(users, user, channel, timeout):
  if not str(user.id) in users:
    users[str(user.id)] = {
      'points': 0,
      'updated': datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
    }

  key = str(user.id)
  updated = datetime.datetime.fromisoformat(users[key]['updated'])

  time_passed = (datetime.datetime.now() - updated).total_seconds()

  if time_passed > timeout:
    job = random.choice(jobs)
    users[key]['points'] += job['salary']
    users[key]['updated'] = datetime.datetime.now().isoformat()

    await channel.send(embed=worked_embed(user, users[key]['points'], job['description'], job['salary']))
  else:
    await channel.send(embed=wait_embed(user, timeout, time_passed))


def worked_embed(user, total, description, salary):
  embed = discord.Embed(
    title = description,
    colour = discord.Colour.blue(),
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
    colour = discord.Colour.blue(),
  )

  embed.set_author(
    name=user,
    url=user.avatar_url,
    icon_url=user.avatar_url
  )

  return embed
