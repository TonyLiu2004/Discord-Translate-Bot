import discord
from discord import app_commands 

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

@tree.command(name = 'tester', description='testing') #guild specific slash command         removed: guild = discord.Object(id=809441460704378931),
async def slash2(interaction: discord.Interaction, name: str): # the string name is a required input
    await interaction.response.send_message(f"Hello {name}! I was made with Discord.py!")#, ephemeral = True) makes the output only visible to sender

client.run("MTE1Mzg2NzE1OTQwNDAyNzk1NQ.GgXezv.E52_69NRvYT3hUBKPMF0vwZsLG_GUG2yiScszE")
#server id: 809441460704378931