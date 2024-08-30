num1, num2, num3  = int(input()), int(input()), int(input())

if num1 < num2 < num3 or num3 < num2 < num1:
    print(num2)
elif num1 < num3 < num2 or num2 < num3 < num1:
    print(num3)
else:
    print(num1)