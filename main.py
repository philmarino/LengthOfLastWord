def lengthOfLastWord(sentence):
    words = sentence.strip().split(' ')
    return len(words[len(words) - 1])

#Example 1:
#Input: 
s = "Hello World"
print(lengthOfLastWord(s))
#Output: 5
#Explanation: The last word is "World" with length 5.

#Example 2:
#Input: 
s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
#Output: 4
#Explanation: The last word is "moon" with length 4.

#Example 3:
#Input: 
s = "luffy is still joyboy"
print(lengthOfLastWord(s))
#Output: 6
#Explanation: The last word is "joyboy" with length 6.
 

