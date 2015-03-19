from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import urllib2
from BeautifulSoup import BeautifulSoup

import scraper
import extraction








global Tuple
Tuple = []
###########
######################################################milad
footballsWords =  pickle.load(open("footballWords.st", "rb"))
programmingWords = pickle.load(open("programmingWords.st", "rb"))
##################

################main################main##################main##################main#####
"""threadList = [myThread(0),myThread(1),myThread(2),myThread(3),myThread(4)]


myPro = Profile()

for i in range(len(myPro.flwing)):
    pro.append(Profile(myPro.flwing[i],userName))
pause = False
userNumb = 0
while not pause:
    for threadUser in threadList:
        threadUser.get_user(pro[userNumb*threadUser.ID])
        threadUser.start()
    userNumb += 1"""
############################################
passedUsers = []
inQueueUsers = []
if len(inQueueUsers) == 0:
    myPro = Profile()
    inQueueUsers += myPro.obj_flwing()
############################################
global pause
pause = False

def filmsooper(i):
    user = inQueueUsers[i]
    if user not in passedUsers:
        user.attraction = getUserAttraction(user)
        inQueueUsers += user.obj_flwing
        passedUsers.append(user)

def do_pause():
    while(1):
        a = input()
        if a == 'pause':
            pause = True
#############################################
checkThread
threads = []
for i in range(5):
    checkThread.append(threading.Thread(target=filmsooper, args=i))
pauseThread = threading.Thread(target = do_pause)
#############################################
while not pause:### in bayad bere tu thread (ye lock ham bayad bara in lista accuire beshe)
    for i in range(5):
        checkThread.start()
    for t in checkThread:
        t.join()
    for i in range(5):
        del inQueueUsers[i]
pickle.dump(footballsWords, open("footballWords.st", "wb"))
pickle.dump(programmingWords, open("programmingWords.st", "wb"))


