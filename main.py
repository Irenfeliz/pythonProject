# найдите четыре положительных целых числа,
# сумма 5-х степеней которых равна 5-й степени другого положительного целого числа.
#
# Таким образом, найдите пять натуральных чисел a,b,c,d,e удовлетворяющих условию:
#
# a**5 + b**5 + c**5 + d**5 = e**5
# В ответе укажите сумму a+b+c+d+e.

for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                summ = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(summ ** 0.2)
                if summ == e ** 5:
                    print(a, b, c, d, e)
                    print(a + b + c + d + e)
                    break
