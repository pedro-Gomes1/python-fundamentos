print('Responda às perguntas com "s" ou "n".')

respostas = []

pergunta1 = input('Telefonou para a vítima? ').lower()
respostas.append(pergunta1)

pergunta2 = input('Esteve no local do crime? ').lower()
respostas.append(pergunta2)

pergunta3 = input('Mora perto da vítima? ').lower()
respostas.append(pergunta3)

pergunta4 = input('Devia dinheiro para a vítima? ').lower()
respostas.append(pergunta4)

pergunta5 = input('Já trabalhou com a vítima? ').lower()
respostas.append(pergunta5)

quantidade = respostas.count('s')

if quantidade == 5:
    print('Classificação: Assassino')

elif quantidade >= 3:
    print('Classificação: Cúmplice')

elif quantidade == 2:
    print('Classificação: Suspeito')

else:
    print('Classificação: Inocente')
