import os
from tkinter.messagebox import NO
from unicodedata import name
import discord
import json
import random
import time
from functions import *
from datetime import datetime
from datetime import date
from discord.ext import commands
jsonfile = open('package.json')
jsondata = jsonfile.read()
obj = json.loads(jsondata)

Intents=discord.Intents.all() 
Intents.members=True 
client=commands.Bot(command_prefix='=',intents=Intents)
client.remove_command("help")
link="https://discord.gg/bZcT9EqWdN"
help_message = """Commands:

=help : For help.
=test : Test if the bot is up or not.
=banroulette <user1> <user2> ... : Ban a random user in the list.
"""

@client.event
async def on_ready():
  print('Logged as {0.user}'.format(client))

@client.command()
@commands.has_permissions(kick_members=True)
async def banroulette(ctx, *members: discord.Member):
  datet = get_date_and_time()
  if not members:
    await ctx.send("Please enter a least 1 user !")
  else: 
    mess2 = []
    member_list=[]
    listMembersForLogs =""
    for member in members:
      mess2.append(member)
      listMembersForLogs += str(member)+"\n"
      datet = get_date_and_time()
      writelog(f"{datet} - {ctx.author} : =banroulette {listMembersForLogs}")
    for member in ctx.guild.members:
      member_list.append(member)

    if check_users(member_list,mess2):
      if isUserInCommand(ctx.author, mess2):
        await ctx.send("ALL USERS FOUND")
        i = random.randrange(len(mess2))
        await ctx.send(mess2[i].id)
        user = client.get_user(mess2[i].id)
        maxUserRole = maxRoleUser(mess2[i])
        botMember = botToMember(ctx,client.user.id)
        maxBotRole = maxRoleUser(botMember)
        if maxUserRole < maxBotRole:
          for x in range(3):
            await ctx.send(3-x)
            time.sleep(1)
          await ctx.send(str(mess2[i]) + " has been banned !")
          await user.send("Don't cry !\nClick here : "+str(link))
          await mess2[i].kick()
        else:
          await ctx.send("Can't ban this user.")
      else:
        await ctx.send("If you want to play, you have to be part of the game 😈")
    else: 
      await ctx.send("INCORRECT USERS")
  #Functions :

@client.command()
async def test(ctx):
  datet = get_date_and_time()
  mess = "I'm up !"
  await ctx.channel.send(mess)
  member_list = []
  for member in ctx.guild.members:
    member_list.append(member)
  writelog(f"{datet} - {ctx.author.id} {ctx.message.content}")
  writelog(datet + " - " + "SkiBot: " + str(mess))

@client.command()
async def help(ctx):
    datet = get_date_and_time()
    writelog(f"{datet} - {ctx.author} : =banroulette {ctx.message.content}")
    await ctx.send(f"```{help_message} ```")
    writelog(datet + " - " + "SkiBot: " + str(help_message))

#Run :
client.run(obj['token'])