start_col, start_str = int(input()), int(input())
finish_col, finish_str = int(input()), int(input())

if finish_col == start_col or finish_str == start_str:
    print('YES')
else:
    print('NO')