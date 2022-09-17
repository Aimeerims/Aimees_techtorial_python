
# Lets ask user a one string and remove the spaces in the begining 
# and end of the string

print("Enter a text")
#s = input()

# s = s.strip()
# print(s)


# s = "        Python is a programming language"
# print(s)
# print(s.strip())


# In strip method we can provide a charachter and it will remove the certain charachter 
# if that charachter is in the begining or end of the the string

# Lets write phone number in the middle of the number tags
phone_number = "###7773332222##"
print(phone_number.strip("#"))


# strip method can also work with multiple charachter
# we can specify charachter instead of removing the default space

web_site = "www.techtorial.com"
# get the domain name from this website
# .wcom
print("Domain name of the website is", web_site.strip(".wcom"))

# Given a gmail address from user, print only the users mail name
# For ex: example@gmail.com -> exapmle
#                      yct@gmail.com _ yct

# version
# gmail = "example@gmail.com"
# print(gmail.strip("@gmail.com"))

print("please enter your gmail")
gmail = input()
gmail_name = gmail.strip("@gmail.co")
print(gmail_name)

# rstrip method which allows us to just remove trailing part of the string
# gmailyusuf@gmail.com

gmail_name1 = gmail.rstrip("gmail.co")
print(gmail_name1)

# lstrip method which allows us to just remove leading part of the string
# yusufm@gmail.com   with 2m 
# we can use replase method 

# From the given website below, print only domain name and .com
web_site = "www.techtorial.com"
print(web_site.lstrip("www."))

# in the strip method we can easily mistaken, so 
# we have to make sure and double check which parts it is going to remove

