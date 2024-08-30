num = int(input())

num1 = num // 10 **2
num2 = num // 10 % 10
num3 = num % 10
num_med = (num1 + num2 + num3) - max(num1, num2, num3) - min(num1, num2, num3)

if (max(num1, num2, num3) - min(num1, num2, num3)) == num_med:
    print(f'Число интересное')
else:
    print(f'Число неинтересное')