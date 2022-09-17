
# Ask user to enter two numbers, first is greater than the second one. 
# Find out sum of all the numbers between given two numbers not inclusive. 3
# first number is 7
# second number is 3
#  4 5 6  -> 15 
# first number is 9
# second number is 6
# 6    7 8     9  -> 15
# first num 11
# second num is 7
# 7    8 9 10     11 -> 27 
print("Enter a number")
num1 = int(input())
print("Enter a number smaller than first one")
num2 = int(input())

#Before we get to the sum let's print all the numbers between given two number
copyOfnum2 = num2
num2 = num2 +  1
sum = 0
while num2 < num1:
  #  print("In the loop",num2)
  sum += num2
  num2 = num2 +1
print(f"Sum of the numbers between {num1} and {copyOfnum2} is {sum}")  








