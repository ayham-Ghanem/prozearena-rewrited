


# war = []
# war1 = []
# war2 = []

# @client.command(aliases = ['POLL'])
# async def poll(ctx):
#     global war
#     gamesstring = ''
#     n=0
    
    
#     myDB1 = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
#     async with myDB1.cursor() as cur1:
#         await cur1.execute(f"SELECT `Team` FROM `tournament`")
#         await myDB1.commit()
#         jwab = await cur1.fetchall()
#         for i in jwab:
#             i = ''.join(i)
#             if i in war:
#                 pass
#             else:
#                 war.append(i)

    
#     while n<4 :   
#         n = n+1
#         chosenT = random.choice(war)
#         war1.append(chosenT)                  
#         war.remove(chosenT)
#         chosenT1 = random.choice(war)
#         war1.append(chosenT1)                  
#         war.remove(chosenT1)
#         gamesstring = gamesstring + f"{chosenT} vs {chosenT1} \n"
#         results = ctx.guild.get_channel(765984718713782272) 
#         botMSG4 = await results.send(f'Match : {chosenT} VS {chosenT1}') 
#         await botMSG4.add_reaction('🔶')
#         await botMSG4.add_reaction('🔷')
#         warch = ctx.guild.get_channel(765984718713782272)

        
#     embed = discord.Embed( title = "clan war started", description = 'Quarter-finale' , colour = discord.Colour.blue())
#     embed.add_field(name=gamesstring, value='GOOD LUCK!', inline=True)
#     await warch.send(embed=embed)
        





# @client.command()
# async def p(ctx):

#     myDB1 = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
#     async with myDB1.cursor() as cur1:
#         await cur1.execute(f"SELECT `Team` FROM `tournament` WHERE stage = '2'")
#         await myDB1.commit()
#         jwab = await cur1.fetchall()
#         for i in jwab:
#             i = ''.join(i)
#             war2.append(i)
                
#     if len(war2) >=2:
#         chosenT = random.choice(war2)
#         war2.remove(chosenT)
#         chosenT1 = random.choice(war2)                  
#         war2.remove(chosenT1)
#         embed = discord.Embed( title = "SEMI-FINALE", description = f'{chosenT} vs {chosenT1}' , colour = discord.Colour.red())
#         clanwarch = ctx.guild.get_channel(765984718713782272)
#         await clanwarch.send(embed=embed)






# @client.command()
# async def show(ctx):

#     global war
#     war =[]
#     myDB1 = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
#     async with myDB1.cursor() as cur1:
#         await cur1.execute(f"SELECT `Team` FROM `tournament` WHERE stage = '1'")
#         await myDB1.commit()
#         jwab = await cur1.fetchall()
#         for i in jwab:
#             i = ''.join(i)
#             war.append(i)
    
#     count = 1
#     teamsstring = ''
#     for i in war:
#         teamsstring = teamsstring + f'{count}-' + f"{i}" + "\n"
#         count = count +1
    
    
#     embed = discord.Embed( title = "Clan WAR Teams:", description = teamsstring, colour = discord.Colour.blue())
#     await ctx.send(embed=embed)





# @client.command(aliases = ['sug'])
# async def suggest(ctx,*,elsuggest):
    
#     suggest = ctx.guild.get_channel(726550277355733094)
    
#     await suggest.send(f'Suggestion: {elsuggest}')   
#     botMSG2 = await ctx.send('thank you for your suggestion ')
#     await asyncio.sleep(3)   
#     await botMSG2.delete()
#     await ctx.message.delete()