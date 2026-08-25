def verificar_par(num):
    return num % 2 == 0


for n in range(1, 101):
    if verificar_par(n):
        print(n)
