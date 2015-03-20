import threading, pickle
import scraper, attraction
import os
#treadsCount = 3
##*****initialize locks*****
global lock_inQueueUsernames
lock_inQueueUsernames = threading.Lock()
global lock_inQueueUsernames
lock_passedUsers = threading.Lock()
global lock_pause
lock_pause = threading.Lock()

##*****initialize lists*****
global passedUsers# list of passed users as user object
passedUsers = []
global inQueueUsernames# list of inqueue usernames as string
inQueueUsernames = []


def isInPassedUsers(username):
	for user in passedUsers:
		if user.name == username:
			return true
	return False
	
def f():#inam be khatere inke ziadi code stylemon shakh nabashe
	lock_pause.acquire()
	lock_pause.release()
	lock_inQueueUsernames.acquire()
	username = inQueueUsers.pop(0)
	lock_inQueueUsernames.release()
	if not isInPassedUsers(username):
		#passedUsers.append(user) shayad inja behtar bashe
		user = scraper.User(username)
		user.attraction = getUserAttraction(user.get_twitt())
		lock_inQueueUsernames.acquire()
		inQueueUsernames += user.get_flwing()
		lock_inQueueUsernames.release()
		lock_passedUsers.acquire()
		passedUsers.append(user)
		lock_passedUsers.release()
fThreads = []
def start(threadsCount):
	
	#scraper.setup_opener() bayad fix she
	attraction.start()
	if not os.path.exists("passedUsers.st"):
		pickle.dump([], open("passedUsers.st", "wb"))
	if not os.path.exists("inQueueUsers.st"):
		pickle.dump([], open("inQueueUsers.st", "wb"))
	passedUsers = pickle.load(open("passedUsers.st", "rb"))
	passedUsers = pickle.load(open("inQueueUsers.st", "rb"))
	for i in range(threadsCount):
		fThreads.append(threading.Thread(target=f))

def stop():
	attraction.stop()
	pickle.dump(passedUsers, open("passedUsers.st", "wb"))
	pickle.dump(inQueueUsernames, open("inQueueUsernames.st", "wb"))

#bayad begim ke az ki shoro kone
while True:
	faz = raw_input("What do you want to do :")
	if faz == "start":#in age tedadam vorodi begire awlie
		#threadCount = input("how many thread? :")
		threadsCount = 1
		start(threadsCount)
	elif faz == "stop":
		stop()
		print ("khoda hafeze hamegi")
		break
	elif faz == "pause":
		lock_pause.acquire()
	elif faz == "show":
		lock_pause.acquire()
		showGraph()
	elif faz == "resume":
		lock_pause.release()
	elif faz == "showAllWords":
		pass
	elif faz == "showFootballWords":
		pass
	elif faz == "showProgrammingWords":
		pass
	else:
		print ("what?")
