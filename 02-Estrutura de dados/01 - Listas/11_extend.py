# Aula 02 - Métodos da classe list

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

# O método extend() adiciona uma lista ao final de outra lista
# Caso um elemento já exista na lista, ele será adicionado novamente
linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
