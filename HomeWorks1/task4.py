# Write a program that will accept 5 digit number and
# will print reversed number at the end.
# Example-1: 
# 53876
# The output is 67835
# Example-2: 
# 97352
# The output is 25379


# print("Enter the 5 digit number")
# s = str (input())
# print(s[4],s[3],s[2],s[1],s[0])


print("Enter the 5 digit number")
s = str(input())
#number = 12345
print(s[:: -1])

# second version

# number = 12345
# number = str(number)           # i cast number to string
# print(number[:: -1])

# 3 rd version

# Finding the remainder by 10 will always get the last digit of the number
# If we divide any number by 10 and reassign it to itself we will get rid of the last digit.

number = 23456
last_digit = number % 10

number //=10                  # we get rid of the actual last digit of the number on this line

fourth_digit = number % 10
number //=10

third_digit = number % 10 
number //=10

second_digit = number % 10
number //=10
first_digit = number % 10 
number //=10


print(last_digit,fourth_digit,third_digit,second_digit,first_digit)

