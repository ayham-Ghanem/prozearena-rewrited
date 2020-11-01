import discord
import random
from discord.ext import commands, tasks
import os
from itertools import cycle
import asyncio
import aiomysql
import string
from discord.utils import get  


playerList1 = []
playerList2 = []
playerList3 = []
uplay1 = []
uplay2 = []
uplay3 = []


Qsize = 10



Maps = ['Coastline!https://cdn.discordapp.com/attachments/726400773122162730/757707782572081152/CoastlineOverheadView.png','Oregon!https://cdn.discordapp.com/attachments/726400773122162730/757707989934407761/Oregon_Rework.jpg','Club house!https://cdn.discordapp.com/attachments/726400773122162730/757708443145470093/Siege_Clubhouse_Thumbnail.jpg','Villa!https://cdn.discordapp.com/attachments/726400773122162730/757699063490805830/534px-R6S_map_villa.jpg','Consulate!https://cdn.discordapp.com/attachments/726400773122162730/757708687518466149/Siege_Consulate_Thumbnail.PNG.png','Kafe Dostoyevsky!https://cdn.discordapp.com/attachments/726400773122162730/757708942309589082/maxresdefault_1.jpg','Theme Park!https://cdn.discordapp.com/attachments/726400773122162730/757709311396020345/R6S_ThPa1.jpg']
PMaps = []

