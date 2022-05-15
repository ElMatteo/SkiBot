from datetime import date
from datetime import datetime
from operator import truediv

def writelog(message):
    f = open("logs/logs.txt", "a")
    f.write(str(message) + "\n")
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
    print(found)
    if found == len(listUser):
        return True
    else :
        return False