# Aula 01 - Listas:Criação e acesso aos elementos

carros = ["gol", "celta", "palio"]

# Acessando todos os elementos da lista usando o for
for carro in carros:
    print(carro)

# Mesmo exemplo, mas usando o indice
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
