s = "Python"
print(s.islower()) #False
# False because, it returns True when the string has only lower case letter

print(s.lower().islower())
# True because the lower method makes all letters in lower case

s.upper() 
print(s.isupper()) # False using method in string will not effect the original value of the string



# Ask user to enter their name in uppercase
# If they didn't enter in upper cases print false

print("Enter your first name in upper cases")
first_name = input()

print(first_name.isupper())