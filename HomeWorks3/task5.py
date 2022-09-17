# Using the input function ask the user to enter one string value and
# print only unique letters combined as String also without any space in
# the beginning and at the end.
# Example -1 : 
# Given Value: "i am happy"
# Output: i am hpy
# Example-2: 
# Given Value: " contribute"
# Output: contribue
# Example-3: 
# Given Value: " i want cup of coffee "
# Output: i want cup of e

# print("Enter one string value")

ss = input("Enter one string value: ").strip()
print(ss)
ss[0:1]
uniq = ""
index = 0
ssLen = len(ss)
print(ssLen)
while index < ssLen:
    if(not uniq.find(ss[index:index+1])):
        print("myna saga ", ss[index:index+1])
        uniq+=str(ss[index:index+1])
    index += 1    

print(uniq)