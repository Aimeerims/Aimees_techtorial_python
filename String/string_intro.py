str = "hello"
str1= "hello"
str2="heLlo"
print(str == str1)
# Equal equal sign is case sensitive , so if cases of the two string is different it will
# return false
print(str == str2) # False

# We can reassign and change the string values as we were able to do with other 
# data types.

str2 = "hello"
print(str2) # hello

# Since we reassign and change the value of the str2 
# equal comparison between str2 and str will give the result as True
print(str2 == str)

# Concatenating the Strings
# Concetanation is adding more string to the existing string value
str2 = str2 + " world"
print(str2) # hello world

# We can use concatenation even when we are creating the string variable first time. 

str3 = "hello "+ "world"
print(str3) # hello world

str4 = str + str1
print(str4) # hellohello