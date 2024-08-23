three_digit_number = abs(int(input()))
digit3 = three_digit_number % 10
digit2 = three_digit_number // 10 % 10
digit1 = three_digit_number // 100
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)