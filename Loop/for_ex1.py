
# ask user a given string duplicate each letter in the given string
# input abc 
# output aabbcc
# input def
# output ddeeff

print("Enter a string")
str = input()

duplicated =""

for l in str:
    duplicated=duplicated+l
    print("THis print shows evolution of the duplicated",duplicated)
    duplicated=duplicated+l
    print("THis print shows evolution of the duplicated",duplicated)
print(duplicated)