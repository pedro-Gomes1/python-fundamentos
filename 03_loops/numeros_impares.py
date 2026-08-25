def verificar_impar(num):
    return num % 2 != 0

for n in range(1, 51):
    if verificar_impar(n):
        print(n)
