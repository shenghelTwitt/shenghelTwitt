import scraper
import extraction
global footballsWords#textlist
global programmingWords#

footballsWords =  pickle.load(open("footballWords.st", "rb"))
programmingWords = pickle.load(open("programmingWords.st", "rb"))

def getTwittAttraction(twitt):
	global footballsWords#textlist
	global programmingWords#
	attraction = [0, 0]#[football, programming]
	football = 0
	programming = 1
	keywords = extraction.getKeyWords(twitt, 4)
	for word in keywords:
		if keywords[word] in footballsWords:
			attraction[football] +=1
		if keywords[word] in programmingWords:
			attraction[programming] +=1
	if attraction[football] == attraction[programming]:
		if  attraction[football] == 0:
			return [0, 0]
		return [1, 1]	
	if attraction[football] > attraction[programming]:
		for word in keywords:
			if word not in footballsWords:
				footballsWords.append(word)
		return [1, 0]
	else :
		for word in keywords:
			if word not in programmingWords:
				programmingWords.append(word)
		return [0, 1]
		
def getUserAttraction(user):
	user_attraction = [0, 0]
	twitts = user.get_twitt()
	for twitt in twitss:
		temp_attraction = getTwittAttraction(twitt)
		user_attraction[0] += temp_attraction[0]
		user_attraction[1] += temp_attraction[1]
	return [user_attraction[0] / len(twitts), user_attraction[1] / len(twitts), len(twitts)]
		
		
passedUsers = []
inQueueUsers = [] 
while (len(inQueueUsers) > 0):### in bayad bere tu thread (ye lock ham bayad bara in lista accuire beshe)
	user = inQueueUsers[0]
	user.attraction = getUserAttraction(user)
	inQueueUsers += user.get_flwing
	passedUsers.append(user)
	del inQueueUsers[user]

pickle.dump(footballsWords, open("footballWords.st", "wb"))
pickle.dump(programmingWords, open("programmingWords.st", "wb"))
