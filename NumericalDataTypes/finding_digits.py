a = 981
# find the maltuplication of digits of the number a
# number a will always have three digit number
# 2 * 3 * 4 = 24
# RULES
# when we find remainder with 10, it will give us the last digit of the number
# a%10 give me reminder
# when i devide the number by 10, it will remove the last digit

#RULES
#find remander of 1 and remove last digit get rid of last digit
#find remainder 0f 8 get rid middle digit
# find reminder of 9

last_digit = a % 10
print(last_digit)
# following line will remove the last digit of variables a
a = a // 10    #-12

middle_digit = a % 10 # -2

a = a // 10    #-1

first_digit = a % 10 #-1

multiplication = last_digit * middle_digit * first_digit

print("multiplication result of all digit is",multiplication)

# integer division will give us only the integir part of the division


# find the maltuplication of digits of the number a
# number a will always have three digit number
# 2 * 3 * 4 = 24
# when we find remainder with 10, it will give us the last digit of the number

#b = 34
#print(b%10)  

#c = 67       
#print(c%10)

#d = 105     
#print(d%10)

#e = 1273     
#print(e%10)


# We remove last digit 4 to find integir division
# Integer division will give us only the integer part of the division
# For Example 
# 21 / 5 is 4.20 but if use integer division operator
# 21 // 5 is 4

#b = 34  
#print(b/10)  #34/10 = 3,4 but reminder is 3    

#c = 67       #67/10 = 3,5 but reminder is 6
#print(c%10)

#d = 105      #105/10 = 3,5 but reminder is 10
#print(d%10)

#e = 1273     #1273/10 = 3,5 but reminder is 127
#print(e%10)