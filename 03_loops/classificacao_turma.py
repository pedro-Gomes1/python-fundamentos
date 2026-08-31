idades = []

while True:
    idade = int(input('Digite sua idade: '))
    idades.append(idade)

    acao = input('Deseja continuar? (s/n): ').lower()

    if acao == 'n':
        break

soma = 0

for idade in idades:
    soma += idade

qtd = len(idades)
media = soma / qtd

if media <= 25:
    print(f'A turma é jovem. A média é {media:.1f}')
elif media <= 60:
    print(f'A turma é adulta. A média é {media:.1f}')
else:
    print(f'A turma é idosa. A média é {media:.1f}')
