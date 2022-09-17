# Write the program to get the string value from the specified position.
# First, ask the user to enter one String value. Then ask the user to the
# enter starting number and ending number. After that, print the value
# between the given starting and ending numbers. (Note: since the user
# does not know the python, the user starts counting from 1, and the
# ending number will be included)
# Example:
# Please enter the String value:
# Definition of Science
# Please enter the starting number:
# 2
# Please enter the ending number
# 5
# The output is:
# efin


string = input("Please enter the String value:")
start_num = int(input(" Please enter the starting number:"))-1
end_num = int(input("Please enter the ending number:"))
print(string[start_num:end_num])    # user enters 2 , 2 -1 that is "e" 


# Yusuf Solutions

print("Enter a string value")
s1 = input()

print("Please enter starting number")
starting_num = int(input())
print("Please enter ending number")
ending_num = int(input())

starting_num = starting_num -1

print(s1[starting_num:ending_num])
