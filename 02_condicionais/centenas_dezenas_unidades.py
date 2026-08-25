n = int(input('Digite um número inteiro menor que 1000: '))

c = n // 100
d = (n % 100) // 10
u = n % 10

partes = []

if c > 0:
    if c == 1:
        partes.append('1 centena')
    else:
        partes.append(f'{c} centenas')

if d > 0:
    if d == 1:
        partes.append('1 dezena')
    else:
        partes.append(f'{d} dezenas')

if u > 0:
    if u == 1:
        partes.append('1 unidade')
    else:
        partes.append(f'{u} unidades')

if len(partes) == 1:
    print(partes[0])

elif len(partes) == 2:
    print(f'{partes[0]} e {partes[1]}')

else:
    print(f'{partes[0]}, {partes[1]} e {partes[2]}')
