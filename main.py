# s = input()

# print(s.count(' ') + 1)

# s = s.lower()
#
# print('Аденин:', s.count('а'))
# print('Гуанин:', s.count('г'))
# print('Цитозин:', s.count('ц'))
# print('Тимин:', s.count('т'))

# n = int(input())
# count = 0
#
# for i in range(n):
#     s = input()
#     if s.count('11') >= 3:
#         count += 1
#
# print(count)

# s = input()
# count = 0
#
# for i in range(len(s)):
#     if s[i] in '0123456789':
#         count += 1
#
# print(count)

# s = input()
#
# print('YES' if s.endswith('.com') or s.endswith('.ru') else 'NO')

# s = input()
# count = 0
#
# for i in range(len(s)):
#     k = s.count(s[i])
#     if k >= count:
#         count = k
#         symbol = s[i]
# print(symbol)

# s = input()
#
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') > 1:
#     print(s.find('f'), s.rfind('f'))
# else:
#     print('NO')

s = input()
print(s[:s.find('h')] + s[s.rfind('h') + 1:])
