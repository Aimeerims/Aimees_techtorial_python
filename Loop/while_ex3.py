# You have $40 in the your phone account
# After each call you will be charged $5
# print --> How much call you can make and
# print how much money left in the account after each call


acct, each_call =40, 5      # if you have $4 in acct you can not call
call_number = 1
while acct >= each_call:   
    print(f"{call_number}th call is made")
    call_number +=1
    acct = acct - each_call
    print(f"After the call i have ${acct} left")






