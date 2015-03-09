TEXT_COUNT = 3
#text_file = open("in_file.txt", "r")
words_file = open("words.txt", "r")
words = {}
###intialize words
for line in words_file:
	splited = line.split(" ")
	words[splited[0]] = int(splited[1])
words_file.close()
###

def getWordsOfLine(line):
	splited = line.split("\s") 
	for i in range(len(splited) - 1, -1, -1):
		if splited[i] == '' or splited[i] == "\n" or splited[i] == "\s":
			del splited[i]
	print ("splited is ", splited)
	return splited
for i in range(TEXT_COUNT):
	text_file = open("in_file" + str(i) + ".txt", "r")
	for line in text_file:
		lineWords = getWordsOfLine(line)
		for word in lineWords:
			words[word] = words.get(word, 0) + 1 ###count of word ++
		
######save words in file
words_file = open("words.txt", "w")
words
for word in words:
	print(word, end="**")
	words_file.write(word + " " + str(words[word]) + "\n")
