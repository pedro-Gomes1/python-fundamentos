dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if mes < 1 or mes > 12:
    print('Data inválida.')

else:
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        dias_por_mes[1] = 29

    if 1 <= dia <= dias_por_mes[mes - 1]:
        print('Data válida.')
    else:
        print('Data inválida.')
