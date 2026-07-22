#Count Elements greater than Previous Average

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    if len(responseTimes) <= 1:
        return 0
        
    average = responseTimes[0]
    total = average
    count = 0
    
    for i in range(1,len(responseTimes)):
        if average < responseTimes[i]:
            count += 1
        total +=  responseTimes[i]
        average = total / (i + 1)
    return count

#Passed


## 
"""
Longest Arithmetic Subsequence with Given Difference
Given an array of integers and a positive integer k, find the length of the longest arithmetic progression with common difference k. Ignore duplicates.
"""


#My code

def findLongestArithmeticProgression(arr, k):
    arr.sort()
    l = arr[:]
    longest = 0

    while l:
        temp = []
        count = 1

        for i in range(len(l) - 1):
            diff = l[i + 1] - l[i]

            if diff == k:
                count += 1
            elif diff < k:
                temp.append(l[i])
            else:
                temp.extend(l[i + 1:])
                break

        longest = max(longest, count)
        l = temp

    return longest


#chats code

def findLongestArithmeticProgression(arr, k):
    if not arr:
        return 0

    s = set(arr)
    longest = 1

    for num in s:
        # Only start from the beginning of a progression
        if num - k not in s:
            length = 1
            curr = num

            while curr + k in s:
                curr += k
                length += 1

            longest = max(longest, length)

    return longest





