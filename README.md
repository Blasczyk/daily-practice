Worked on Logest Common Prefix:
- The inital problem, I found the longest prefix amoungst the whole array, though it only needed to be shared once. 
- Following this I found the longest common prefix. I used a whle loop, and array slicing to to go through individual loops. Then compared the prefix, to my sliced string. 

Better way:
- Using startswith function, then looping through strings and comparing pre= pre[:-1]

## Day 2
- length of the last word, lesson. I used split to seperate words in the string, then indexed the last words and returned it length.

- Reverse words, was solved could have been faster, and I tried to use trim in the place of strip().
- Better version: return " ".join(s.strip().split()[::-1])



