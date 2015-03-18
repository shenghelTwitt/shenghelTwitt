import scraper
import extraction
global footballsWords#textlist
global programmingWords#

footballsWords =  pickle.load(open("footballWords.st", "rb"))
programmingWords = pickle.load(open("programmingWords.st", "rb"))

def getTwittAttract(keywords):
	attraction = [0, ,0]
	for word in keywords:
		if keywords[word] in footballsWords:
			
	
passedUsers = []
inQueueUsers = [] 
while (len(users_queue)>0):
	user = inQueueUsers[0]
	twitts = user.get_twitt()
	keywords = []
	for twitt in twitss:
		keyWords.append(extraction.getKeyWords(twitt, 3)
		
