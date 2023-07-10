# Aula 01: Tuplas

carros = (
    "gol",
    "celta",
    "palio",
)

# Iterando sobre uma tupla, usando um laço for
for carro in carros:
    print(carro)

# Iterando sobre uma tupla, usando a função enumerate()
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
