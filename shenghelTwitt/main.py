import threading, pickle
import scraper, attraction, extraction
import os
#treadsCount = 3
##*****initialize locks*****
global lock_inQueueUsernames
lock_inQueueUsernames = threading.Lock()
global lock_passedUsers
lock_passedUsers = threading.Lock()
global lock_pause
lock_pause = threading.Lock()

##*****initialize lists*****
global passedUsers# list of passed users as user object
passedUsers = []
global inQueueUsernames# list of inqueue usernames as string
inQueueUsernames = []

##*****initialize variables*****

def isInPassedUsers(username):
	#print("in pass function")
	for user in passedUsers:
		#print("loop **")
		if user.name == username:
			return True
	return False
	
def f(i):#inam be khatere inke ziadi code stylemon shakh nabashe
	global inQueueUsernames
	global passedUsers
	global lock_inQueueUsernames
	global lock_inQueueUsernames
	global lock_pause
	while True:
		print i
		#print "salam"
		#print("len is :",len(inQueueUsernames))
		if len(inQueueUsernames) <= 0:
			#print("in if")
			continue
		#print ("before lock_pause")
		lock_pause.acquire()
		#print ("between lock_pause")
		lock_pause.release()
		#print ("after pause")
		lock_inQueueUsernames.acquire()
		username = inQueueUsernames.pop(0)
		lock_inQueueUsernames.release()
		print "user is :", username
		#print ("befor if")
		if not isInPassedUsers(username):
			print "**adding :", username
			#passedUsers.append(user) shayad inja behtar bashe
			user = scraper.User(username)
			user.attraction = attraction.getAllTextsAttraction(user.get_twitt())
			#print "after get atract"
			user_flowing = user.get_flwing()
			lock_inQueueUsernames.acquire()
			inQueueUsernames += user_flowing#age dota opener kar kone in bayad birone lock bere
			lock_inQueueUsernames.release()
			lock_passedUsers.acquire()
			passedUsers.append(user)
			lock_passedUsers.release()
fThreads = []
def start(threadsCount):
	global inQueueUsernames
	global passedUsers
	global lock_inQueueUsernames
	global lock_inQueueUsernames
	global lock_pause
	#scraper.setup_opener() bayad fix she
	extraction.initialize()
	attraction.start()
	scraper.start()
	if not os.path.exists("passedUsers.st"):
		pickle.dump([], open("passedUsers.st", "wb"))
	if not os.path.exists("inQueueUsernames.st"):
		pickle.dump(["armanjtehrani","joof"], open("inQueueUsernames.st", "wb"))
	passedUsers = pickle.load(open("passedUsers.st", "rb"))
	inQueueUsernames = pickle.load(open("inQueueUsernames.st", "rb"))
	for i in range(threadsCount):
		fThreads.append(threading.Thread(target=f, args=(i,)))
		fThreads[i].start()
		#fThreads[i].join()
	print "end of starting"
def stop():
	attraction.stop()
	extraction.stop()
	file_passedUsers = open("passedUsers.st", "wb")
	file_inQueueUsernames = open("inQueueUsernames.st", "wb")
	pickle.dump(passedUsers, file_passedUsers)
	pickle.dump(inQueueUsernames, file_inQueueUsernames)
	file_passedUsers.close()
	file_inQueueUsernames.close()
	#for thread in fThreads:
	#	thread.close()
	print "end of stop"
"""start(1)
print "after starting"
import time
for i in range (1200):
	print 1200 - i
	time.sleep(1)
print "I want stop"
stop()
print "after stop"
"""
#bayad begim ke az ki shoro kone
while True:
	faz = raw_input("What do you want to do :")
	if faz == "start":#in age tedadam vorodi begire awlie
		threadCount = input("how many thread? :")
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
		print extraction.allWords
	elif faz == "showFootballWords":
		print attraction.footballsWords
	elif faz == "showProgrammingWords":
		print attraction.programmingWords
	else:
		print ("what?")


