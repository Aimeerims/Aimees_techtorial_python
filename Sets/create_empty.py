s = set()

print(type(s)) # set
print(s)
s.add("new value")

print(s)

s = {} # dict

print(type(s))

# using set() function we can convert lists in to set
# How we can remove the duplicates from the list below?
list = ["s","s",2,2,4,5,7,3,6,3,2]

set1 = set(list)
print(set1)
print(type(set1)) # set

# Clear method

set1.clear()
print(set1)
print(type(set1)) # <class set> 

# Copy method

list = ["s","s",2,2,4,5,7,3,6,3,2]

set1 = set(list)
print("From line 31",set1)

set2 = set1.copy()
print(set1 == set2)
print("set 2 from line 35",set2)
print(type(set2)) # set