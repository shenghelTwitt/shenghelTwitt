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


def getWordsOftext(doc):#get a text by file.read()
	docWords = {}#word -> [count, weight]
	splitedDoc = doc.split("\s") 
	bigooDchars = ['', '\n', '\s']
	for i in range(len(splited) - 1, -1, -1):
		if splitedDoc[i] in bigooDchars:
			del splitedDoc[i]
	print ("splited is ", splited)
	for word in slpited:
		docWords[word] = docWords.get(word, [0, 0])[0] + 1
	return docWords

def getMaxOfWord(words):
	maxWord = ('', 0)
	for word in words:
		if word[0] > maxWord[1]:
			maxWord = (word, word[0])
