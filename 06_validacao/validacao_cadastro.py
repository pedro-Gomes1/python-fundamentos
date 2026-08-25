nome = input('Qual o seu nome? ')

while len(nome) <= 3:
    print('Nome inválido. O nome deve possuir mais de 3 caracteres.')
    nome = input('Qual o seu nome? ')


idade = int(input('Qual sua idade? '))

while idade < 0 or idade > 150:
    print('Idade inválida. Digite uma idade entre 0 e 150.')
    idade = int(input('Qual sua idade? '))


salario = float(input('Qual o seu salário? '))

while salario <= 0:
    print('Salário inválido. O salário deve ser maior que zero.')
    salario = float(input('Qual o seu salário? '))


estado_civil = input(
    'Qual seu estado civil? (s - solteiro, c - casado, v - viúvo, d - divorciado): '
).lower()

while estado_civil not in ['s', 'c', 'v', 'd']:
    print('Estado civil inválido.')
    estado_civil = input(
        'Qual seu estado civil? (s - solteiro, c - casado, v - viúvo, d - divorciado): '
    ).lower()


print('\nCadastro realizado com sucesso!')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: R$ {salario:.2f}')
print(f'Estado civil: {estado_civil}')
