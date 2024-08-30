col1, str1 = int(input()), int(input())
col2, str2 = int(input()), int(input())

if (str1 - str2 == 1 or str1 - str2 == -1) and (col1 - col2 == -2 or col1 - col2 == 2):
    print('YES')
elif (str1 - str2 == 2 or str1 - str2 == -2) and (col1 - col2 == -1 or col1 - col2 == 1):
    print('YES')
else:
    print('NO')