# Write a program that will take a given amount of
# money and return the number of dollars in quarters,
# dimes, nickels, and pennies that make up that given
# amount 
# Example 1:
# Please enter your balance:
# 2.36
# $2.36 will make 9 quarters 1 dime 0 nickels and 1
# pennies

quarters = 25
dimes = 10
nickels = 5
pennies = 1

dollar_amount = 2.36 * 100
max_quarters = int (dollar_amount // quarters)
max_dimes = int((dollar_amount - (max_quarters * quarters)) // dimes)
max_nickels = int((dollar_amount - (max_quarters * quarters) - (max_dimes*dimes)) // nickels)
max_pennies = int((dollar_amount - (max_quarters * quarters) - (max_dimes*dimes) - (max_nickels*nickels)) / 1)

print("quartes: ",max_quarters,", dimes: ",max_dimes,", nickels: ",max_nickels,", pennies: ",max_pennies)




# 2 version

dollar = 2.36
dollar_amount = dollar * 100
quarter_value = 25
dime_value = 10
nickel_value = 5
penny = 1                     
              
count_of_q = dollar_amount // quarter_value  # instead of using division we used double integer division becouse you cant devide quorter
print("We need to give back",count_of_q, "quarters") 
                          
remaining_exchange_after_q = dollar_amount % quarter_value
count_of_d = remaining_exchange_after_q // dime_value
print(count_of_d , "dimes")

remaining_exchange_after_d = remaining_exchange_after_q % dime_value
count_of_nickel = remaining_exchange_after_d // nickel_value
print(count_of_nickel, "nickels")

remaining_after_nickel = remaining_exchange_after_d % nickel_value
count_of_pennies = remaining_after_nickel // penny
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

