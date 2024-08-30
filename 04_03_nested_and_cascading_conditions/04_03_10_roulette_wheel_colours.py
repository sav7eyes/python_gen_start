num = int(input())

if num < 0 or num > 36:
    print('ошибка ввода')
elif num == 0:
    print('зеленый')
elif num in range(1, 11) and num % 2 != 0:
    print('красный')
elif num in range(1, 11) and num % 2 == 0:
    print('черный')
elif num in range(11, 19) and num % 2 != 0:
    print('черный')
elif num in range(11, 19) and num % 2 == 0:
    print('красный')
elif num in range(19, 29) and num % 2 != 0:
    print('красный')
elif num in range(19, 29) and num % 2 == 0:
    print('черный')
elif num in range(29, 37) and num % 2 != 0:
    print('черный')
elif num in range(29, 37) and num % 2 == 0:
    print('красный')