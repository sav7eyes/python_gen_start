num1, num2, num3  = int(input()), int(input()), int(input())

# if num1 == num2:
#     if num2 == num3:
#         print(3)
#     else:
#         print(2)
# else:
#     if num1 == num3:
#         print(2)
#     else:
#         if num2 == num3:
#             print(2)
#         else:
#             print(0)

if num1 == num2 == num3:
    print(3)
elif num1 == num2 or num1 == num3 or num2 == num3:
    print(2)
else:
    print(0)