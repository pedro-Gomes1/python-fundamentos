lista = []
lista_par = []
lista_impar = []


def verificar_par(numero):
    return numero % 2 == 0


for n in range(1, 11):
    num = int(input('Digite um número: '))
    lista.append(num)

    if verificar_par(num):
        lista_par.append(num)
    else:
        lista_impar.append(num)


print(f'Números pares: {len(lista_par)}')
print(f'Números ímpares: {len(lista_impar)}')
