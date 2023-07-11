# Aula 01: Conjuntos

# Conjuntos são estruturas de dados que não possuem valores duplicados
# Podemos utilizar conjuntos para remover valores duplicados de uma lista
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

# Set não mantem a ordem dos elementos
letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens)  # {"python", "java"}
