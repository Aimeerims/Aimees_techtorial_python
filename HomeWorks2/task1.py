# Please use method chaining for the following Strings. 
# Methods are provided next to the String.
# String “ Snicker " —> strip, upper, remove prefix and slice the string with
# any number of your choice
# String “Cookie” —> lower, replace ‘o’ with ‘u’, remove suffix e, 
# starts with ‘C’

## "Snicker"  ##



print("please enter your string")
string = input()
print(string.strip("r").upper().removeprefix("SN")[0:]) #Sniker-> Snike ->SNIKE -> IKE


##    "Cookie"   ##

print("please enter your string")
string = input()
print(string.lower())
print(string.replace("o", "u"))
print(string.removesuffix("e"))
print(string.startswith("C"))

# print(string.lower().replace("0", "u").removesuffix("e").startswith("c"))


# Yusuf solution 

s1 = "Snicker"
print(s1.strip().upper().removeprefix("S")[2:5])

s2 = "Cookie"
print(s2.lower().replace("o","u").removesuffix("e").startswith("C"))