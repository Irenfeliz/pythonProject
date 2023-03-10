s = input()
count1 = 0
count2 = 0

for i in range(len(s)):
    if s[i] in '+':
        count1 += 1
    elif s[i] in '*':
        count2 += 1

print('Символ + встречается', count1, 'раз')
print('Символ * встречается', count2, 'раз')
