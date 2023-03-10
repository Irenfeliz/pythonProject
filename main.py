# s = 'In {0}, someone paid {1} {2} for two pizzas.'
#
# print(s.format(2010, '10k', 'Bitcoin'))
#
# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
#
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')
#
#

# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

s = input()

for i in range(len(s)):
    print(ord(s[i]), end=' ')