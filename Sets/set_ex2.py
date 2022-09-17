s  = {2,2,3,4,5,7}
s2 = {4,10,2,5,44}
print(min(s))
print (max(s2))
print(min(s)*max(s2))
# find out min number from the s and 
# multiply with the max number of s2
min = -200
max1 = 0 
#In the first iteration of the loop i should 
# change the value of the min but later on I should only change 
# it when the min is bigger than the number
# in the loop below how can I understan it is the first iteration
count_of_iteration = 0
for number in s:
    if count_of_iteration == 0:
        min = number
        max1 = number
    if number < min:
        #If code comes to this line it means min is bigger than number
        min = number
    elif number > max1:
        max1 = number    
    count_of_iteration+=1  
   


print("This is the min from the second first set",min)
print(max1)


max =0
for number in s2:
    if max == 0:
        max = number
    if max < number:
        max = number

print ("This is the maximum from the second set",max)    

print("Multiplication of min and max is", min*max)















