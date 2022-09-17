# User wants to deposit his money into his bank account
# he already has $200 in his account
# he has three different paychecks ( 400,600, and $350)
# he can only deposit one paychek at the time
# after he deposit all the money in the account
# he bought a phone for $599, and headphone for $299
# create a python programm to calculate his final money in the account
# use input function to get all the values

# user_account = 200
# user_paychek1 = 400
# user_paychek2 = 600
# user_paychek3 = 350

# print(user_account+user_paychek1+user_paychek2+user_paychek3)

# phone = 599
# headphone = 299 


bank_acct = 200

print("Please enter the first paycheck amount you want to deposit")

first_deposit = int(input())

bank_acct += first_deposit   # this is exactly same as doing bank_acct = bank_acct + first_deposit

print("Please enter the second paycheck amount you want to deposit")

second_deposit = int(input())

bank_acct += second_deposit

print("Please enter the third paycheck amount you want to deposit")

third_deposit = int(input())

bank_acct += third_deposit
print("Please enter the dollar amount of phone you want to but")
phone = int(input())

bank_acct -= phone

print("Please enter the dollar amount of head phone you want to buy")
head_phone = int(input())

bank_acct -= head_phone
print("His final money in the bank account is",bank_acct)
