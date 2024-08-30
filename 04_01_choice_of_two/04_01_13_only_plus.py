num1 = int(input())
num2 = int(input())
num3 = int(input())
num1_p = 0
num2_p = 0
num3_p = 0

if num1 > 0:
    num1_p = num1
else:
    num1_p = 0
if num2 > 0:
    num2_p = num2
else:
    num2_p = 0
if num3 > 0:
    num3_p = num3
else:
    num3_p = 0
print(num1_p + num2_p + num3_p)