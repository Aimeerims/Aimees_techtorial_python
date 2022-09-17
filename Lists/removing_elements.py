
list = ["Python","C++","C#","Java","Ruby"]

# Remove the C# from the list? 

list.remove("C#")

print(list) #["Python","C++","Java","Ruby"]

#["Python","C++","Java","Ruby"]

# I want to remove the second element from this list.

list.pop(1)
print(list)
#['Python', 'Java', 'Ruby']

# since the -5 is not in the list it will give index error
# list.pop(-5)
# print(list)
#Index out of range error
#list.pop(12)  # error


# If you use bigger or lower indexes to get elements from iterable 
#objects you will index out of range error. 
#print(list[20])


nums = [1,2,3,4,5,6,7]

nums.pop(5)

print(nums) #

#[1, 2, 3, 4, 5, 7]
nums.remove(5)
print(nums)

# nums.remove(5)

# print(nums)


nums = [1,2,3,5,4,5,6,7]

# It will remove the first 5 that exist in the list. 
nums.remove(5)

print(nums)

nums.clear()

print(nums)
