import threading, pickle
import scraper, attraction, extraction, graph
import os
#treadsCount = 3
##*****initialize locks*****
global lock_inQueueUsernames
lock_inQueueUsernames = threading.Lock()
global lock_passedUsers
lock_passedUsers = threading.Lock()
global lock_inProcessUsernames
lock_inProcessUsernames = threading.Lock()
global lock_pause
lock_pause = threading.Lock()

##*****initialize lists*****
global passedUsers# list of passed users as user object
passedUsers = []
global inQueueUsernames# list of inqueue usernames as string
inQueueUsernames = []
global inProcessUsernames
inProcessUsernames = []
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
	global lock_passedUsers
	global lock_inQueueUsernames
	global lock_pause
	while True:
		print i
		#print "salam"
		#print("len is :",len(inQueueUsernames))
		if len(inQueueUsernames) <= 0:
			print("no User in Queue")
			continue
		#print ("before lock_pause")
		lock_pause.acquire()
		#print ("between lock_pause")
		lock_pause.release()
		#print ("after pause")
		lock_inQueueUsernames.acquire()
		username = inQueueUsernames.pop(0)
		lock_inQueueUsernames.release()
		#print "user is :", username
		#print ("befor if")
		lock_passedUsers.acquire()
		is_inPassed = isInPassedUsers(username)
		lock_passedUsers.release()
		lock_inProcessUsernames.acquire()
		is_inProcess = username in inProcessUsernames
		lock_inProcessUsernames.release()
		if not is_inProcess and not is_inPassed:
			lock_inProcessUsernames.acquire()
			inProcessUsernames.append(username)
			lock_inProcessUsernames.release()
			print "**adding :", username
			#passedUsers.append(user) shayad inja behtar bashe
			user = scraper.User(username)
			user_twitts = user.get_twitt()
			lock_pause.acquire()
			lock_pause.release()
			user.attraction = attraction.getAllTextsAttraction(user_twitts)
			print "user attraction is :", user.attraction
			#print "after get atract"
			user.followingUsernames = user.get_flwing()#age dota opener kar kone in bayad birone lock bere
			"""inja chon tedade inQueueUsers ha ziade tekrari bodan dar inqueue ro bar resi nemikonim 
			ta order zamani kam beshe dar avazmoghe faghat moghe ezafe kardan be inPAssed check
			mikonim tekrari nabashe"""
			lock_pause.acquire()
			lock_pause.release()
			lock_inQueueUsernames.acquire()
			inQueueUsernames += user.followingUsernames
			lock_inQueueUsernames.release()
			lock_passedUsers.acquire()
			passedUsers.append(user)
			lock_passedUsers.release()
			lock_inProcessUsernames.acquire()
			inProcessUsernames.remove(username)
			lock_inProcessUsernames.release()
			
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
		fThreads.append(threading.Thread(target=f, args=(i,)))#in i bayad nabashe
		print fThreads[i].daemon
		fThreads[i].setDaemon(True)
		print fThreads[i].daemon
		fThreads[i].start()
		
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
#	for thread in fThreads:
	#	del thread
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
		fThreadsCount = input("how many thread? :")
		start(fThreadsCount)
	elif faz == "stop":#must be pause befor stop
		if not lock_pause.locked():
			lock_pause.acquire()
			print "bigoodi"
		stop()
		print ("khoda hafeze hamegi")
		break
	elif faz == "pause":
		lock_pause.acquire()
	elif faz == "show":
		lock_pause.acquire()
		graph.draw_graph(passedUsers)
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


