lista_cds = []
lista_precos = []

while True:
    cd = int(input('Digite a quantidade de CDs: '))

    while cd <= 0:
        print('Quantidade de CDs inválida.')
        cd = int(input('Digite a quantidade de CDs: '))

    lista_cds.append(cd)

    preco = float(input('Digite o preço do CD: '))

    while preco <= 0:
        print('Preço inválido.')
        preco = float(input('Digite o preço do CD: '))

    lista_precos.append(preco)

    continuar = input('Deseja adicionar mais? (s/n): ').lower()

    if continuar != 's':
        break

total_cds = sum(lista_cds)

total_gasto = sum(
    cd * preco
    for cd, preco in zip(lista_cds, lista_precos)
)

print(f'Total de CDs: {total_cds}')
print(f'Total gasto: R$ {total_gasto:.2f}')
