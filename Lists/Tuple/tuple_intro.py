fruits = ("strawberry", "apple","orange", "banana", "orange")
print(fruits)
print(type(fruits)) 

print(fruits.index("apple")) # 1
print(fruits.count("orange")) # 2

# Accesing the elements of a tuple

# We can use index numbers as we did with list.
# Getting the third element from tuple
print(fruits[2])  # orange



# Using for loop with tuples. 

for element in fruits:
    print(element)


# fruits =  ("strawberry", "apple","orange", "banana", "orange")  

# From this tuple print out first fruit name that has odd lenght.
# If there is no fruit with odd lenght print odd lenght could not be found.
odd_fruit = ""
for fruit in fruits:
    if len(fruit) % 2!=0:
        # I have found odd lenght
        odd_fruit = fruit
        break
if odd_fruit!="":
    print("First odd fruit is",odd_fruit)
else:
    print("Odd lenght fruit is not found.")


