num = int(input())

digit1 = num % 10**3 // 10**2
digit2 = num % 10**2 // 10
digit3 = num % 10

if digit1 != digit2 != digit3:
    print('Цифры различны')
else:
    print('Цифры не различны')