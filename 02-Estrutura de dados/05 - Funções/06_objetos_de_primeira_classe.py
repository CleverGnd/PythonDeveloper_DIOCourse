# Aula 2 - Funções em Python- Parte 2

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

# Ao passar a função somar como parâmetro, ela funciona normalmente, e já identifica os parâmetros a e b
# A função somar tem o comportamento de um objeto, e pode ser passada como parâmetro para outra função
exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
