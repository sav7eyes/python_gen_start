num_a, num_b, num_c = int(input()), int(input()), int(input())

if (num_a + num_b) > num_c and (num_a + num_c) > num_b and(num_b + num_c) > num_a:
    print('YES')
else:
    print('NO')