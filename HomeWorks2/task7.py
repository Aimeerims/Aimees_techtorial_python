# 1. Ask the user to enter a random word using input function.
# 2. Then ask the user to input the number of letters that word consists of.
# 3. Lastly ask the user for a letter that they want to learn its index. 
# 4. Your code should print True if the user entered a right number of letters in the
# word. Print False if the wrong number is entered.
# 5. Your code should print the index of the entered letter, if the word doesn’t
# contain the letter then the code should print -1.
# 6. Please look at the example output below to understand how your code
# should work. 
# EXAMPLE OUTPUT:
# Enter a random word  
# Techtorial -> this line represents user's input
# Enter number of letter that word consists
# 10 -> this line represents user's input
# True
# Enter a letter that you want to find an index
# a -> this line represents user's input
# 8

random=input("Enter a random text: ")
lenght_of_string = int(input("How many letters or spaces your text consist of?"))
print(lenght_of_string == len(random))
index=input("Which letters index do you want to learn?")
print(random.find(index))


# Yusuf Solution 

print("Enter a string")
s1 = input()

print("Enter the number of the letters in the string")
user_guess = int(input())

print("Enter any letter that you want to learn its index")
letter = input()

is_guess_correct = len(s1) == user_guess
print(is_guess_correct)

print(s1.find(letter))
