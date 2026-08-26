conjunto_numeros = []
soma = 0


def operacoes_valores(conjunto_numeros):
    maior_valor = max(conjunto_numeros)
    menor_valor = min(conjunto_numeros)

    return maior_valor, menor_valor


while True:
    n = int(input('Digite um numero: '))
    conjunto_numeros.append(n)

    acao = input('Deseja continuar? (s/n): ')

    if acao == 'n':
        break


for num in conjunto_numeros:
    soma += num


maior_valor, menor_valor = operacoes_valores(conjunto_numeros)

print(f'A soma é {soma}')
print(f'O maior valor é {maior_valor}')
print(f'O menor valor é {menor_valor}')
