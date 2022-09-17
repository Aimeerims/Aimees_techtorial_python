# Ask user to enter an integer number 
# and print multiplication table for given number

# 3 * 1 = 3 
# 3 * 2 = 6  
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# .....
# .....
# 3 * 10 = 30

print("enter a number")
num = int(input())

#  to use the loop i need to find the range
# On which number multiplication table starts - 1
# On which multiplication table ends - 10

table_num = 1
while table_num<11:
    print(f"{num} * {table_num} = {num*table_num}")
    table_num +=1