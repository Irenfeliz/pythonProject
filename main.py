# s = input()
# newS = ''
#
# for i in range(len(s)):
#     if i % 3 == 0:
#         newS += ''
#     else:
#         newS += s[i]
# print(newS, end='')
#

# s = input()
# print(s.replace('@', ''))

# s = input()
# count = 0
#
# for i in range(len(s)):
#     if s[i] == 'f':
#         count += 1
#         if count == 2:
#             print(i)
#             break
#
# if count == 1:
#     print('-1')
# elif count == 0:
#     print('-2')

# супер вариант решения
# s = input()
# if 'f' not in s:
#     print(-2)
# else:
#     print(s.replace('f', '0', 1).find('f'))

# s = input()
# h1 = s.find('h')
# h2 = s.rfind('h')
# snew = ''
# s1 = s[h1 + 1:h2]
#
# for i in range(len(s1) - 1, -1, -1):
#     snew += s1[i]
#
# print(s[:h1 + 1] + snew + s[h2:])

# лучшее решение здесь:
s = input()
a = int(s.find('h'))
b = int(s.rfind('h'))
print(s[:a] + s[b:a:-1] + s[b:])
