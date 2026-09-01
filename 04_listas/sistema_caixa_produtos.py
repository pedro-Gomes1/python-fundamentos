produtos = []

while True:

    produtos = []

    print('\n--- NOVA COMPRA ---')

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

    while True:
        pagamento = float(input('Digite o valor pago: R$'))

        troco = pagamento - total

        if troco < 0:
            print('Valor pago insuficiente.')
            print(f'Faltam: R${abs(troco):.2f}')
        else:
            print('Pagamento realizado com sucesso.')

            if troco > 0:
                print(f'Troco: R${troco:.2f}')

            break

    print('\nCompra finalizada!')

    while True:
        resposta = input('Deseja realizar uma nova compra? (s/n): ').lower()

        if resposta == 's':
            break

        if resposta == 'n':
            print('Caixa encerrado.')
            break

        print('Opção inválida. Digite "s" ou "n".')

    if resposta == 'n':
        break
