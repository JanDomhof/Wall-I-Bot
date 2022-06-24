import discord

async def handle_message(message, client):
    print("MemeBot message recieved")

    if message.content.startswith("$harefather"):
      await message.channel.send("opening confidential information 2/10:")
      await message.channel.send(file=discord.File('HareGodFather.jpg'))

    if message.content.startswith("$help me harefather"):
      await message.channel.send(file=discord.File('aDeal.gif'))

    if message.content.startswith("$give offer"):
      await message.channel.send(file=discord.File('DealOfNothing.gif'))
