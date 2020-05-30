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

    hello_there = ("hello there", "hello there!")

    content_no_case = message.content.lower()

    if content_no_case in hello_there:
        asset = discord.File("assets/grievous.gif", filename="grievous.gif")
        # embed = discord.Embed()
        # embed.set_image(url="attachment://{}".format(asset.filename))
        await message.channel.send(file=asset)


client.run(settings.CLIENT_TOKEN)
