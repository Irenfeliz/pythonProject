n = int(input())
digit = ''

while n > 0:
    digit = str(n % 2) + digit
    n //= 2
print(digit)

# for i in range(len(digit) - 1, -1, -1):
#     print(digit[i], end='')
