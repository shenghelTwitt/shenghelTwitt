def getAllWordsFromFile():
	"""
	return all words as a dictionari  {word:[tedade kol , tedad dar sanad haye motefavet]
	"""
	words_file = open("allWords.txt", "r")
	words = {}
	for line in words_file:
		splited = line.split("%") 
		for i in range(len(splited) - 1, -1, -1):
			if splited[i] == '' or splited[i] == "\n":
				del splited[i]
		words[splited[0]] = [int(splited[1]), int(splited[2])]
	words_file.close()
	print ("after initialize words")
	return words
	
def saveAllWordsToFile(words):
	"""
	save all words to file
	"""
	allWords_file = open("allWords.txt", "w")
	for word in Words:
		allWords_file.write(word + "%" + str(words[0]) + "%" + str(words[1]) + "\n")


def getWordsOftext(text):#get a text by file.read()
	"""
	return all words of string as a dictionary : word -> [count, weight]
	"""
	textWords = {}#word -> [count, weight]
	splitedt = text.split("\s") 
	bigooDchars = ['', '\n', '\s']
	for i in range(len(splited) - 1, -1, -1):
		if splited[i] in bigooDchars:
			del splited[i]
	print ("splited is ", splited)
	for word in slpited:
		textWords[word] = textWords.get(word, [0, 0])[0] + 1
	return textWords

def getMaxOfWords(words):
	"""
	return maximum of a dictionary by word_count as a toples
	"""
	maxWord = ('', 0)
	for word in words:
		if word[0] > maxWord[1]:
			maxWord = (word, word[0])
	return maxWord
	
def getNMAxOFWordsByWeight(words, n):
	"""
	return n maximum of words list
	"""
	maxes = {}
	for i in range (n):
		maxx = ('', 0)#string , weight
		for word in words:
			if words[word][1] > maxx[1]:
				maxx = (word, word[1])
		maxes[maxx[0]] = words[word]
		del words[word]
	return maxes
	
def getKeyWords(doc, keyWordCount):
	"""
	return n keyWords of a document as a dictionary word->[count, weight]
	"""
	docWords = getWordsOftext(doc)
	maxOfDocWords = getMaxOfWords(docWords)
	k = .5
	for word in docWords:
		docWords[word][1] = k + (1 - k) * docWords[word][0] / MaxOfDocWords
	getNMAxOFWordsByWeight(docWords, keyWordCount)
