import discord

async def handle_message(message, client):
  print('MessageBot message recieved')

  if message.content.startswith("#hello"):
    await message.channel.send("Hello there fellow hare!")

  if message.content.startswith("#vo"):
    await message.channel.send("Vo gast")