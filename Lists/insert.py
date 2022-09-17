#
list = [11,7,44,6,8]

# inset the number 9 on the index number 4

list.insert(4,9)
print(list) # [11,7,44,6,9,8]

# insert method will take two parameters first is for index number
# second one is for the value of new element. 

# [11,7,44,6,9,8]
list.append(33)
print(list) # [11,7,44,6,9,8,33]

# If you provide bigger index than you have it will insert the 
# new element at the end of the list. 
list.insert(10,"new element")
print(list)

# What do you think the output? 
# This will create an error.
#Number of arguments for append is exactly 1
#list.append(4,90)

items = [2,3,4,5]

items.insert(2,1) # prints 2,3,1,4,5













