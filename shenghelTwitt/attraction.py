import pickle
import extraction
import os

global footballsWords#textlist
global programmingWords#

def start():
	global footballsWords
	global programmingWords
	if not os.path.exists("footballWords.st"):
		file_footballWords = open("footballWords.st", "wb")
		pickle.dump(["football", "goal","manchester united" , "man utd" , "man city" , "chelsea"
                  ,"arsenal" , "liverpool" , "F.C barcelona" , "real madrid" ,
                   "bayern munich","B.V.B" , "jueventus" , "A.C milan" ,
                   "inter milan" , "Rooney" , "Van Persie" , "Mata" , "De Gea"
                   , "Falcao" , "Di Maria" , "aguero" , "Toure" , "Nasri" ,
                   "Silva" , "Costa", "Fabregas" , "Lampard" ,"Terry","Welbeck"
                   "Ozil" , "Giroud" , "Sterling" , "sturidge" , "Neymar" ,
                   "messy" , "Suarez" , "Pique" , "Iniesta" , "Ronaldo" , "Bale"
                   , "Benzema" , "Casillas" , "Pepe" , "Robben" , "mueller" ,
                   "Ribery" , "Gotze" , "Neuer" , "Hummels" , "Reus" , "Kagawa"
                   , "Tevez" , "Pogba" , "vidal" , "Podolski" , "Icardi" ,
                   "Red Devil" , "Mia_San_Mia" , "You'll_never_walk_alone" ,
                   "Pride_of_London" , "Gunners" , "Noisy Neighburs" ,
                   "La Decima" , "Tici Taca" , "Cantona" , "CR7"], file_footballWords)#
		file_footballWords.close()
	if not os.path.exists("programmingWords.st"):
		file_programmingWords = open("programmingWords.st", "wb")
		pickle.dump(["programming", "cpp"], file_programmingWords)
		file_programmingWords.close()
	file_footballWords = open("footballWords.st", "rb")
	file_programmingWords = open("programmingWords.st", "rb")
	footballsWords =  pickle.load(file_footballWords)##behtare ke az pickle ensefade nashe
	programmingWords = pickle.load(file_programmingWords)
	
def stop():
	global footballsWords
	global programmingWords
	file_footballWords = open("footballWords.st", "wb")
	pickle.dump(footballsWords, file_footballWords)
	file_footballWords.close()
	file_programmingWords = open("programmingWords.st", "wb")
	pickle.dump(programmingWords, file_programmingWords)
	file_programmingWords.close()
	
def getTextAttraction(text):
	global footballsWords#textlist
	global programmingWords#
	attraction = [0.0, 0.0]#[football, programming]
	football = 0
	programming = 1
	keywords = extraction.getKeyWords(text, 3)
#	print "key words are :", keywords
#	print keywords
#	print "************football words are :***", footballsWords
	for word in keywords:
		#print "###",word,keywords[word], 
		if word in footballsWords: #fixed keyword[word] is a bug
			print "find a football word :", word
			attraction[football] +=1
		if word in programmingWords:
			print "find a programming word :", word
			attraction[programming] +=1
	if attraction[football] == attraction[programming]:
		if  attraction[football] == 0:
			return [0.0, 0.0]#testing 
		for word in keywords:
			if word not in footballsWords:
				footballsWords.append(word)
			if word not in programmingWords:
				programmingWords.append(word)
		return [1.0, 1.0]	
	if attraction[football] > attraction[programming]:
		for word in keywords:
			if word not in footballsWords:
				footballsWords.append(word)
		return [1.0, 0.0]
	else:
		for word in keywords:
			if word not in programmingWords:
				programmingWords.append(word)
		return [0.0, 1.0]
######################################################milad		
def getAllTextsAttraction(texts):
	texts_attraction = [0.0, 0.0]
	for text in texts:
		temp_attraction = getTextAttraction(text)
		texts_attraction[0] += temp_attraction[0]
		texts_attraction[1] += temp_attraction[1]
	if len(texts) == 0:
		return [0.0, 0.0, 0.0]
	return [texts_attraction[0] / len(texts), texts_attraction[1] / len(texts), len(texts)]		

	
