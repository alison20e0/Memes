import discord
import os
from discord.ext import commands
import random

description = "Este es un programa donde vinculamos a Discord con VS Code para lanzar imagenes"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", description=description, intents=intents)
img_mem = os.listdir("images")

@bot.event
async def on_ready():
    print(f"Logueado como {bot.user} (ID: {bot.user.id})")

@bot.command()
async def mem(ctx):
    if ctx.message.author == bot.user:
        return
    
    img_to_send = random.choice(img_mem)
    with open(f'images/{img_to_send}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("Token")