in_file = open("in_file.txt", "r")
rutin_file = open("rutin_words.txt", "r")#r+ : read and write

rutinWords = {} # A dictionery from word to count of that . 
#kalame hayi ke to hame matnaye mozoate mokhtalef ziad estefade mishano az matn hazf mikonim 
for line in rutin_file:
	splited = line.split(" ")
	rutinWords[splited[0]] = int(splited[1])
for word in rutinWords:
	print (word, rutinWords[word])
for line in in_file:
	splited = line.split(" ") 
	for i in range(len(splited) - 1, -1, -1):
		if splited[i] == '' or splited[i] == "\n":
			del splited[i]
	words = splited
	for i in range(len(words) - 1, -1 ,-1):
		print(words[i],end = "*")
		if words[i] in rutinWords.keys():
			rutinWords[words[i]] += 1
			del words[i]
print ("after deleting rutinWords")
for word in words:
	print(word,end = "*")
rutin_file = open("rutin_words.txt", "w")
for word in rutinWords:
	rutin_file.write(word + " " + str(rutinWords[word]) + "\n")
