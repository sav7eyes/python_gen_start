from math import sqrt, pow

a, b, c = float(input()), float(input()), float(input())
x1 = (- b - sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
x2 = (- b + sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
if a == 0:
    print('Нет корней')
else:
    print(min(x1, x2))
    print(max(x1, x2))