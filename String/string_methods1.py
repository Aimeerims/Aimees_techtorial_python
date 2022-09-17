

s = "Python"
print(s.upper()) # ->PYTHON
print(s)         # ->python
# Since the string is immutable, it will not change its value unless it is reassigned.

s = "PYthon"
print(s.lower())

# Method chaining --> as long as the method you use in the string returns another string
# You can use other string  method

print(s.lower().upper()) # s will be printed in all upper case since it is the last method  # PYTHON
print(s.upper().lower()) # s will be printed in all lower case since it is last method # python

print("Result of swap case method", s.swapcase()) # pyTHON

print("Result of capitalize method", s.capitalize()) # Python

