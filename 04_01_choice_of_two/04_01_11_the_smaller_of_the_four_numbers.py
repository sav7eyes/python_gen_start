num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num1_2 = 0
num3_4 = 0

if num1 < num2:
    num1_2 = num1
else:
    num1_2 = num2
if num3 < num4:
    num3_4 = num3
else:
    num3_4 = num4
if num1_2 < num3_4:
    print(num1_2)
else:
    print(num3_4)