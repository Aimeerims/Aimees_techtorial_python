# Ask user to enter a password
# If the password doesnot have any uppercase or does not have any lower 
# case print False otherwise True

# password should have upper case and should have lower case 
# 'password' will be equal to its lower case version

print("Enter your password with upper and lower case letter ")
password = input()
is_there_upper = password != password.lower()

# "password" will be equal to its upper case version
# if the password is not equal to its upper case version
# it means there is lower case in the string

is_there_lower = password != password.upper();

is_valid_pass = is_there_lower and is_there_upper

print("Your password is valid", is_valid_pass)




