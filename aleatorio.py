import random

# Exemplo de dicionário
meu_dicionario = {
    "nome": "Christian",
    "idade": 19,
    "cidade": "Resende",
    "profissão": "Estudante"
}

# Escolhe uma chave aleatória do dicionário
chave_aleatoria = random.choice(list(meu_dicionario))

# Obtém o valor correspondente a essa chave
item_aleatorio = (chave_aleatoria, meu_dicionario[chave_aleatoria])

print(f"Chave: {item_aleatorio[0]}, Valor: {item_aleatorio[1]}")
