from datetime import date
from datetime import datetime
from operator import truediv
import discord
def writelog(message):
    f = open("logs/logs.txt", "a")
    message = message.encode('latin1','ignore').decode('latin1','ignore')
    f.write(f"{message} \n")
    f.close()

def get_date_and_time():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    d1 = today.strftime("%d/%m/%Y")
    dateandtime = str(d1) + " " + str(current_time)
    return dateandtime

def check_users(users_list_array, listUser):
    found = 0
    for user in users_list_array:
        for userr in listUser:
            if user == userr:
                found+=1
    print(str(found) + " users found !")
    if found == len(listUser):
        return True
    else :
        return False

def maxRoleUser(member: discord.Member):
    max = 0
    for role in member.roles:
        if role.position > max:
            max = role.position
    return max

def botToMember(ctx,id):
    for member in ctx.guild.members:
        if member.id == id:
            return member

def isUserInCommand(member, mess2):
    for user in mess2:
        if user.id == member.id:
            return True
    return False

def retrieveUser(member, member_list):
    print(member.id)
    for user in member_list:
        if user.id == member.id:
            return user.name