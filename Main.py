import discord

client = discord.Client()

@client.event
async def on_read():
    print('Hello, my name is {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startwith('#hello there'):
        await message.channel.send("General Kenobi")
