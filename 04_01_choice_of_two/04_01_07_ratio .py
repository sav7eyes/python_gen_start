num = int(input())

digit1 = num % 10000 // 1000
digit2 = num % 1000 // 100
digit3 = num % 100 // 10
digit4 = num % 10

if (digit1 + digit4) == (digit2 - digit3):
    print('ДА')
else:
    print('НЕТ')