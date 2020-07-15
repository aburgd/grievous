import discord
import settings

client = discord.Client()


@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hello_there = "hello there"

    content_no_case = message.content.lower()

    if hello_there in content_no_case:
        asset = discord.File("assets/grievous.gif", filename="grievous.gif")
        await message.channel.send(file=asset)


client.run(settings.CLIENT_TOKEN)
