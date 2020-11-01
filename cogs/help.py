import discord
import random
from discord.ext import commands, tasks
import os
from itertools import cycle
import asyncio
import aiomysql
import string
from discord.utils import get   



# class Help(commands.Cog):

#     def __init__(self,client):
        
#         self.client = client

#     @commands.command()
#     async def help(self,ctx,page):
        
#         embed = discord.Embed( title=  'ProzHelp', description = 'Press the arrow buttons to scroll between pages!', colour = discord.Colour.blue())
#         embed.add_field(name=  '.player',value= 'Used in order to register the player or to change his Uplay name for the queue feature' ,inline=True)
#         embed.add_field(name=  '.clan',value= "Opens the clan's menu from there u can create a team or join one " ,inline=True)
#         embed.add_field(name=  '.report [member] [reason]',value= 'Report a member to staff for breaking the rules.' ,inline=True)

            

class Report(commands.Cog):

    def __init__(self,client):
        
        self.client = client

    @commands.command()
    async def report(self,ctx,*,elreport):
        
        report = ctx.guild.get_channel(765963956560199700)
        await report.send(f'report: {elreport}')
        botMSG1 = await ctx.send('thank you for your report')
        await asyncio.sleep(2)   
        await botMSG1.delete()
        await ctx.message.delete()
        





def setup(client):
    
    client.add_cog(Report(client))
    
    #client.add_cog(Help(client))