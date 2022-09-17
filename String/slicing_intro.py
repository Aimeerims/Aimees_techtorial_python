#Ask user the enter a string which lenght is even and longer than 3
# and print the middle 3 letter from the string


# Chicago -> ica
# seven -> eve
print("Enter a string which lenght is odd and longer than 3")
text = input()
middle_index = len(text) // 2 # int(len(text)/2)

print(text[middle_index-1:middle_index+2])



#Ask user the enter a string which lenght is even and longer than 4
# and print the middle 4 letter from the string

# techtorial -> htor
# keyboard -> yboa

print("Enter a string which lenght is odd and longer than 4")
text = input()
middle_index = len(text) // 2 # int(len(text)/2)

print(text[middle_index-2:middle_index+2])










