# Using the input function asks the user to input the min and max number. 
# Write a python code that will calculate the sum of numbers between the range of min and max 
# and those that can only be divided by 3 and 11. 

# (min and max numbers are included)
# Example: 
# 0, 99 -> 33 + 66 + 99 = 198

print("Enter the min number")
min = int(input())
print("Enter the min number")
max = int(input())

sumOfDividibleBy3_11 = 0
for number in range(min, max+1):
    if((number % 3 == 0) and (number % 11 == 0)):
        sumOfDividibleBy3_11 += number

print(sumOfDividibleBy3_11)

