import threading
import scraper
import attraction

treadsCount = 3
##*****initialize locks*****
global lock_inQueueUsers
lock_inQueueUsers = threading.Lock()
global lock_pause
lock_pause = threading.Lock()

##*****initialize lists*****
global passedUsers# list of passed users as user object
passedUsers = []
global inQueueUsers# list of inqueue usernames as string
inQueueUsers = []


def isInPassedUsers(username):
	for user in passedUsers:
		if user.name == username:
			return true
	return False
	
def f():#inam be khatere inke ziadi code stylemon shakh nabashe
	lock_pause.acquire()
	lock_pause.release()
	lock_inQueueUsers.acquire()
	username = inQueueUsers.pop(0)
	lock_inQueueUsers.release()
	if not isInPassedUsers(username):
		user = scraper.User(username)
		user.attraction = getUserAttraction(user)
		inQueueUsers += user.get_flwing()
		passedUsers.append(user)


def start(treadsCount):
	#scraper.setup_opener() bayad fix she
	attraction.start()
	for i in range(treadsCount):
		fThread.append(threading.Thread(target=f))

def stop():
	attraction.stop()


while True:
	faz = raw_input("What do you want to do :")
	if faz == "start":#in age tedadam vorodi begire awlie
		start(treadsCount)
	elif faz == "stop":
		stop()
		print ("khoda hafeze hamegi")
		break
	if faz == "pause":
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

