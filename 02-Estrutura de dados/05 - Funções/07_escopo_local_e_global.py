# Aula 2 - Funções em Python- Parte 2

# Variável com escopo global
salario = 2000

def salario_bonus(bonus):
    # Chamando a variável global
    global salario
    salario += bonus
    return salario

slario_com_bonus = salario_bonus(500)

print(slario_com_bonus)  # 2500
