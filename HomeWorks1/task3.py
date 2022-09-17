# Example 2:
# Please enter your balance:
# 5.22
# Output: 
# $5.22 will make 20 quarters 2 dimes 0 nickels and 2
#           pennies


dollar = 5.22
dollar_amount = dollar * 100

quarters = 25
dimes = 10
nickels = 5
pennies = 1

print("Please Enter your balance:")
s = input()

count_of_q = dollar_amount // quarters
print("We need to give back",count_of_q, "quarters") 
                          
remaining_exchange_after_q = dollar_amount % quarters
count_of_d = remaining_exchange_after_q // dimes
print(count_of_d , "dimes")

remaining_exchange_after_d = remaining_exchange_after_q % dimes
count_of_nickel = remaining_exchange_after_d // nickels
print(count_of_nickel, "nickels")

remaining_after_nickel = remaining_exchange_after_d % nickels
count_of_pennies = remaining_after_nickel // pennies
print(count_of_pennies,"pennies")



# Yusuf solution

# total_value = 2.89 # this is a dollar amount
# value_in_cents = 100 * total_value # value of the dollar amount in cents

# value_of_q = 25
# value_of_d = 10
# value_of_n = 5
# value_of_p = 1 

# number_of_q = value_in_cents // value_of_q  # (100*2.89) // 25

# remaining_balance = value_in_cents % value_of_q

# number_of_dimes = remaining_balance // value_of_d
# remaining_balance = remaining_balance % value_of_d

# number_of_n = remaining_balance // value_of_n
# remaining_balance = remaining_balance % value_of_n

# number_of_pennies = remaining_balance // value_of_p

# print(f"""You will get {number_of_q} amount quarters, {number_of_dimes} amount of dimes,
# {number_of_n} amount of nickels and lastly you will get {number_of_pennies} amount of pennies.""")

