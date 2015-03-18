import scraper
import extraction
global footballsWords#textlist
global programmingWords#

footballsWords =  pickle.load(open("footballWords.st", "rb"))
programmingWords = pickle.load(open("programmingWords.st", "rb"))

def f():
	
passedUsers = []
inQueueUsers = [] 
while (len(users_queue)>0):
	user = inQueueUsers[0]
	twitts = user.get_twitt()
	for twitt in twitss:
		keyWords = extraction.getKeyWords(twitt, 3)
		
