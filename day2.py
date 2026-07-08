# Length of last word

def lengthOfLastWord(s:str) -> int:
	l = s.split()
	last_word = l[-1]
	
	print(f" the last word {last_word} its length is {len(last_word)}")
	return len(last_word)


s = "Hello World"

lengthOfLastWord(s)
