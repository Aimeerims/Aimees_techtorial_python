# Ask user to enter thir age
# Print out your age is {age}
# Till their age gets to 60
print("Enter your current age")
age = int(input())

# Their age should be smaller equal to 60

while age <=60:
    print(f"Your age is {age}")
    age+=1                      # if you remove this code it will print 60 60 60 etc
                                # +1 increase by one