# Length of last word

def lengthOfLastWord(s:str) -> int:
	l = s.split()
	last_word = l[-1]
	
	print(f" the last word {last_word} its length is {len(last_word)}")
	return len(last_word)


#s = "Hello World"
#lengthOfLastWord(s)


# Next Question: reverse the words in a string
def reverseWords(s:str)->str:
	newstring =""
	l = s.split()

	for word in reversed(l):
		newstring = newstring + " " + word
		print(word)
	return newstring.strip()

s = "The sky is blue"

print(reverseWords(s))

