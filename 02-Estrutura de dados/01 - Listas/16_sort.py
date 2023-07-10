# Aula 02 - Métodos da classe list

linguagens = ["python", "js", "c", "java", "csharp"]

# O método sort() ordena os elementos da lista
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

# Usando o argumento reverse=True, a lista é ordenada de forma decrescente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# O método sort() também aceita uma função como argumento, que será usada para ordenar a lista
# Neste exemplo, a lista é ordenada com base no tamanho de cada elemento
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

# Neste exemplo, a lista é ordenada com base no tamanho de cada elemento, de forma decrescente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
