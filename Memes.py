
import discord
from discord.ext import commands
import random
import asyncio
import os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='@', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def mem(ctx):
    img = random.choice(os.listdir("M2L1/IMG"))
    with open(f'M2L1/IMG/{img}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)





bot.run('MTMzMjc5OTk3MzI4NDI0OTY5MA.GD5dz1.aCsZs54BdE22Xa8zVCpYIuGK_Mfz0eAvqXWp1c')
