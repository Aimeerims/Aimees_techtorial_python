
num1 = 3
num2 = 7
num3 = 4 

#find multiply sum of num2 and num3 with num1

#sum_of_nums = num2 + num3
#result = sum_of_nums * num1
#result = num2 + num3 * num1  # it will give different result, we do not looking for this 

result = (num2 + num3) * num1
print(result) 

result2 = (num1 * (num2 - num3))*num1  # 1) num2-num3  2) num1*3 3) 3*3=9 9*3 =27
print(result2)    #result 27