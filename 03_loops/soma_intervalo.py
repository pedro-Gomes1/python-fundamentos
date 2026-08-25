lista = []

for a in range(2):
    num = int(input('digite um numero'))
    lista.append(num)

soma = 0

for n in range(lista[0], lista[1]):
    soma += n

print(soma)
