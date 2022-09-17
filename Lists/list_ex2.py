
nums = [1,2,10,11,13,17,21,26]

#From the given list find sum of all the even numbers 
# lets find sum of all the odds seperately
sum = 0
sum_odd = 0
for number in nums:
    if number % 2 == 0:
        sum += number
    else:
        sum_odd += number
print(number) # the variable number will take the last value
print("Sum of all the even numbers from list is",sum)
print("Sum of all the odd numbers is",sum_odd)    