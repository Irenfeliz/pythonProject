text = input()
count = 0
while text not in ('стоп', 'хватит', 'достаточно'):
    text = input()
    count += 1

print(count)
