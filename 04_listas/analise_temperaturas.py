temperaturas = []

while True:
    temp = float(input('Digite a temperatura (ou "0" para encerrar): '))

    if temp == 0:
        break

    temperaturas.append(temp)

if temperaturas:
    print(f'\nTemperaturas: {temperaturas}')
    print(f'Média: {sum(temperaturas) / len(temperaturas):.2f}')
    print(f'Maior temperatura: {max(temperaturas):.2f}')
    print(f'Menor temperatura: {min(temperaturas):.2f}')
else:
    print('\nNenhuma temperatura foi informada.')
