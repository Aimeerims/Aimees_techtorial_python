c = 4 + 2j  # j means root of -1 j - represent of imaginary number
# 4 devide 2
# devide imaniginary parts 2 devide 
# 2 + 1j
c = c / 2 
print(c)

c = c - 10    #if you have real number for ex: 10 you will substruct from 2 -10=-8 
print(c)      # here you dont need imaginari number, you substruct from real part
              # result is -8+1j   1j just stay
              # real parts changing -8+10=2

d = 10 + 5j   # -8 -10 

e = c + d     # imaginary parts 1j+5j    result= (2+6j)
print(e)

# learning Imaginary part and real part of the number
# following line will give you real part of the number
print(e.real)
# following line will give you the imaginary part of the number
print(e.imag)

