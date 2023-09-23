import discord
import responses

async def sendMessage(message, user_message, is_private):
    try:
        response = responses.getResponse(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e: #simple exception catch, improve later
        print(e)

def runDiscordBot():
    TOKEN = 'MTE1Mzg2NzE1OTQwNDAyNzk1NQ.GgXezv.E52_69NRvYT3hUBKPMF0vwZsLG_GUG2yiScszE'
    bot_intents = discord.Intents.default()
    bot_intents.message_content = True
    client = discord.Client(intents=bot_intents)

    @client.event #Tells us that the server is running
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user: #avoid infinite loop since client user is the bot, and when bot creates message, the bot becomes the message author
            return
        username = str(message.author)
        user_message = str(message.content) #convert message.content to string and return, in case message.content does not return string
        channel = str(message.channel)

        print(f'{username} said: {user_message} in {channel}') # for testing

        if user_message[0] == '?': #responding to users privately
            user_message = user_message[1:] #removes the ? from the message
            await sendMessage(message, user_message, is_private=True)
        else:
            await sendMessage(message, user_message, is_private=False)

    client.run(TOKEN) #RUN THE BOT!