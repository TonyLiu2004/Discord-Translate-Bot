import discord
from discord import app_commands 
import translater

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync()#removed:  guild = discord.Object(id=809441460704378931))          #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'translate', description='translates') #guild specific slash command         removed: guild = discord.Object(id=809441460704378931),
async def translate(interaction: discord.Interaction, language: str, sentence: str):
    await interaction.response.send_message(translater.translate(sentence,language))#, ephemeral = True) makes the output only visible to sender

client.run("")
#server id: 809441460704378931