notas = []
soma = 0

while True:
    n = float(input('Digite sua nota: '))
    notas.append(n)

    acao = input('Deseja continuar? (s/n): ').lower()

    if acao == 'n':
        break

for num in notas:
    soma += num

qtd = len(notas)
media = soma / qtd

print(f'A média é {media:.2f}')
