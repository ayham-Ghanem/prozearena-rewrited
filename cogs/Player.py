import discord
import random
from discord.ext import commands, tasks
import os
from itertools import cycle
import asyncio
import aiomysql
import string
from discord.utils import get     



class Player(commands.Cog):
     
    def __init__(self,client):
       
        self.client = client
    
    
    @commands.command(aliases = ['PLAYER'])
    async def player(self,ctx,* ,Argument= None):
        if ctx.channel.id == 765219179372216361 :    
            if Argument != None:
                pass
            else:
                myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
                async with myDB.cursor() as cur:
                    await cur.execute("SELECT name FROM test1.whatever ")
                    PlayerID = await cur.fetchall()
                    feWa7d = 0
                    for i in PlayerID: 
                        if (f'{ctx.author.id}',) == i:
                            feWa7d = feWa7d+1 

                    if feWa7d == 0: 
                        Bembed = discord.Embed( title = 'WELCOME!', description = None, colour = discord.Colour.blue())
                        Bembed.add_field(name="🖊", value=f"Register", inline=True)
                        PbotMSG = await ctx.author.send(embed=Bembed)
                        await PbotMSG.add_reaction('🖊')
                        
                    else:
                        Bembed = discord.Embed( title = 'Player menu:', description = None, colour = discord.Colour.blue())
                        Bembed.add_field(name="📄", value=f"Change uplay name", inline=True)
                        PbotMSG = await ctx.author.send(embed=Bembed)
                        await PbotMSG.add_reaction('📄')
    
        else:
            embed = discord.Embed( title = 'PA help', description = f'{ctx.author.mention} , You can use .player only in Register channel', colour = discord.Colour.red())
            botMSG1 = await ctx.send(embed = embed)
            await asyncio.sleep(15)   
            await botMSG1.delete()
            await ctx.message.delete() 




class Info(commands.Cog):
     
    def __init__(self,client):
       
        self.client = client

    @commands.command(aliases = ['INFO','Info'])
    async def info(self,ctx):
        shbab = []
        mwjod = 0
        myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
        async with myDB.cursor() as cur:
            await cur.execute(f"SELECT `name` FROM `whatever`")
            await myDB.commit()
            up = await cur.fetchall()
            for i in up:
                i = ''.join(i)
                shbab.append(i)
            for i in shbab:
                if i == f'{ctx.author.id}':
                    mwjod = 1
            
            if mwjod == 1:

                await cur.execute(f"SELECT uplay FROM `whatever` WHERE name = '{ctx.author.id}'")
                await myDB.commit()
                up = await cur.fetchall()
                for i in up:
                    i = ''.join(i)
                await cur.execute(f"SELECT  `Platform` FROM `whatever` WHERE name = {ctx.author.id}")
                await myDB.commit()
                pl = await cur.fetchall()
                for a in pl:
                    a = ''.join(a)
                await cur.execute(f"SELECT  `MMR` FROM `whatever` WHERE name = {ctx.author.id}")
                await myDB.commit()
                mmr = await cur.fetchall()
                for b in mmr:
                    b = ''.join(b)
                await cur.execute(f"SELECT  `Games_Played` FROM `whatever` WHERE name = {ctx.author.id}")
                await myDB.commit()
                GP = await cur.fetchall()
                for c in GP:
                    c = ''.join(c)
                await cur.execute(f"SELECT  `Games_won` FROM `whatever` WHERE name = {ctx.author.id}")
                await myDB.commit()
                GW = await cur.fetchall()
                for d in GW:
                    d = ''.join(d)
                await cur.execute(f"SELECT  `Games_Lost` FROM `whatever` WHERE name = {ctx.author.id}")
                await myDB.commit()
                GL = await cur.fetchall()
                for e in GL:
                    e = ''.join(e)
            
                istring =  f'{i}' + "\n" +f'{a}\n' + f'{b}\n'+ f'{c}\n' + f'{d}\n' +f'{e}\n' 
                string = "Uplay:\n Platform: \n MMR: \n Games Played: \n Games Won: \n Games Lost:"
                embed = discord.Embed( title = f"{i}'s Stats:", description = f"Known as:{ctx.author.mention}", colour = discord.Colour.red())
                embed.add_field(name=f"{string}", value='‎', inline=True)
                embed.add_field(name=f"{istring}", value='‎', inline=True)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed( title = "PA help", description = f"{ctx.author.mention} ,You need to register using .player ", colour = discord.Colour.red())
                await ctx.send(embed=embed)



class Top(commands.Cog):
     
    def __init__(self,client):
       
        self.client = client

    @commands.command()
    async def top(self,ctx):
        myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')           
        async with myDB.cursor() as cur:
            await cur.execute(f"SELECT `name` FROM `whatever` ORDER BY `whatever`.`MMR` DESC LIMIT 10")
            await myDB.commit()  
            elshbab = []
            elshb = await cur.fetchall()
            for i in elshb:
                i = ''.join(i)
                elshbab.append(i)
            
            await cur.execute(f"SELECT `MMR` FROM `whatever` ORDER BY `whatever`.`MMR` DESC LIMIT 10")
            await myDB.commit() 
            elmmrs = []
            elmmr = await cur.fetchall()
            for j in elmmr:
                j = ''.join(j)   
                elmmrs.append(j)
            
            Tembed = discord.Embed( title = 'TOP 10', description = None, colour = discord.Colour.blue())
            Tcount = 1
            Tplayer = ""
            for i in elshbab:
                Tplayer = f"{Tplayer}" + f"{Tcount} - " + f"<@{i}>" + "\n"
                Tcount  = Tcount +1
            
            Mplayer = ""
            for m in elmmrs:
                Mplayer = f"{Mplayer}" + f"{m}" + "\n"    
            
            Tembed.add_field(name="PLAYERS ", value=f"{Tplayer}", inline=True)
            Tembed.add_field(name="MMR ", value=f"{Mplayer}", inline=True)
            await ctx.send(embed=Tembed)





def setup(client):
    
    client.add_cog(Player(client))
    
    client.add_cog(Info(client))

    client.add_cog(Top(client))
    
    
