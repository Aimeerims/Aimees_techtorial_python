# prefix -> will remove from the beginning of the string
# suffix -> will remove it from the end of the string

s = "Hello Python"
# If you want to remove Python from this string you can use remove suffix method

print(s.removesuffix("Python"))

print(s.removeprefix("Hello"))
# this method is case sensative

# From the given website string
# print only the domain name of the website



website = input()
domain_name = website.removeprefix("www.").removesuffix(".com")
print(domain_name)

str = "hello world"
print(str.removeprefix("el"))

str2 = "Encapsulation isx good for data hiding"
print(str2.removesuffix("idin")) 
print(str2.strip("gni")) #hid


str2 ="Encapsulation is good for data hiding"
print("Result of the suffix",str2.removesuffix("gni"))
print("Result of strip",str2.strip("gni"))
#  "Encapsulation is good for data hiding"
#  "Encapsulation is good for data hid"
#  "Encapsulation is good for data hidi"