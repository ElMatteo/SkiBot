import os
from unicodedata import name
import discord
import json
import random

from functions import *
from datetime import datetime
from datetime import date
from discord.ext import commands
jsonfile = open('package.json')
jsondata = jsonfile.read()
obj = json.loads(jsondata)
Intents=discord.Intents.default() 
Intents.members=True 
client=discord.Client(intents=Intents)

help_message = """Commands:

=help      : For help.
=test      : Test if the bot is available"""

@client.event
async def on_ready():
  print('Logged as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return
    
  if message.content == '=test':
    datet = get_date_and_time()
    writelog(datet + " - " + str(message.author) + ": " + str(message.content))
    await upFunc(message)
  elif message.content == '=help':
    datet = get_date_and_time()
    writelog(datet + " - " + str(message.author) + ": " + str(message.content))
    await message.channel.send(help_message)
    writelog(datet + " - " + "SkiBot: " + str(help_message))
  elif message.content == '=mentionme':
    datet = get_date_and_time()
    writelog(datet + " - " + str(message.author) + ": " + str(message.content))
    msg = '{0.author.mention}'.format(message)
    await message.channel.send(msg)
    writelog(datet + " - " + "SkiBot: " + str(msg))
  elif message.content.startswith('=banroulette'):
    mess = message.content.split(" ") 
    mess2 = []
    mess2 = mess
    mess2.pop(0)
    if len(mess2) >= 2: 
      datet = get_date_and_time()
      writelog(datet + " - " + str(message.author) + ": " + str(message.content))
      mess = message.content.split(" ")
      member_list=[]
      listUser = ""
      ct = 0
      for member in message.guild.members:
        member_list.append("<@"+str(member.id)+">")
        listUser += (str(member.id)+"\n")

      print(mess2)
      await message.channel.send(listUser)
      writelog(datet + " - " + "SkiBot: " + str(listUser))
      if check_users(member_list, mess2):
        await message.channel.send("EVERYTHING IS READY")
        writelog(datet + " - " + "SkiBot: " + "EVERYTHING IS READY")
        i = random.randrange(len(mess2))
        print(i)
        await message.channel.send(mess2[i])
      else: 
        await message.channel.send("USERS ARE INCORRECT")
    else:
      await message.channel.send("MISSING PARAMETERS. PLEASE ENTER AT LEAST TWO USERS")
      datet = get_date_and_time()
      writelog(datet + " - " + str(message.author) + ": " + str(message.content))
      writelog(datet + " - " + "SkiBot: " + "MISSING PARAMETERS. PLEASE ENTER AT LEAST TWO USERS")   
  elif message.content.startswith("="):
      await message.channel.send("Unknown command. Please type =help")
#Functions :

async def upFunc(message):
  datet = get_date_and_time()
  mess = "I'm up !"
  await message.channel.send(mess)
  writelog(datet + " - " + "SkiBot: " + str(mess))
#Run :
client.run(obj['token'])