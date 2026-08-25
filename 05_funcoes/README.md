# Funções em Python

Exercícios e exemplos práticos sobre criação e utilização de funções em Python.

## 📚 Conteúdos estudados

- Criação de funções com `def`
- Parâmetros e argumentos
- `return`
- Funções sem retorno
- Funções com múltiplos parâmetros
- Funções com condições
- Funções utilizadas dentro de estruturas de repetição
- Reutilização de código
- Organização e modularização do programa

## 📂 Exercícios

| Arquivo | Conceito |
|---|---|
| `01_funcao_impar.py` | Criação de uma função para verificar se um número é ímpar |
| `02_funcao_par.py` | Função para verificar se um número é par |
| `03_soma.py` | Função para realizar uma soma |
| `04_media.py` | Função para calcular uma média |
| `05_maior_numero.py` | Função para encontrar o maior número |
| `06_crescimento_populacional.py` | Função aplicada a um problema de crescimento populacional |

## 🎯 Objetivo

Praticar a criação de funções para tornar os programas mais organizados, reutilizáveis e fáceis de manter.

## 🧠 Exemplo

```python
def verificar_impar(num):
    return num % 2 != 0

for n in range(1, 51):
    if verificar_impar(n):
        print(n)
