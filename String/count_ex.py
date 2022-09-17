# Ask user to give 2 different string values
# If the first string contains the second string
# return True, if not return False

print("Give a string consists of string ")
str = input()
str2 = input()


count_of_characters_in_string = str.count(str2)
print(count_of_characters_in_string>0) 


# Version Yusuf

print("Enter first string")
s1 = input()


print("Enter second string")
s2 = input()

# If the first string doesn't contain the second string 
# count of second string in the first one should be 0

count_of_second = s1.count(s2)
is_contain = bool(count_of_second)
print(is_contain)