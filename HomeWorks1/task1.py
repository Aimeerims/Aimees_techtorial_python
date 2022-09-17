# Create a program that will add up the value of a number of
# quarters, dimes, nickels, and pennies.  The number of each
# type of coin is input by the user.  The total value is printed in
# dollars.  

# Example: 
# Quarters:   5
# Dimes:       4
# Nickels:      3
# Pennies:    2
# The total in dollars is $1.82

from turtle import numinput


quarters = 25
dimes = 10
nickels = 5
pennies = 1

total_value_of_coins = (quarters*5+dimes*4+nickels*3+pennies*2)/100
print(total_value_of_coins)

amount_Quarters = 5
amount_Dimes = 4
amount_Nickels = 3
amount_Pennies = 2

total_value_of_coins2 = (quarters*amount_Quarters
+dimes*amount_Dimes
+nickels*amount_Nickels
+pennies*amount_Pennies)/100
print(total_value_of_coins2)


# Yusuf version solutions

# number_of_g = 5
# number_of_d = 4
# number_of_n = 3
# number_of_p = 2

# value_of_q = .25
# value_of_d = .1
# value_of_n = .05
# value_of_p = .01

# total_value = value_of_q*number_of_g+value_of_d*number_of_d
# +value_of_n*number_of_n+value_of_p*number_of_p
# print("total value of given coins is ${total_value}")

