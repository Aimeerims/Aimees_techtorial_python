


num1 = 5
num2 = 7

if num1 < num2:
    print(f"{num1} is less than {num2}") # f for formating string

if num2 < num1:
    print(f"{num2} is less than {num1}")

# If statement will execute the next line only when the given condition is True

is_num2_bigger = num2 > num1

if is_num2_bigger:
    print("num2 is biger than num1")


# Ask user to enter a string
# If user enters a string with all lower case print you entered correct case

print("Enter a string")
str = input()
is_lower = str.islower()

if is_lower:
    print("You entered correct cases")     #1
    print("because you entered all lower") #2
print("you entered a string")              #3  If you entered Techtorial this print will print whatever

# Line number 1 and 2 inside the if statement so they depend on condition,
# but number 3 is outside the if statement ( becoause no indentation) therefore,
# line number 3 doesnt depend on any condition