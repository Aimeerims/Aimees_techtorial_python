# Ask user to enter any string value using input function.
# Then, remove all the spaces (" ") from the given string. 
# After removing the spaces from the string, 
# if the string's length is odd print True, otherwise print False. 
# Example: 
# Input : I love coding
# Output: True
# Input : one two 
# Output: False

# odd - ne chentye nomera
# even - chetnye




# s = "I love my Life"
s = input("Please enter your Text:")
# s = s.replace(" ","")
# print(s)
print(len(s.replace(" ","")) % 2 == 1)


# Nur version

# print("Enter any string with spaces")
# str = input()                 # for odd =1  for even =0
# print(len(str.repace(" ", ""))%2==1)

# yusuf solutions 

print("Enter any string with spaces")
s1 = s1.replace(" ","")
is_lenght_Odd = len(s1) % 2 !=0
print(is_lenght_Odd)