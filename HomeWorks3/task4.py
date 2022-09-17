# Ask the user to enter one in number between 1 to 10 then, 
# Write the program to print the string in the following format:
# Search to see what happens when you multiply the string with
# numbers and use it for solving this question.
# Example:
# Input: 6
# Output:
# 666666
# 55555
# 4444
# 333
# 22
# 1

# print("Enter number")
# num = int(input())
# start = 1
# start2 = 1
# while start > num:
#     while start2 > num:
#         print(num)
#         start2 -=1
#     start-=1


print("Enter number")
num = int(input())

for i in range(6, num+1):
    for number in range(1, i+1):
        print(i, end="")
        print()
