len_ab, len_bc, len_ac = int(input()), int(input()), int(input())

if len_ab == len_bc == len_ac:
    print('Равносторонний')
elif len_ab == len_bc or len_bc == len_ac or len_ab == len_ac:
    print('Равнобедренный')
else:
    print('Разносторонний')