# Write a python program to convert minutes into a number of
# years and days. 
# Test Data
# Input the number of minutes: 3456789
# Expected Output :
# 3456789 minutes is approximately 6 years and 210 days




one_hour = 60
one_day = 24 * one_hour
one_year = 365 * one_day 

#input: 3456789

print("Input the number of minutes:")
s = int(input())

year = int(s//one_year)

remainder_of_year = s % one_year
days = remainder_of_year//one_day
print(s, "minutes is approximately:", year, "years and", days, "days")




# Yusuf solutions

minutes = 3456789
minutes_in_a_year = 60 * 24 * 365
minutes_in_a_day = 60 * 24

total_number_of_years = minutes // minutes_in_a_year

remaining_minutes_after_years = minutes % minutes_in_a_year

total_days = remaining_minutes_after_years // minutes_in_a_day

print(f"{minutes} amount of minutes makes {total_number_of_years} years and {total_days} days")



