col1, str1 = int(input()), int(input())
col2, str2 = int(input()), int(input())

if col1 == col2 or str1 == str2:
    print('YES')
elif col1 + str1 == col2 + str2 or col1 - str1 == col2 - str2:
    print('YES')
else:
    print('NO')