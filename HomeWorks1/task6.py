# Create two string variables bigger than the length 3.
# If the second string starts with the first string’s last three
# characters, print true. If not, print false.

# a = "seven" 
# b = "ven"  # if her ve it will show False

# last_3_char = a[-3:]
# is_starts_with_last_3_char = b == last_3_char
# print(is_starts_with_last_3_char)





# Yusuf solutions

# I have to find last three character of the first string

str1 = "laptop"
str2 = "topthree"

# Last index number of str1 going to be
# Last index of the string will be always be one less than the lenght of the string

last_index_of_str1 = len(str1) -1
last_three_of_str1 = str1[last_index_of_str1-2]+str1[last_index_of_str1-1]+str1[last_index_of_str1-0]

first_three_of_str2 = str2[0]+str2[1]+str2[2]

print(last_three_of_str1)
print(first_three_of_str2)
print(last_three_of_str1 == first_three_of_str2)