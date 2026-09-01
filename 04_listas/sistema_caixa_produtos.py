produtos = []

while True:
    preco = float(input('Digite o preço do produto (ou "0" para encerrar): '))

    if preco == 0:
        break

    if preco < 0:
        print('Preço inválido.')
        continue

    produtos.append(preco)


print('\nProdutos:')

for i, preco in enumerate(produtos, start=1):
    print(f'{i}. R${preco:.2f}')


total = sum(produtos)

print(f'\nTotal: R${total:.2f}')


pagamento = float(input('Digite o valor pago: R$'))

troco = pagamento - total

if troco < 0:
    print('Valor pago insuficiente.')
else:
    print('Pagamento realizado com sucesso.')

    if troco > 0:
        print(f'Troco: R${troco:.2f}')
