# Aula 02 - Métodos da classe list

lista = [1, "Python", [40, 30, 20]]

# O método copy() retorna uma cópia da lista
l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]
print(l2) # [1, "Python", [40, 30, 20]]

print(id(lista), id(l2)) # Mesmos elementos, mas endereços diferentes
