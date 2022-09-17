
a = 5
print(a)

a = a + 10
print(a)
# It will be dispaly 15 because we redefine ( reassign ) the value of the variable a


b = 4         # remember a is 15
b = b * a     # 4*15
# What will be the output of print on the line? 
print(b)


a = a - b + b/4 + a*7 -7
# first prior b/4 division  = 60/4=15 division (always look from left to right)
# second prior a*7 multiplication 15*7=105
# a is 15, b is 60,
# a=15-60+15+105-7
# What will be the output of print on the line? 
print(a)
