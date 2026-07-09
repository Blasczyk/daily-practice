import math

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


# Zig zag conversion

def convert(s:str, numRows: int) -> str:
	newstring =""
	sList = list(s)
	# find matrix num of collumns
	# 14 letters 4 rows, 6 letters per cyle -> 3 cycles, columns per sycle are numRows - 1
	string_len = len(s)
	cycle_size = (numRows * 2) - 2
	num_cycles = math.ceil(string_len / cycle_size)
	#build matrix
	numCol = num_cycles * (numRows -1) 
	
	pattern = [numRows][numCol]

	index = 0
	cyle_count = 1
	
	while cylce_count >0:
		for i in range(numCol):

			for j in range(numRows):
				if j % (numRows -1) == 0:
					[i][j] = sList[index]
					index += 1
	

				elif 
			




	
