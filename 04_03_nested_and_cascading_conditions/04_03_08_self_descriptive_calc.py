num1, num2, oper = int(input()), int(input()), input()

if oper == '+':
    print(num1 + num2)
elif oper == '-':
    print(num1 - num2)
elif oper == '*':
    print(num1 * num2)
elif oper == '/' and num2 != 0:
    print(num1 / num2)
elif oper == '/' and num2 == 0:
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')