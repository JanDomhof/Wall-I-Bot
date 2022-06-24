import datetime
import random

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


async def update_data(users, user):
    if not user.id in users:
        new_user = {}
        new_user['points'] = 0
        new_user['updated'] = datetime.datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0).isoformat()
        users[str(user.id)] = new_user


async def add_work(users, user, channel, timeout):
    if not str(user.id) in users:
        await update_data(users, user)

    key = str(user.id)
    updated = datetime.datetime.fromisoformat(users[key]['updated'])

    time_passed = (datetime.datetime.now() - updated).total_seconds()

    if time_passed > timeout:
        job = random.choice(jobs)
        users[key]['points'] += job['salary']
        users[key]['updated'] = datetime.datetime.now().isoformat()



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
      
        message = job['description'] + " You earned {} points!".format(job['salary'])
      
        await channel.send(message + " You have a total of {} points!".format(users[key]['points']))
    else:
        await channel.send(
            'You can work again in {} seconds'.format(timeout - time_passed))
