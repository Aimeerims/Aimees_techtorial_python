# Reverse a given String and print it, if they have space in the
# beginning and at the end then remove it.  
# Without using slicing [ : :-1]. Try doing with for loop or while loop. 

# Example:  " Job" -> "boJ" 
#  * " Happy " -> "yppaH" 
#  * "Sun " -> "nuS" 
#  * " Dream Job!" -> "!boJ maerD" 

print("Enter your word ")
str = input().strip()

reverse_string = ""
count = len(str) # 5

while count > 0:
    reverse_string+=str[count-1]
    count -= 1
print("The reversed string using a while loop is:", reverse_string)