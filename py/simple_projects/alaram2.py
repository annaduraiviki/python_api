import datetime
from time import sleep
import random
import webbrowser


def seconds_elapsed(current,later):
    h1,m1,s1 = current.hour,current.minute,current.second
    h2,m2,s2 = later.hour,later.minute,later.second

    current_seconds = h1*60*60 + m1*60 + s1
    later_seconds = h2*60*60 + m2*60 + s2
    return(later_seconds-current_seconds)


FMT = '%H:%M:%S'
today = datetime.datetime.now()
now = today.strftime(FMT)

x = raw_input('please enter the alarm time in HH:MM:SS format\n' )
alarmtime = datetime.datetime.strptime(x,FMT).time()
now = datetime.datetime.strptime(now,FMT).time()
sleeptime = seconds_elapsed(now,alarmtime)

print sleeptime

sleep(sleeptime)

f = open('alarm_urls.txt')
url_list = f.readlines()
url_index = random.randint(0,2)

webbrowser.open(url_list[url_index])
