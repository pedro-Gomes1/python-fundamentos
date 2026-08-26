a = 1
b = 1

n = int(input('Quantos termos? '))

if n == 1:
    print(a)

elif n == 2:
    print(a)
    print(b)

else:
    print(a)
    print(b)

    for num in range(2, n):
        proximo = a + b
        a = b
        b = proximo

        print(proximo)
