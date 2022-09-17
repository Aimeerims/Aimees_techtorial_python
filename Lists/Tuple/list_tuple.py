# If you need update the list use this solution

t = (1,2,3,4,5,6)
print(type(t))
# From this tuple remove each number if square of the number is 
# smaller then 20

# Convert the tuple in to a list

t = list(t)

# I can make a copy of t
l = t.copy()
for number in l:
    if number ** 2 < 20:
        t.remove(number)

t = tuple(t)

print(t)
print(type(t))