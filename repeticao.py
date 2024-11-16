# 1. Pedir ao usuário o número de notas
num_notas = int(input("Quantas notas você vai inserir? "))

# Inicializando a soma das notas como 0
soma_notas = 0

# 2. Repetir o pedido de nota num_notas vezes
for i in range(num_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma_notas += nota  # Adiciona a nota à soma total

# 4. Calcular a média
media = soma_notas / num_notas

# 5. Mostrar o resultado
print(f"A média das notas é: {media:.2f}")