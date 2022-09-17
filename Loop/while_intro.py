# Print numbers from 1 to 10 inclusive

num =1 
while num<=10:
    print(num)                 # is 11
    # I have to update the value of variables num in the loop so
    # condition will become false eventually
    num = num + 1
# it wil be print 1,2,3,4,5,6,7,8,9,10

# print even number that are smaller equal to 10 

num = 2
while num <=10:
    print(num)
    num = num + 2 
print(f"Value of the variable num is {num}") # is 12 last number of the loop is 12


# print even number that are smaller equal to 10 
# this time variable num is going to start from 1

num =1 
while num <= 10:
    if num%2==0:    # This line is in the while loop
      print(num)    # this line is in the while as well as in the if statement
    num += 1        # this line is in the while loop
# line below is there for to understand what value the variable num will take
# after the loop above 
print(num)  # 11


# From 1 to 20 inclusive, print every odd number in following format
# "This is an odd number {Value of number}"
# print every even number 
#"This is an even number {Value of number}"

num = 1
while num <=20:
    #In the while loop I have to decide num is currently even or odd
    if num % 2==1:                               #This line is in only while loop
        print(f"This is an odd number {num}")    #This line is in while loop also in if
    else:                                        #This line is in only while loop
        print(f"This is an even number {num}")   #This line is in while loop also in if
    #I have to update the value of the number
    num +=1                                      #This line is in only while loop 


#Example of an infinite loop.
# num =0
# while num < 1:
#     print("in the while loop")                     #This line is in the while
# print("Outside the while after the infinite loop")  #This line is outside the while



