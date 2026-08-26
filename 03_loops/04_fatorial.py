n = int(input('Qual número deseja calcular o fatorial? '))

resultado = 1

for num in range(1, n + 1):
    resultado *= num

print(f'O fatorial de {n} é {resultado}')
