col1, str1 = int(input()), int(input())
col2, str2 = int(input()), int(input())

if (col1 + str1) % 2 == (col2 + str2) % 2:
    print('YES')
else:
    print('NO')