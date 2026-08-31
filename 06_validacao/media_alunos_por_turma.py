qtd_turmas = int(input('Digite a quantidade de turmas: '))

lista_alunos = []

while qtd_turmas <= 0:
    print('Quantidade de turmas inválida.')
    qtd_turmas = int(input('Digite a quantidade de turmas: '))

for n in range(qtd_turmas):
    alunos = int(input('Digite a quantidade de alunos: '))

    while alunos <= 0 or alunos > 40:
        print('Quantidade de alunos inválida.')
        alunos = int(input('Digite a quantidade de alunos: '))

    lista_alunos.append(alunos)

media_turma = sum(lista_alunos) / len(lista_alunos)

print(f'A média de alunos por turma é: {media_turma:.2f}')
