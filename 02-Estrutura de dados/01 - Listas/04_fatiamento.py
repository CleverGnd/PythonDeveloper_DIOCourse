# Aula 01 - Listas:Criação e acesso aos elementos

lista = ["p", "y", "t", "h", "o", "n"]

# Essa sintaxe é chamada de fatiamento, e permite que você retorne somente uma parte da lista
print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
