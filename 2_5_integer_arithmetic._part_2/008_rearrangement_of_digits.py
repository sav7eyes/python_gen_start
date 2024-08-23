three_digit_int = abs(int(input()))

digit_c = three_digit_int % 10
digit_b = three_digit_int // 10 % 10
digit_a = three_digit_int // 100

print(digit_a, digit_b, digit_c, sep='')
print(digit_a, digit_c, digit_b, sep='')
print(digit_b, digit_a, digit_c, sep='')
print(digit_b, digit_c, digit_a, sep='')
print(digit_c, digit_a, digit_b, sep='')
print(digit_c, digit_b, digit_a, sep='')