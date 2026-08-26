a = 1
b = 1

print(a)
print(b)

while True:
    proximo = a + b

    if proximo >= 500:
        break

    print(proximo)

    a = b
    b = proximo
