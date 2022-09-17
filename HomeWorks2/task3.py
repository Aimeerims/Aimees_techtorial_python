# Using the input function ask the user to enter one sentence with three
# words and print the index number of each word's last character and then
# print the sum of each index number that you found. 
# For Example: 
# Input: 
#  01234567891011121314
# "Importance of Human" --> it can be any three-word sentence. 
#  Output: 
# 9 --> index number of 'e'
# 12 --> index number of 'f'
# 18 --> index number of 'n'
# The sum: 39




# Think about using find method for finding the index of space 
# and using the split function for gettting the words.


print("Enter one sentence with three words")
s1 = input()
space1 = s1.find(" ")

last_of_first = space1-1
space2 = s1.rfind(" ")
last_of_second = space2-1
third_word = len(s1)-1
last_of_third = len(s1)-1
Total = last_of_first+last_of_second+last_of_third
print(f"the sum {Total}")


# Yusuf Solution

# How can we find last index of space in the giving string? 
# rfind(" ") will give you last index of space in the given string

len(str)-1 # gives us last index


print("Enter any text with three words")
three_words = input()

last_index_of_firstWord = three_words.find(" ")-1

last_index_of_secondWord = three_words.rfind(" ") -1 

last_index_of_lastWord = len(three_words) -1

print(last_index_of_firstWord+last_index_of_secondWord+last_index_of_lastWord)

