# Given two lists a, b. Check if two lists have 
# at least one element common in them.

# Examples:

# Input : a = [1, 2, 3, 4, 5]
#         b = [5, 6, 7, 8, 9]
# Output : True

# Input : a=[1, 2, 3, 4, 5]
#         b=[6, 7, 8, 9]
# Output : False


list1 = [1, 2, 3, 4, 5]

list2 = [ 5, 6, 7, 8, 9]

# Check if two lists have 
# at least one element common in them.

set1 = set(list1)
set2 = set(list2)

# How can i check if there is common element from these two sets? 
# In the below i will get common elements from both sets above.
common_elements = set1.intersection(set2)

# If there is at least one common element what should be the size of 
# common_elements set?
# It should be at least 1.
# len(common_elements) >= 1

# if len(common_elements) >=1:
#     print("True")
# else:
#     print("False")

is_there_common = len(common_elements) >= 1

print(is_there_common)
# print(len(common_elements) >= 1)












