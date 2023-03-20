# import math
#
# n = int(input())
# print(math.ceil(math.log(n, 2)))

import random


def is_valid(s):
    if s.isdigit():
        return True
    else:
        return False


def game():
    print('Добро пожаловать в числовую угадайку')
    print('Угадываем число от 1 до ...?')
    num = int(input())
    r = random.randint(1, num)
    print('Введите число от 1 до', num)
    s = input()
    flag = False
    count = 0
    while flag == False:
        count += 1
        while not is_valid(s):
            print('А может быть все-таки введем целое число от 1 до', num, '?')
            s = input()
        n = int(s)
        if n < r:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            s = input()
        if n > r:
            print('Ваше число больше загаданного, попробуйте еще разок')
            s = input()
        if n == r:
            print('Вы угадали, поздравляем!')
            print('Вы отгадали с ', count, 'попыток!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            flag = True


game()
