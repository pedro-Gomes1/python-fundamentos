votos = []

while True:

```
voto = input('Digite seu voto (1 para candidato 1, 2 para candidato 2, 3 para candidato 3, n para encerrar): ')

if voto == 'n':
    break

votos.append(voto)
```

resultados = {
'candidato 1': 0,
'candidato 2': 0,
'candidato 3': 0
}

for voto in votos:

```
if voto == '1':
    resultados['candidato 1'] += 1

elif voto == '2':
    resultados['candidato 2'] += 1

elif voto == '3':
    resultados['candidato 3'] += 1
```

print('Resultado da eleição:')

for candidato, quantidade in resultados.items():
print(f'{candidato}: {quantidade} votos')
