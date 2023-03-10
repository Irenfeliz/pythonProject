n = int(input())
s = input()

for i in range(len(s)):
    newOrder = ord(s[i]) - n
    if newOrder < 97:
        newOrder = 26 + newOrder
    print(chr(newOrder), end='')
