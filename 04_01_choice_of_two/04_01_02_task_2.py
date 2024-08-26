num = int(input())

first_digit = num // 10
second_digit = num % 10

if first_digit == second_digit:
    print('ДА')
else:
    print('НЕТ')