# Write a python program that reads a number in inches,
# converts it to meters.
# Note: One inch is 0.0254 meter.
# Test Data
# INCH: 2000
# Expected Output :
# 2000.0 inch is 50.8 meters

one_inch = 0.0254
inch = 2000
print(one_inch*inch)


num = int(input("Enter the inches:"))
convert = one_inch * num
print("2000.0 inches is", convert, "meters")


# Yusuf version 

# inch = 2000

# conversion_factor_to_meter = 0.0254
# inches_in_meters = inch * conversion_factor_to_meter
# print(f"{inch} inches is {inches_in_meters} meters")