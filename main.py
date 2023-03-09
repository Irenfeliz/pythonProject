s = input()
glas = 0
soglas = 0

for i in range(len(s)):
    if s[i].lower() in 'ауоыиэяюёе':
        glas += 1
    elif s[i].lower() in 'бвгджзйклмнпрстфхцчшщ':
        soglas += 1

print('Количество гласных букв равно', glas)
print('Количество согласных букв равно', soglas)
