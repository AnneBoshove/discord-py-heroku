import os
from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    
@bot.command(name='kroket')
async def meme(ctx):
    response = 'De kroket is een gefrituurd gerecht, waarbij een vulling in paneermeel is gerold. In Nederland wordt met een kroket meestal een vleeskroket bedoeld, doorgaans van rund- of kalfsvlees. Hoewel vleeskroketten vroeger een slagers- en banketbakkersproduct waren, worden vleeskroketten vooral als typische snack bij de meeste snackbars verkocht. Voor de Nederlandse automatiek zijn zij belangrijk, omdat zij handzaam zijn, makkelijk voorbereid kunnen worden (in tegenstelling tot patates frites) en snel te verkrijgen zijn, en hun smaak na een half uur warm bewaren nog behouden. Ze worden los, of op een broodje ("broodje kroket"), of samen met friet gegeten. Veel mensen eten een kroket met mosterd of een andere saus. Kleinere kroketjes, meestal gemaakt van aardappelen of groenten, worden ook in andere landen gegeten als bijgerecht bij een uitgebreide maaltijd. '
    await ctx.send(response)

if __name__ == "__main__":
    bot.run(TOKEN)
