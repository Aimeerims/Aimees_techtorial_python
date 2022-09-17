
# Create a python program to give 
# most efficient exchange possible using only 
# coins 
# quarter 25 cent
# nickel 5 cents
# dime is 10 cents
# penny 1 cent
# $2.34 exchange
# 9 quarters 
# 0 dimes 
# 1 nickel 
# 4 pennies
# $1.89
# 7 quarters 1 dimes and 0 nickels 4 pennies
dollar = 2.96
print(type(dollar))
dollar_amount = dollar * 100
print(type(dollar_amount))
quarter_value = 25
dime_value = 10
nickel_value = 5
penny = 1                     # sometimes with decement numbers it will give wrong result
              #2.96 // .25 11
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