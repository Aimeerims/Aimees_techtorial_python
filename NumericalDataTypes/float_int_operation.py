#every math op between float and int data type will result in float data type 

floatnum = 3.0
intnum = 5 

print( " type of floatnum is", type (floatnum))
print("type of intnum is", type(intnum))

addition = floatnum = intnum
print("addition of float and int is",type(addition))

substruction = intnum - floatnum
print("subsruction between int and float is", type(substruction))

multiplication = floatnum * intnum
print("multiplication between int data type and float is", type(multiplication))

division = intnum / floatnum
print("the division between float and int is", type(division))

remainder = floatnum % intnum
print("The remainder between float and int data type is ", type(remainder))

remainder2 = intnum % floatnum
print("The remainder between float and int data type is", type (remainder2))

# There is only one way to get int which is using //
int_division = floatnum // intnum
print("The integer symbol division result between float and integer is", type(int_division))

square_of_float = floatnum * floatnum
print(type(square_of_float))
