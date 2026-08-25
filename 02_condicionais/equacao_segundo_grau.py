import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

if a == 0:
    print('O valor de a deve ser diferente de zero.')

else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print('A equação não possui raízes reais.')

    elif delta == 0:
        x = -b / (2 * a)
        print(f'A equação possui uma raiz real: {x}')

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
