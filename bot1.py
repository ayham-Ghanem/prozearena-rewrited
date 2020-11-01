import discord
import random
from discord.ext import commands, tasks
import os
from itertools import cycle
import asyncio
import aiomysql
import string
from discord.utils import get   
from Key import key


client = commands.Bot(command_prefix='.')
status = cycle(['.help for help', 'BETA Version','Rainbow Six Siege'])
client.remove_command('help')
print ('sndeeed kadeeeeem')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_ready():
   change_status.start()
   print('Bot is Ready.')
  

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#@client.event
#async def on_member_join(member):
  #  print(f'{member} has joined the server.')


@client.command()
async def on_command_error(ctx, error):
    pass



mfta7 = key()
client.run(mfta7)







