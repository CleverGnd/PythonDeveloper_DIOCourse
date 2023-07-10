# Aula 01 - Listas:Criação e acesso aos elementos

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]

# Usando o list comprehension. Para cada numero na lista números, se o numero for par, adicione na lista pares
# [Elemento for integrável in lista if condição]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
