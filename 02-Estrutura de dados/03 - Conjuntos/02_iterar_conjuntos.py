# Aula 01: Conjuntos

carros = {"gol", "celta", "palio"}

# Podemos iterar sobre um conjunto utilizando um for
for carro in carros:
    print(carro)

# Podemos utilizar a função enumerate para obter o índice de cada elemento
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
