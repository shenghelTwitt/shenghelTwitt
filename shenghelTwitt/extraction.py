import math
import pickle
import os
import copy


global docCount
global allWords
def getAllWordsFromFile():
	"""
	return all words as a dictionari  {word:[tedade kol , tedad dar sanad haye motefavet]
	"""
	"""
	words_file = open("allWords.txt", "r")
	words = pickle.dump(words)
	
	text = words_file.read()
	lines = text[:-1].split('!')
	for line in words_file:
		splited = line.split("%") 
		for i in range(len(splited) - 1, -1, -1):
			if splited[i] == '' or splited[i] == "\n":
				del splited[i]
		print ("#$$$word is :", splited[i])
		print("line is ", splited[2][0])
		words[splited[0]] = [int(splited[1]), int(splited[2][0])]
	words_file.close()
	
	print ("after initialize words")
	return words"""
	file_allWords = open("allWords.st", "rb")
	aw= pickle.load(file_allWords)
	file_allWords.close()
	#print ("#### types is ", a)
	return aw
	
def saveAllWordsToFile(words):
	"""
	save all words to file
	"""
	"""
	allWords_file = open("allWords.txt", "w")
	for word in words:
		print ("word is   :", word)
		allWords_file.write(word + "%" + str(words[word][0]) + "%" + str(words[word][1]) + "!" + "\n")
	"""
	#print("%%%%%words before save is ", words)
	file_allWords = open("allWords.st", "wb")
	temp_words = words # in bara ine ke age vasate save threadehaye dg taghir dadan napoke 
	#agar temp sakhtan tol bekeshe mipoke:D
	pickle.dump(temp_words, file_allWords)
	file_allWords.close()

def getWordsOftext(text):#get a text by file.read()
	"""
	return all words of string as a dictionary : word -> [count, weight]
	"""
	textWords = {}#word -> [count, weight]
	splited = text.split(" ") 
	bigooDchars = ['', '\n', '\s']
	for i in range(len(splited) - 1, -1, -1):
		if splited[i] in bigooDchars:
			del splited[i]
	for word in splited:
		#print ("##### word is ", word)
		textWords[word] = [textWords.get(word, [0, 0])[0] + 1, 0]
	return textWords

def getMaxOfWords(words):
	"""
	return maximum of a dictionary by word_count as a toples
	"""
	#print ("###words is : ", words) 
	maxWord = ('', 0)
	for word in words:
		#print ("$$word is : ", word)
		if words[word][0] >= maxWord[1]:
			maxWord = (word, words[word][0])
	#print("$$max is :", maxWord)
	return maxWord
	
def getNMAxOFWordsByWeight(words, n):
	"""
	return n maximum of words list
	"""
	maxes = {}
	if len(words) <= n:
		return words
	#print "in Nmax func words are :" ,words
	for i in range (n):
		#print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&")
		maxx = ('', 0)#string , weight
		for word in words:
			#print("in maxx for words[word][1] is:", words[word][1])
			if words[word][1] >= maxx[1]:
			#	print("in if e maxxx")
				maxx = (word, words[word][1])
		#print ("maxes[0] is :", maxx[0], "words[maxx[0]] is :", words[maxx[0]])
		maxes[maxx[0]] = words[maxx[0]]
		#print("$$$adding   :", maxx[0]) 
		#print "****"+str(i)+"is", maxx
		del words[maxx[0]]
	#print ("&&&in last function", maxes)
	return maxes
	
def getKeyWords(doc, keyWordCount):
	global allWords
	global docCount
	"""
	return n keyWords of a document as a dictionary word->[count, weight]
	"""
	docWords = getWordsOftext(doc)

	maxOfDocWords = getMaxOfWords(docWords)
	k = .5
	for word in docWords:
		#print "word is :", word, docWords[word]
		if(allWords.get(word) == None):	
			allWords[word] = [0,1]
			#print "in if"
			#print "docCount is :", docCount
			#print "allWords[word][1] is :", allWords[word][1]
			docWords[word][1] = math.log(docCount / allWords[word][1]) * (k + (1 - k) * docWords[word][0] / maxOfDocWords[1])
		else:
			#print "in else"
			#print "docCount is :", docCount
			#print "allWords[word][1] is :", allWords[word][1]
			docWords[word][1] = math.log(docCount / allWords[word][1]) * (k + (1 - k) * docWords[word][0] / maxOfDocWords[1])
			allWords[word][1] += 1
		allWords[word][0] += docWords[word][0]
	#print ("docWords is :", docWords)
	docCount += 1
	return getNMAxOFWordsByWeight(docWords, keyWordCount)

def initialize(): 
	global allWords
	global docCount
	"""
	intializing variables from file 
	"""
	if not os.path.exists("allWords.st"):
		pickle.dump({"hello":[1, 1]}, open("allWords.st", "wb"))
	if not os.path.exists("initializer.st"):
		open("initializer.st", "w").write("1")
	initializer_file = open("initializer.st", 'r')
	allWords = getAllWordsFromFile()
	#print("$$$$$ all words in intial is ",allWords)
	docCount = int(initializer_file.read())#doraghamio bayad movazeb bashim va in kar mikone
	initializer_file.close()
###### 

def stop():
	file_initializer = open("initializer.st", 'w')
	file_initializer.write(str(docCount))
	file_initializer.close
	saveAllWordsToFile(allWords)

