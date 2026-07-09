# 125 Valid palidrome

def isPalindrome(s:str) -> bool:

	cleaned = ''.join(filter(str.isalnum,s)).upper()
	return cleaned == cleaned[::-1]


s = 'racecar'
print(isPalindrome(s))


## Two Sum II

def twoSum(numbers:List[int], target: int) -> List[int]:
	dict = {}
	
	for i  in range(len(numbers)):
		if numbers[i] in dict:
			return [dict[numbers[i]],i]
		else:
			partner = target - numbers[i]
			dict[partner] = i
	

