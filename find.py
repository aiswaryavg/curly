sentence=input("Enter the string:")
word=input("ENter a word to search:")
if sentence.find(word) !=-1:
	print(word,"is Present in",sentence)
	b=sentence.count(word)
	print(b,"times")
else:
	print("not present")

