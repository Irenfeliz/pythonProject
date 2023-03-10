import math

s = input()
l = len(s)
# Qwe-rty
# Hel-lo
middle = math.ceil(len(s) / 2)
a = s[:middle]
b = s[middle:]
print(b + a)
