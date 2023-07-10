# Aula 02 - Métodos da classe list

linguagens = ["python", "js", "c", "java", "csharp"]

# O método sorted() retorna uma lista ordenada com base na lista passada como argumento
# A diferença entre o sort(), é que o sorted() é uma função, e o sort() é um método da classe list
# O sorted() não altera a lista original
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
