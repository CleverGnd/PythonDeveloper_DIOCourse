# Aula 01: Conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Podemos obter a diferença simétrica entre dois conjuntos utilizando o método symmetric_difference
# Elementos que não estão na intersecção
resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)
