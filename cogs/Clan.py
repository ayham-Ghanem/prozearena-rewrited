import discord
import random
from discord.ext import commands, tasks
import os
from itertools import cycle
import asyncio
import aiomysql
import string
from discord.utils import get   




class Clan(commands.Cog):
     
    def __init__(self,client):
       
        self.client = client

    @commands.command(aliases = ['CLAN','Clan','cLAN'])
    async def clan(self,ctx):
        mwjod = 0
        #myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
        myDB1 = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
        async with myDB1.cursor() as cur1:
            await cur1.execute(f'SELECT  `Player` FROM `clan`')
            await myDB1.commit()
            pLA = await cur1.fetchall()
            for i in pLA:
                if i== (f'{ctx.author.id}',):
                    mwjod = mwjod+1
                else:
                    pass
            if mwjod == 0 :
                Bembed = discord.Embed( title = 'CLAN WARS ⚔', description = None, colour = discord.Colour.blue())
                Bembed.add_field(name="🔎", value=f"Join A Team", inline=True)
                Bembed.add_field(name="l", value=f"l", inline=True)
                Bembed.add_field(name="🏛 ", value=f"Create A Team", inline=True)
                PbotMSG = await ctx.author.send(embed=Bembed)
                await PbotMSG.add_reaction('🔎')
                await PbotMSG.add_reaction('🏛')
            else:
                await cur1.execute(f'SELECT `Captin` FROM `clan`')
                await myDB1.commit()
                elcapi = await cur1.fetchall()
                elcaptins = []
                for i in elcapi:
                    i = ''.join(i)
                    elcaptins.append(i)
                
               
                
                if f'{ctx.author.id}' in elcaptins:
                    Bembed = discord.Embed( title = 'CLAN WARS ⚔', description = None, colour = discord.Colour.blue())
                    Bembed.add_field(name="🏰", value=f"Show Team Members", inline=True)
                    Bembed.add_field(name="l", value=f"l", inline=True)
                    Bembed.add_field(name="🚶‍♂️ ", value=f"Leave Team", inline=True)
                    Bembed.add_field(name="🥾", value=f"Kick Player", inline=True)
                    Bembed.add_field(name="l", value=f"l", inline=True)
                    Bembed.add_field(name="⚔", value=f"join the war", inline=True)
                    PbotMSG = await ctx.author.send(embed=Bembed)
                    await PbotMSG.add_reaction('🏰')
                    await PbotMSG.add_reaction('🚶‍♂️')
                    await PbotMSG.add_reaction('🥾')
                    # await PbotMSG.add_reaction('⚔')
                    

                
                else:
                    Bembed = discord.Embed( title = 'CLAN WARS ⚔', description = None, colour = discord.Colour.blue())
                    Bembed.add_field(name="🏰", value=f"Show Team Members", inline=True)
                    Bembed.add_field(name="l", value=f"l", inline=True)
                    Bembed.add_field(name="🚶‍♂️ ", value=f"Leave Team", inline=True)
                    PbotMSG = await ctx.author.send(embed=Bembed)
                    await PbotMSG.add_reaction('🏰')
                    await PbotMSG.add_reaction('🚶‍♂️')

                    
class Teams(commands.Cog):
     
    def __init__(self,client):
       
        self.client = client

    
    @commands.command()
    async def teams(self,ctx):
    
        global war
        war =[]
        myDB1 = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
        async with myDB1.cursor() as cur1:
            await cur1.execute(f"SELECT `Team` FROM `clan` ")
            await myDB1.commit()
            jwab = await cur1.fetchall()
            for i in jwab:
                i = ''.join(i)
                if i in war:
                    pass
                else:
                    war.append(i)
        
        count = 1
        teamsstring = ''
        for i in war:
            teamsstring = teamsstring + f'{count}-' + f"{i}" + "\n"
            count = count +1
        
        
        embed = discord.Embed( title = "Teams:", description = teamsstring, colour = discord.Colour.blue())
        await ctx.send(embed=embed)





def setup(client):
    
    client.add_cog(Teams(client))
    
    client.add_cog(Clan(client))