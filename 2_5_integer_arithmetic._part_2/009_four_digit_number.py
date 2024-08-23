four_digit_number = abs(int(input()))

digit4 = four_digit_number % 10
digit3 = four_digit_number % 100 // 10
digit2 = four_digit_number % 1000 // 100
digit1 = four_digit_number % 10000 // 1000

print('Цифра в позиции тысяч равна', digit1)
print('Цифра в позиции сотен равна', digit2)
print('Цифра в позиции десятков равна', digit3)
print('Цифра в позиции единиц равна', digit4)