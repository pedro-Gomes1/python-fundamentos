lista = []

for n in range(5):
    num = float(input(f'Digite o {n + 1}º número: '))
    lista.append(num)

soma = sum(lista)
media = soma / len(lista)

print(f'\nNúmeros digitados: {lista}')
print(f'Soma: {soma}')
print(f'Média: {media}')
