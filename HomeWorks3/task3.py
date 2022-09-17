# Ask the user to enter one number between 1 to 10 then, 
# Write the program to print the string in the following format:
# Search to see what happens when you multiply the string with
# numbers and use it for solving this question.

# Example: 
# Input: 5 
# Output: 
# 1
# 22
# 333
# 4444
# 55555

print("Enter number")
num = int(input())

for i in range(1,num+1):
    for number in range(1, i+1):
        print(i, end="")
    print()


# print("Enter one number between 1 to 10: ")
# num = int(input())
# startingNumber = 0
# multiplyNumber = ""
# while startingNumber < num:
#     multiplyNumber += str(num)
#     startingNumber+=1

# print(multiplyNumber)









