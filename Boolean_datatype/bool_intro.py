bool1 = True
bool2 = False
a     = 5 

# The word True in boolean numerically represented by 1
# The word False in boolean numerically represented by 0
print(bool1+5) # 6
# print(True + a) #6 
b =2 
print(bool2 *b)  # 0 False is 0. Because since the value of bool2 is False and false is represented by 0*any number will give 0

text = "Text"
# since the boolean value are not represented by text value we can not use +(addition) symbol between string and boolean
# Therefore, following line will generate an error
#print(bool1+text) #error
#-----------------------

print(bool1,text) # True Text

# we will only see numerical output with boolean only when we use mathemetical operation with other numerical data types