a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

sum1 = 0 # сумма четных
sum2 = 0 # сумма нечетных
sum3 = 0 # сумма кратных 9

c1 = 0 # кол-во четных
c2 = 0 # кол-во нечетных
c3 = 0 # кол-во кратных 9

for i in range(a, b):
    if i % 2 == 0:
        c1 += 1
        sum1 += i
    else:
        c2 += 1
        sum2 += i

    if i % 9 == 0:
        c3 += 1
        sum3 += i

print(sum1, sum1 / c1)


