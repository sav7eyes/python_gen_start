num_a1, num_b1 = int(input()), int(input())
num_a2, num_b2 = int(input()), int(input())

if num_b1 < num_a2 or num_b2 < num_a1:
    print(f'пустое множество')
elif num_b1 == num_a2:
    print(num_b1)
elif num_b2 == num_a1:
    print(num_b2)
elif num_a2 > num_a1 and num_b1 < num_b2:
    print(num_a2, num_b1)
elif num_a2 < num_a1 and num_b1 > num_b2:
    print(num_a1, num_b2)
elif num_a1 >= num_a2 and num_b2 >= num_b1:
    print(num_a1, num_b1)
elif num_a1 <= num_a2 and num_b2 <= num_b1:
    print(num_a2, num_b2)