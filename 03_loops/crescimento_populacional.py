def calc_crescimento(pais, taxa):
    cresc = (pais * taxa) / 100
    return cresc


while True:

    pais_a = int(input('Qual a população do país A? '))
    while pais_a <= 0:
        print('A população deve ser maior que zero.')
        pais_a = int(input('Qual a população do país A? '))

    pais_b = int(input('Qual a população do país B? '))
    while pais_b <= 0:
        print('A população deve ser maior que zero.')
        pais_b = int(input('Qual a população do país B? '))

    taxa_a = float(input('Qual a taxa de crescimento do país A? '))
    while taxa_a <= 0:
        print('A taxa de crescimento deve ser maior que zero.')
        taxa_a = float(input('Qual a taxa de crescimento do país A? '))

    taxa_b = float(input('Qual a taxa de crescimento do país B? '))
    while taxa_b <= 0:
        print('A taxa de crescimento deve ser maior que zero.')
        taxa_b = float(input('Qual a taxa de crescimento do país B? '))

    total_a = pais_a
    total_b = pais_b
    ano = 0

    while total_a < total_b:

        total_a += calc_crescimento(total_a, taxa_a)
        total_b += calc_crescimento(total_b, taxa_b)

        ano += 1

    print(f'País A será maior que o país B em {ano} anos.')

    opcao = input('Deseja continuar? [s/n] ').lower()

    if opcao == 'n':
        print('Programa encerrado.')
        break