class Queue(commands.Cog):

    def __init__(self,client):
       
        self.client = client


    @commands.command(aliases = ['q','Q','QUEUE'])
    async def queue(self,ctx, argument = None):
        global Maps
        global PMaps
        global playerList1
        global playerList2
        global playerList3
        global uplay1
        global uplay2
        global uplay3
        picked = 0
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
        if mwjod != 1 :
            embed = discord.Embed( title = "PA help", description = f"{ctx.author.mention} ,You need to register using .player ", colour = discord.Colour.red())
            await ctx.send(embed=embed)
        else:
            myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
            async with myDB.cursor() as cur: 
                await cur.execute("SELECT `Team 1` FROM `games` WHERE won = 0")
                data = await cur.fetchall()
                await cur.execute("SELECT `Team 2` FROM `games` WHERE won = 0")
                data1 = await cur.fetchall()
                data2 = []
                for i in data:
                    i = ''.join(i)
                    data2.append(i)
                for j in data1:
                    j = ''.join(j)
                    data2.append(j)    
                jwa = 0
                for k in data2 :
                    if k == str(ctx.author.id) :
                        jwa = jwa + 1
                if jwa != 0 :
                    embed = discord.Embed( title = "Queue help", description = f"{ctx.author.mention} , You must finish your game first ", colour = discord.Colour.red())
                    await ctx.send(embed=embed)
                else :       
            
                    myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
                    if ctx.message.channel.id == 765220691888832542 or ctx.message.channel.id == 765974936929042452: #-------------------------------pc
                        if argument in ['join','j','J'] :
                            if ctx.author in playerList1:

                                embed = discord.Embed( title = "Queue help", description = f"{ctx.author.mention} , You are already in the Queue ", colour = discord.Colour.green())
                                await ctx.send(embed=embed)
                                
                            
                            else: 
                                async with myDB.cursor() as cur:
                                    await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = '{ctx.author.id}'")
                                    uplai = await cur.fetchall()
                                    for i in uplai:
                                        i = ''.join(i)
                                    uplay1.append(i)
                                    playerList1.append(ctx.author)
                                    embed = discord.Embed( title = "Queue help", description = f"{ctx.author.mention} has joined the queue\n there are {len(playerList1)} Players out of 10 ", colour = discord.Colour.green())
                                    await ctx.send(embed=embed)

                                
                        elif argument in ['l','leave','L']:
                            if ctx.author in playerList1:
                                async with myDB.cursor() as cur:
                                    await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = '{ctx.author.id}'")
                                    uplao = await cur.fetchall()
                                    for i in uplao:
                                        i = ''.join(i)
                                    if i in uplay1:
                                        uplay1.remove(i)
                                    else:
                                        pass
                                    playerList1.remove(ctx.author)
                                    embed = discord.Embed( title = "Queue help", description = f"{ctx.author.mention} , has left the queue ", colour = discord.Colour.red())
                                    await ctx.send(embed=embed)
                                    
                            else:
                                embed = discord.Embed( title = "Queue help", description = f"{ctx.author.mention} , you are not in the Queue ", colour = discord.Colour.red())
                                await ctx.send(embed=embed)
                            
                        elif argument == None:
                            embed = discord.Embed( title = "Queue help", description = f"{len(playerList1)} Players out of 10 ", colour = discord.Colour.blue())
                            await ctx.send(embed=embed)
                        else : 
                            embed = discord.Embed( title = f'Queue help', description = f"{ctx.author.mention}, USE (.q j) to join OR (.q L) to leave", colour = discord.Colour.blurple())
                            await ctx.send(embed=embed) 

                        if len(playerList1)  >= Qsize:
                            Team1 = []
                            Team2 = []
                                
                            n = 0   
                            if len(PMaps) == 7 :
                                PMaps = []
        

                            while picked == 0:
                                M = random.choice(Maps)
                                if M in PMaps :
                                    pass
                                else: 
                                    PMaps.append(M)
                                    M= M.split("!")
                                    elmap = M[0]
                                    elurl = M[1]
                                    elurl = elurl.replace(" ","")
                                    elurl = elurl.replace("'","")
                                    picked = 1
                        

                                    

                                
                            myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
                            async with myDB.cursor() as cur: 
                                await cur.execute("SELECT `Game_id` FROM `games`") 
                                data = await cur.fetchall()
                                data2 = []
                                for i in data:
                                    i = ''.join(i)
                                    data2.append(i)     #getting all game id names
                                gen_id = []
                                for i in range(0, len(data2) + 1):
                                    rn = random.randint(0,9)
                                    rl = random.choice(string.ascii_letters)
                                    GameID = f"{rl}-{rn}"
                                    gen_id.append(GameID)
                                for i in gen_id : 
                                    for t in data2:
                                        if t != i :
                                            GameID = i
                                
                                
                                    
                                while n<Qsize/2 :   
                                    n = n+1
                                    chosenP = random.choice(playerList1)
                                    Team1.append(chosenP.mention)                  
                                    playerList1.remove(chosenP)
                                    chosenP1 = random.choice(playerList1)
                                    Team2.append(chosenP1.mention)                  
                                    playerList1.remove(chosenP1)
                                    await cur.execute(f"INSERT INTO `games` (`Team 1`, `Team 2`, `Game_id`, `Won`, `sign`) VALUES ('{chosenP.id}','{chosenP1.id}','{GameID}', 0, 0)")
                                    await myDB.commit()
                            
                            
                            embed = discord.Embed( title = f'Map: {elmap}', description = f"{GameID}", colour = discord.Colour.blue())
                            count = 1
                            orange_player_string = ""
                            for i in Team1:
                                orange_player_string = f"{orange_player_string}" + f"{count} - " + f"{i}" + "\n"
                                count  = count +1
                            count1 = 1
                            Blue_player_string = ""
                            for i in Team2:
                                Blue_player_string = f"{Blue_player_string}" + f"{count1} - " + f"{i}" + "\n"
                                count1 = count1 +1
                            
                            embed.add_field(name="Orange Team ", value=f"{orange_player_string}", inline=True)
                            embed.add_field(name="Blue Team ", value=f"{Blue_player_string}", inline=True)
                            embed.add_field(name='Uplay Names:', value= f'{uplay1}', inline=True)
                            embed.set_image(url=f'{elurl}')
                            await ctx.send(embed=embed)
                            await ctx.send(Team1 + Team2)  
                                
                            results = ctx.guild.get_channel(765969729910997023) 
                            botMSG4 = await results.send(f'Match : {GameID}') 
                            await botMSG4.add_reaction('🟧')
                            await botMSG4.add_reaction('🟦')
                            await botMSG4.add_reaction('✖')
                            uplay1 = []
                            await ctx.send(f'{chosenP.mention} you are the host')
                    
                # elif ctx.message.channel.id == 728640805102682165 : #-----------------------------------ps4
                #     if argument in ['join','j'] :
                #         if ctx.author in playerList2:

                #             await ctx.send(f'{ctx.author.mention}, you are already in the Queue')
                        
                #         else: 
                #             async with myDB.cursor() as cur:
                #                 await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = '{ctx.author.id}'")
                #                 uplai = await cur.fetchall()
                #                 for i in uplai:
                #                     i = ''.join(i)
                #                 uplay2.append(i)
                #                 playerList2.append(ctx.author)
                #                 await ctx.send(f'{ctx.author.mention} has joined the queue')
                #                 await ctx.send(f'there are {len(playerList2)} Players out of 10')

                            
                #     elif argument in ['l','leave']:
                #         if ctx.author in playerList2:
                #             async with myDB.cursor() as cur:
                #                 await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = '{ctx.author.id}'")
                #                 uplai = await cur.fetchall()
                #                 for i in uplai:
                #                     i = ''.join(i)
                #                 uplay2.remove(i)
                #                 playerList2.remove(ctx.author)
                #                 await ctx.send(f'{ctx.author.mention} has left the queue')
                                
                #         else:
                #             await ctx.send(f'{ctx.author.mention} you are not in the Queue')
                        
                #     elif argument == None:
                #         await ctx.send(f'{len(playerList2)} Players out of 10')
                #     else : 
                #         await ctx.send('Invalid Argument') 

                #     if len(playerList2)  >= Qsize:
                #         Team12 = []
                #         Team22 = []
                            
                #         n = 0   
                            
                            
                #         myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
                #         async with myDB.cursor() as cur: 
                #             await cur.execute("SELECT `Game_id` FROM `games`") 
                #             data = await cur.fetchall()
                #             data2 = []
                #             for i in data:
                #                 i = ''.join(i)
                #                 data2.append(i)     #getting all game id names
                #             gen_id = []
                #             for i in range(0, len(data2) + 1):
                #                 rn = random.randint(0,9)
                #                 rl = random.choice(string.ascii_letters)
                #                 GameID = f"{rl}-{rn}"
                #                 gen_id.append(GameID)
                #             for i in gen_id : 
                #                 for t in data2:
                #                     if t != i :
                #                         GameID = i
                            
                            
                                
                #             while n<Qsize/2 :   
                #                 n = n+1
                #                 chosenP2 = random.choice(playerList2)
                #                 Team12.append(chosenP2.mention)                  
                #                 playerList2.remove(chosenP2)
                #                 chosenP3 = random.choice(playerList2)
                #                 Team22.append(chosenP3.mention)                  
                #                 playerList2.remove(chosenP3)
                #                 await cur.execute(f"INSERT INTO `games` (`Team 1`, `Team 2`, `Game_id`, `Won`, `sign`) VALUES ('{chosenP2.id}','{chosenP3.id}','{GameID}', 0, 0)")
                #                 await myDB.commit()
                                

                #         await ctx.send(f'Orange Team  : {Team12}') 
                #         await ctx.send(f'Blue Team  : {Team22}') 
                #         await ctx.send(f'Map: {random.choice(Maps)}') 
                #         await ctx.send(f'Match ID : {GameID}')       
                #         await ctx.send(f'uplay names: {uplay2}')
                #         uplay2 = []
                #         await ctx.send(f'{chosenP2.mention} you are the host')
                #         results = ctx.guild.get_channel(728759249064427580) 
                #         botMSG4 = await results.send(f'Match : {GameID}') 
                #         await botMSG4.add_reaction('🟧')
                #         await botMSG4.add_reaction('🟦')
                #         await botMSG4.add_reaction('✖')
                    
                    
                # elif ctx.message.channel.id == 728640828934979664 : #-----------------------------------XBOX
                #     if argument in ['join','j'] :
                #         if ctx.author in playerList3:

                #             await ctx.send(f'{ctx.author.mention}, you are already in the Queue')
                        
                #         else: 
                #             async with myDB.cursor() as cur:
                #                 await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = {ctx.author.id}")
                #                 uplai = await cur.fetchall()
                #                 for i in uplai:
                #                     i = ''.join(i)
                #                 uplay3.append(i)
                #                 playerList3.append(ctx.author)
                #                 await ctx.send(f'{ctx.author.mention} has joined the queue')
                #                 await ctx.send(f'there are {len(playerList3)} Players out of 10')

                            
                #     elif argument in ['l','leave']:
                #         if ctx.author in playerList3:
                #             async with myDB.cursor() as cur:
                #                 await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = {ctx.author.id}")
                #                 uplai = await cur.fetchall()
                #                 for i in uplai:
                #                     i = ''.join(i)
                #                 uplay3.remove(i)
                #                 playerList3.remove(ctx.author)
                #                 await ctx.send(f'{ctx.author.mention} has left the queue')
                                
                #         else:
                #             await ctx.send(f'{ctx.author.mention} you are not in the Queue')
                        
                #     elif argument == None:
                #         await ctx.send(f'{len(playerList3)} Players out of 10')
                #     else : 
                #         await ctx.send('Invalid Argument') 

                #     if len(playerList1)  >= Qsize:
                #         Team13 = []
                #         Team23 = []
                            
                #         n = 0   
                            
                            
                #         myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
                #         async with myDB.cursor() as cur: 
                #             await cur.execute("SELECT `Game_id` FROM `games`") 
                #             data = await cur.fetchall()
                #             data2 = []
                #             for i in data:
                #                 i = ''.join(i)
                #             data2.append(i)     #getting all game id names
                #             gen_id = []
                #             for i in range(0, len(data2) + 1):
                #                 rn = random.randint(0,9)
                #                 rl = random.choice(string.ascii_letters)
                #                 GameID = f"{rl}-{rn}"
                #                 gen_id.append(GameID)
                #             for i in gen_id : 
                #                 for t in data2:
                #                     if t != i :
                #                         GameID = i
                            
                            
                                
                #             while n<Qsize/2 :   
                #                 n = n+1
                #                 chosenP4 = random.choice(playerList3)
                #                 Team13.append(chosenP4.mention)                  
                #                 playerList3.remove(chosenP4)
                #                 chosenP5 = random.choice(playerList3)
                #                 Team23.append(chosenP5.mention)                  
                #                 playerList3.remove(chosenP5)
                #                 await cur.execute(f"INSERT INTO `games` (`Team 1`, `Team 2`, `Game_id`, `Won`, `sign`) VALUES ('{chosenP4.id}','{chosenP5.id}','{GameID}', 0, 0)")
                #                 await myDB.commit()
                                

                #         await ctx.send(f'Orange Team  : {Team13}') 
                #         await ctx.send(f'Blue Team  : {Team23}') 
                #         await ctx.send(f'Map: {random.choice(Maps)}') 
                #         await ctx.send(f'Match ID : {GameID}')       
                #         results = ctx.guild.get_channel(728759249064427580) 
                #         botMSG4 = await results.send(f'Match : {GameID}') 
                #         await botMSG4.add_reaction('🟧')
                #         await botMSG4.add_reaction('🟦')
                #         await botMSG4.add_reaction('✖')
                #         await ctx.send(f'uplay names: {uplay3}')
                #         uplay3 = []
                #         await ctx.send(f'{chosenP4.mention} you are the host')
                    
                    else : 
                        embed = discord.Embed( title = 'PA help', description = f'{ctx.author.mention}, You are not in the Queue Channel', colour = discord.Colour.red())
                        await ctx.send(embed= embed)


def setup(client):
    
    client.add_cog(Queue(client))