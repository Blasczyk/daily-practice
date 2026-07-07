Worked on Logest Common Prefix:
- The inital problem, I found the longest prefix amoungst the whole array, though it only needed to be shared once. 
- Following this I found the longest common prefix. I used a whle loop, and array slicing to to go through individual loops. Then compared the prefix, to my sliced string. 

Better way:
- Using startswith function, then looping through strings and comparing pre= pre[:-1]