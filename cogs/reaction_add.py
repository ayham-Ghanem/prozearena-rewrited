import discord
import random
from discord.ext import commands, tasks
import os
from itertools import cycle
import asyncio
import aiomysql
import string
from discord.utils import get 


#checks if the person is in a clan
async def fewa7d(mem,role):
    mwjod1 = 0
    myDB1 = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
    async with myDB1.cursor() as cur1:
        await cur1.execute(f'SELECT  {str(role)} FROM `clan`')
        await myDB1.commit()
        pLA = await cur1.fetchall()
        for i in pLA:
            if i== (f'{mem}',):
                mwjod1 = mwjod1+1
    return mwjod1




class Reaction(commands.Cog):
    def __init__(self,client):
       
        self.client = client

    
    

    @commands.Cog.listener()
    async def on_reaction_add(self,react: discord.Reaction, person: discord.User):
        mwjod = 0
        Tmwjod = 0
        squadsN = 0
        squadN = 0
        global fewa7d
        if react.message.channel.id == 765969729910997023 :
            if person.id == 725433666481946736 or person.id == 732996700783902770:
                pass
            else:
                if str(react) == '🟧' :
                    FGID =   react.message.content[8:]
                    myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
                    myDB1 = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
                    async with myDB.cursor() as cur: 
                        await cur.execute(f"SELECT `Team 1` FROM `games` WHERE Game_id = '{FGID}' AND Won = '0'")
                        await myDB.commit()
                        WonT = await cur.fetchall()
                        await cur.execute(f"SELECT `Team 2` FROM `games` WHERE Game_id = '{FGID}' AND Won = '0'")
                        await myDB.commit()
                        LosT = await cur.fetchall()
                        await cur.execute(f"UPDATE `games` SET `Won`= 1,`sign`='{person}' WHERE Game_id = '{FGID}' AND Won = '0'")
                        await myDB.commit()
                    async with myDB1.cursor() as cur1:
                        for i in WonT :
                            i = ''.join(i)
                            await cur1.execute(f"UPDATE `whatever` SET `MMR`=`MMR`+50,`Games_Played`=`Games_Played`+1,`Games_won`=`Games_won`+1 WHERE name = {i}")
                            await myDB1.commit()
                        for i in LosT:
                            i = ''.join(i)
                            await cur1.execute(f"UPDATE `whatever` SET `MMR`=`MMR`-50,`Games_Played`=`Games_Played`+1,`Games_Lost`=`Games_Lost`+1 WHERE name = {i}")
                            await myDB1.commit()
                    await react.message.clear_reaction('🟧')
                    await react.message.clear_reaction('🟦')
                    await react.message.clear_reaction('✖')
                    
                    
                elif str(react) == '🟦':
                    FGID =   react.message.content[8:]
                    myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
                    myDB1 = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
                    async with myDB.cursor() as cur: 
                        await cur.execute(f"SELECT `Team 2` FROM `games` WHERE Game_id = '{FGID}' AND Won = '0'")
                        await myDB.commit()
                        WonT = await cur.fetchall()
                        await cur.execute(f"SELECT `Team 1` FROM `games` WHERE Game_id = '{FGID}' AND Won = '0'")
                        await myDB.commit()
                        LosT = await cur.fetchall()
                        await cur.execute(f"UPDATE `games` SET `Won`= 2,`sign`='{person}' WHERE Game_id = '{FGID}' AND Won = '0'")
                        await myDB.commit()
                    async with myDB1.cursor() as cur1:
                        for i in WonT :
                            i = ''.join(i)
                            await cur1.execute(f"UPDATE `whatever` SET `MMR`=`MMR`+50,`Games_Played`=`Games_Played`+1,`Games_won`=`Games_won`+1 WHERE name = {i}")
                            await myDB1.commit()
                        for i in LosT:
                            i = ''.join(i)
                            await cur1.execute(f"UPDATE `whatever` SET `MMR`=`MMR`-50,`Games_Played`=`Games_Played`+1,`Games_Lost`=`Games_Lost`+1 WHERE name = {i}")
                            await myDB1.commit()
                    await react.message.clear_reaction('🟧')
                    await react.message.clear_reaction('🟦')
                    await react.message.clear_reaction('✖')


                elif str(react) == '✖':
                    FGID =   react.message.content[8:]
                    myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
                    async with myDB.cursor() as cur:
                        await cur.execute(f"DELETE FROM `games` WHERE Game_id = '{FGID}'")
                        await myDB.commit()
                    await react.message.clear_reaction('🟧')
                    await react.message.clear_reaction('🟦')
                    await react.message.clear_reaction('✖')
        
                elif str(react) == '🔶':
                    war2 = []
                    await react.message.clear_reaction('🔶')
                    await react.message.clear_reaction('🔷')
                    FGID =   react.message.content[8:]
                    FGID = FGID.split(" ")
                    elefaz = FGID[0]
                    elefaz = elefaz.replace("'","")
                    elefaz = elefaz.replace(" ","")
                    ele5sr = FGID[-1]
                    ele5sr = ele5sr.replace("'","")
                    ele5sr = ele5sr.replace(" ","")
                    myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
                    async with myDB.cursor() as cur: 
                        await cur.execute(f"UPDATE `tournament` SET `stage`='2' WHERE Team = '{elefaz}'")
                        await myDB.commit()
                        await asyncio.sleep(3)
                        await cur.execute(f"SELECT `Team` FROM `tournament` WHERE stage = '2'")
                        await myDB.commit()
                        jwab = await cur.fetchall()
                        for i in jwab:
                            i = ''.join(i)
                            war2.append(i)
                    
                    if len(war2) >=2:
                        chosenT = random.choice(war2)
                        war2.remove(chosenT)
                        chosenT1 = random.choice(war2)                  
                        war2.remove(chosenT1)
                        embed = discord.Embed( title = "SEMI-FINALE", description = f'{chosenT} vs {chosenT1}' , colour = discord.Colour.red())
                        clanwarch = react.message.guild
                        clanwarch = clanwarch.get_channel(765984718713782272)
                        await clanwarch.send(embed=embed)
                        async with myDB.cursor() as cur: 
                            await cur.execute(f"UPDATE `tournament` SET `stage`='0' WHERE Team = '{chosenT}' OR Team = '{chosenT1}'")
                            await myDB.commit()
                            

                elif str(react) == '🔷':
                    war2 = []
                    await react.message.clear_reaction('🔶')
                    await react.message.clear_reaction('🔷')
                    FGID =   react.message.content[8:]
                    FGID = FGID.split(" ")
                    ele5sr = FGID[0]
                    ele5sr = ele5sr.replace("'","")
                    ele5sr = ele5sr.replace(" ","")
                    elefaz = FGID[-1]
                    elefaz = elefaz.replace("'","")
                    elefaz = elefaz.replace(" ","")
                    myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')
                    async with myDB.cursor() as cur: 
                        await cur.execute(f"UPDATE `tournament` SET `stage`='2' WHERE Team = '{elefaz}'")
                        await myDB.commit()
                        await asyncio.sleep(3)
                        await cur.execute(f"SELECT `Team` FROM `tournament` WHERE stage = '2'")
                        await myDB.commit()
                        jwab = await cur.fetchall()
                        for i in jwab:
                            i = ''.join(i)
                            war2.append(i)
                    
                    if len(war2) >=2:
                        chosenT = random.choice(war2)
                        war2.remove(chosenT)
                        chosenT1 = random.choice(war2)                  
                        war2.remove(chosenT1)
                        embed = discord.Embed( title = "SEMI-FINALE", description = f'{chosenT} vs {chosenT1}' , colour = discord.Colour.red())
                        clanwarch = react.message.guild
                        clanwarch = clanwarch.get_channel(765984718713782272)
                        await clanwarch.send(embed=embed)
                        async with myDB.cursor() as cur: 
                            await cur.execute(f"UPDATE `tournament` SET `stage`='0' WHERE Team = '{chosenT}' OR Team = '{chosenT1}'")
                            await myDB.commit()
                            
        
        
        
        
        
        
        else :

            if person.id == 725433666481946736 or person.id == 732996700783902770 :
                pass
                        

            else:
                myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
                myDB1 = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='test1')

                if str(react) == '🔎':
                    async with myDB1.cursor() as cur1:
                        mwjod = await fewa7d(person.id,'player')
                        if mwjod == 0:
                            await react.message.delete()
                            await cur1.execute(f"SELECT `Team` FROM `clan`")
                            await myDB1.commit()
                            teams = await cur1.fetchall()
                            alteam = []
                            for i in teams:
                                i = ''.join(i)
                                if i in alteam :
                                    pass              
                                else: 
                                    alteam.append(i)
                            Teams_string = ""
                            count = 1
                            TeamN = ''
                            for i in alteam:
                                Teams_string = f"{Teams_string}" + f"{count} - " + f"{i}" + "\n"
                                count  = count +1
                            Aembed = discord.Embed( title = f'Teams Names:', description = None, colour = discord.Colour.blue())
                            Aembed.add_field(name="please write the team's name you want to join", value=f"{Teams_string}", inline=True)
                            await person.send(embed=Aembed)
                            def check(m):
                                return m.content and m.author.id != 725433666481946736 and m.author == person
                            msg = await self.client.wait_for('message', check=check)
                            TeamN = str(msg.content.upper().replace(' ', ''))

                            if TeamN in alteam:
                                await cur1.execute(f"SELECT `Captin` FROM `clan` WHERE Team = '{TeamN}'")
                                await myDB1.commit()
                                capi = await cur1.fetchall()
                                for i in capi:
                                    i = int(''.join(i))
                                capi = await self.client.fetch_user(i)           
                                ASKembed = discord.Embed( title = f'Joining Request', description = f"Do you want to accept?\n {person.mention}"
                                , colour = discord.Colour.blue())
                                
                                pMSG = await discord.User.send(capi, embed=ASKembed)
                            
                                await pMSG.add_reaction('🤝')
                                await pMSG.add_reaction('🚫')
                                embed = discord.Embed( title = f'Joining Request Sent', description = f"Please wait for {capi.mention} Response")
                                await person.send(embed=embed)
                            else:
                                await person.send('Please try again and write the exact name')


                            


                # elif str(react) == '⚔':
                #     await react.message.delete()
                #     async with myDB1.cursor() as cur1:
                #         await cur1.execute(f'SELECT  `Captin` FROM `clan`')
                #         await myDB1.commit()
                #         pLA = await cur1.fetchall()
                #         for i in pLA:
                #             if i== (f'{person.id}',):
                #                 mwjod = mwjod+1
                #             else:
                #                 pass
                        
                #         await cur1.execute(f"SELECT `Captain` FROM `tournament`")
                #         await myDB1.commit()
                #         pLA = await cur1.fetchall()
                #         for i in pLA:
                #             i = ''.join(i)
        
                        
                #         await cur1.execute(f"SELECT `Player` FROM `clan` WHERE '{person.id}' = Captin")
                #         await myDB1.commit()
                #         elcapi = await cur1.fetchall()
                #         for i in elcapi:
                #             i = ''.join(i)
                #             squadN = squadN + 1


                #         await cur1.execute(f"SELECT `Team` FROM `tournament`")
                #         await myDB1.commit()
                #         elcapi = await cur1.fetchall()
                #         for i in elcapi:
                #             i = ''.join(i)
                #             squadsN = squadsN + 1
                        
                #         if i ==  (f'{person.id}',):
                #             await person.send('you are already in the tournament')

                        
                #         else:
                #             if squadsN < 8:
                #                 if squadN > 4:
                #                     await cur1.execute(f"SELECT `Team` FROM `clan` WHERE Captin = '{person.id}'")
                #                     await myDB1.commit()
                #                     pLA = await cur1.fetchall()
                #                     for i in pLA:
                #                         i = ''.join(i)
                #                     await cur1.execute(f"INSERT INTO `tournament`(`Team`, `Captain`, `stage`) VALUES ('{i}','{person.id}','1')")
                #                     await myDB1.commit()
                #                     await person.send('you have joined the tournament')
                #                 else:
                #                     await person.send("you need a full stack to join")
                #             else:
                #                 await person.send('Sorry, tournament is full')










                            
                elif str(react) == '🤝':  
                    async with myDB1.cursor() as cur1:
                        mwjod= await fewa7d(person.id,'captin')
                        await cur1.execute(f"SELECT `Team` FROM `clan` WHERE Captin = '{person.id}'")
                        await myDB1.commit()
                        Team = await cur1.fetchall()
                        for i in Team:
                            i = ''.join(i)
                        Team = i
                            
                        if mwjod != 0:
                            player = react.message.embeds[0].description
                            player = player.split(" ")
                            Aplayer = player[-1].replace("<","")
                            Aplayer = Aplayer.replace(">","")
                            Aplayer = Aplayer.replace("@","")
                            Aplayer = Aplayer.replace("!","")
                            Aplayer = await self.client.fetch_user(Aplayer)
                            Aembed = discord.Embed( title = f'Congratulations!!', description = f"Your now a member of {Team} clan")
                            await discord.User.send(Aplayer,embed=Aembed)
                            await cur1.execute(f"INSERT INTO `clan`(`Team`, `Player`, `Captin`) VALUES ('{Team}','{Aplayer.id}','{person.id}')")
                            await myDB1.commit()
                




                elif str(react) == '🚫':
                    async with myDB1.cursor() as cur1:
                        mwjod = await fewa7d(person.id, 'captin')
                        await cur1.execute(f"SELECT `Team` FROM `clan` WHERE Captin = '{person.id}'")
                        await myDB1.commit()
                        Team = await cur1.fetchall()
                        for i in Team:
                            i = ''.join(i)
                        Team = i
                            
                        if mwjod != 0:
                            player = react.message.embeds[0].description
                            player = player.split(" ")
                            Aplayer = player[-1].replace("<","")
                            Aplayer = Aplayer.replace(">","")
                            Aplayer = Aplayer.replace("@","")
                            Aplayer = Aplayer.replace("!","")
                            Aplayer = await self.client.fetch_user(Aplayer)
                            Aembed = discord.Embed( title = f'Sorry!', description = f"You have been Rejected from {Team} clan")
                            await discord.User.send(Aplayer,embed=Aembed)
                







                
                
                
                elif str(react) == '🏛':
                    async with myDB1.cursor() as cur1:
                        mwjod = await fewa7d(person.id , 'player')
                        if mwjod == 0:
                            await react.message.delete()
                            await person.send('Please type youre clan name')
                            def check(m):
                                return m.content and m.author.id != 725433666481946736 and m.author == person
                            msg = await self.client.wait_for('message', check=check)
                            TeamN = str(msg.content.upper().replace(' ', ''))
                            await cur1.execute(f'SELECT `Team` FROM `clan`')
                            await myDB1.commit()
                            Teamm = await cur1.fetchall()
                            for i in Teamm:
                                if i== (f'{TeamN}',):
                                    Tmwjod = Tmwjod+1
                                else:
                                    pass
                            
                            if Tmwjod == 0:
                                await cur1.execute(f"INSERT INTO `clan`(`Team`, `Player`, `Captin`) VALUES ('{TeamN}','{person.id}','{person.id}')")
                                await myDB1.commit()
                                await person.send('You just created your team')
                            else:
                                await person.send(f'{TeamN} is taken, please try again')
                
                
                
                
                
                
                elif str(react) == '🚶‍♂️':
                    async with myDB1.cursor() as cur1:
                        mwjod = await fewa7d(person.id,'player')
                        if mwjod != 0:
                            await react.message.delete()
                            Pembed = discord.Embed( title = 'Are you sure you want to leave the clan?', description = None, colour = discord.Colour.blue())
                            Pembed.add_field(name="✅", value=f"YES", inline=True)
                            Pembed.add_field(name="🛑", value=f"NO", inline=True)
                            PbotMSG = await person.send(embed=Pembed)
                            await PbotMSG.add_reaction('✅')
                            await PbotMSG.add_reaction('🛑')

                
                
                
                
                
                
                elif str(react) == '✅':
                    async with myDB1.cursor() as cur1:
                        mwjod = await fewa7d(person.id , 'player')
                        if mwjod != 0:  
                            await cur1.execute(f'DELETE FROM `clan` WHERE Player = {person.id}')
                            await myDB1.commit()
                            await react.message.delete()
                            await person.send('You just left your team')

                
                
                
                

                elif str(react) == '📄':
                    async with myDB1.cursor() as cur1:
                        await cur1.execute(f'SELECT `name` FROM `whatever` ')
                        await myDB1.commit()
                        pLA = await cur1.fetchall()
                        for i in pLA:
                            if i== (f'{person.id}',):
                                mwjod = mwjod+1
                            else:
                                pass
                        if mwjod != 0: 
                            await person.send('please write your new Uplay name')
                            def check(m):
                                return m.content and m.author.id != 725433666481946736 and m.author == person
                            msg = await self.client.wait_for('message', check=check)
                            playerN = str(msg.content.upper().replace(' ', ''))
                            await cur1.execute(f"UPDATE `whatever` SET `uplay`='{playerN}' WHERE name = '{person.id}'")
                            await myDB1.commit()
                            Pembed = discord.Embed( title = 'Your Uplay name has been changed', description =f"New name: {playerN}", colour = discord.Colour.blue())
                            await person.send(embed=Pembed)


                
                
                elif str(react) == '🛑':
                    mwjod = await fewa7d(person.id, 'player')
                    if mwjod != 0 :
                        await react.message.delete()
                            
                        

                
                
                
                
                elif str(react) == '🏰':
                    async with myDB1.cursor() as cur1:
                        mwjod = await fewa7d(person.id,'player')
                        await cur1.execute(f"SELECT `Team` FROM `clan` WHERE Player = '{person.id}'")
                        await myDB1.commit()
                        Teamk = await cur1.fetchall()
                        for i in Teamk:
                            i = ''.join(i)
                            
                        Teamk = ''.join(i)
                        
            
                        if mwjod != 0:
                            await react.message.delete()
                            await cur1.execute(f"SELECT `Player` FROM `clan` WHERE Team = '{Teamk}'")
                            await myDB1.commit()
                            Players = await cur1.fetchall()
                            alteam = []
                            for i in Players:
                                i = ''.join(i)
                                alteam.append(i) 
                            count = 1
                            player_string = ""
                            for i in alteam:
                                player_string = f"{player_string}" + f"{count} - " + f"<@{i}>" + "\n"
                                count  = count +1
                            embed = discord.Embed( title = f'Team Members', description = f"{player_string}", colour = discord.Colour.blue())
                            await person.send(embed=embed)



                elif str(react) == '🖊':
                    await react.message.delete()
                    async with myDB1.cursor() as cur1:
                        await cur1.execute(f"SELECT `name` FROM `whatever` WHERE name = '{person.id}'")
                        await myDB1.commit()
                        pLA = await cur1.fetchall()
                        for i in pLA:
                            if i== (f'{person.id}',):
                                mwjod = mwjod+1

                        if mwjod == 0 :
                            embed = discord.Embed( title = f'Register', description = "Please type youre Uplay name:", colour = discord.Colour.blue())
                            def check(m):
                                return m.content and m.author.id != 725433666481946736 and m.author == person
                            await person.send(embed=embed)
                            msg = await self.client.wait_for('message', check=check)
                            playerN = str(msg.content.upper().replace(' ', ''))
                            await cur1.execute(f"SELECT `uplay` FROM `whatever`")
                            await myDB1.commit()
                            pLAs = await cur1.fetchall()
                            for i in pLAs: 
                                if i== (f'{playerN}',):
                                    mwjod = mwjod+1
                            if mwjod != 0 :
                                await person.send('you already have been Registered')
                            else:
                                await cur1.execute(f"INSERT INTO `whatever`(`name`, `uplay`, `Platform`, `MMR`, `Games_Played`, `Games_won`, `Games_Lost`) VALUES ('{person.id}','{playerN}','pc',2500,0,0,0)")
                                await myDB1.commit()
                                embed = discord.Embed( title = f'Congratulations!!', description = f"You have been Registered Successfully as {playerN}", colour = discord.Colour.red())
                                await person.send(embed=embed)
    
                
                elif str(react) == '🥾':
                    async with myDB1.cursor() as cur1:
                        await react.message.delete()
                        mwjod = await fewa7d(person.id, 'player')
                        
                        if mwjod != 0 :
                            await cur1.execute(f"SELECT `Player` FROM `clan` WHERE Captin = '{person.id}'")
                            await myDB1.commit()
                            Players = await cur1.fetchall()
                            alteam = []
                            for i in Players:
                                i = ''.join(i)
                                if i == f'{person.id}':
                                    pass   
                                else:
                                    alteam.append(i)
                            
                            player_string = ""
                            for i in alteam:
                                player_string = f"{player_string}" + f"{i}  =>" + f"<@{i}>" + "\n"
                                
                            
                            embed = discord.Embed( title = f'Which player?', description = "Please write player's Number you want to kick \n" + f"{player_string}", colour = discord.Colour.red())
                            await person.send(embed=embed)
                            def check(m):
                                return m.content and m.author.id != 725433666481946736 and m.author == person
                            msg = await self.client.wait_for('message', check=check)
                            playerN = str(msg.content.upper().replace(' ', ''))
                            if playerN in alteam:
                                playerN = await self.client.fetch_user(playerN)
                                Aembed = discord.Embed( title = f'Sorry!!', description = f"You have been kicked from {person.mention} team")
                                await discord.User.send(playerN,embed=Aembed)
                                await cur1.execute(f"DELETE FROM `clan` WHERE Player = '{playerN.id}'")
                                await myDB1.commit()
                                await person.send(f"{playerN.mention} got kicked")




                            else:
                                await person.send('Please try again and type the exact number')  


def setup(client):
    
    client.add_cog(Reaction(client))
                    

   
                  