start_col, start_str = int(input()), int(input())
finish_col, finish_str = int(input()), int(input())

if (-1 <= finish_col - start_col <= 1) and (-1 <= finish_str - start_str <= 1):
    print('YES')
else:
    print('NO')