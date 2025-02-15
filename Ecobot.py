import discord
from discord.ext import commands
import random, os


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
    print('Para ver la lista de comandos pon @ayuda')

@bot.command()
async def ayuda(ctx):
    await ctx.send('Estos son los comandos: ,@Separar @Reciclar, @Beneficio')

@bot.command()
async def Separar(ctx):
    await ctx.send('Para clasificar la basura existen varias canecas de colores, y cada color indica que tipo de basura le pertenece.')
    with open('M2L2/Media/Separarbasura.mp4', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def Reciclar(ctx):
    await ctx.send('Pasos para reciclar: 1.Separar los residuos en diferentes recipientes, 2.Limpiar los materiales a reciclar, 3.Secar los materiales, 4.Aplastar los envases, 5.Depositar los residuos en los contenedores correspondientes, 6.Indicar al recolector de basura cómo están clasificados los residuos')
    with open('M2L2/Media/TresR.mp4', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def Beneficio(ctx):
    await ctx.send('Estos son los beneficios del reciclaje:')
    with open('M2L2/Media/Reciclaje.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

bot.run("My token")
