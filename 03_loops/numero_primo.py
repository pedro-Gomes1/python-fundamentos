n = int(input('Digite um número: '))
primo = True

lista = []

if n < 2:
    print(f'O número {n} não é primo')

else:
    for divisor in range(2, n):
        if n % divisor == 0:
            lista.append(divisor)
            primo = False

    if primo:
        print(f'O número {n} é primo')
    else:
        print(f'O número {n} não é primo')
        print('É divisível por 1')

        for divisor in lista:
            print(f'É divisível por {divisor}')

        print(f'E é divisível por {n}')
