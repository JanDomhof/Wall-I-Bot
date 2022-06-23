import discord
from replit import db

async def handle_message(message):
    print("PointsBot message recieved")

    author = f"{message.author}"

    if message.content.startswith("$give point"):
        if author in db.keys():
            db[author] = db[author] + 1
            print("Added 1 point to {}, Current points of {} are {}".format(author, author, db[author]))
        else:
            db[author] = 1

    if message.content.startswith("$show points"):
        await message.channel.send("total points of {} are / is {}".format(author, db[author]))
