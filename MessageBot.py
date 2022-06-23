import discord

async def handle_message(message):
    print('MessageBot message recieved')

    if message.content.startswith("#hello"):
        await message.channel.send("Hello there fellow hare!")