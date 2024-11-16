# Exemplo de dicionário
meu_dicionario = {
    "nome": "Christian",
    "idade": 19,
    "cidade": "Resende",
    "profissão": "Estudante"
}

# Exibe as opções para o usuário
print("Escolha um item do dicionário:")
for chave in meu_dicionario:
    print(f"{chave}: {meu_dicionario[chave]}")

# Pede ao usuário para escolher uma chave
escolha_usuario = input("Digite a chave desejada: ")

# Verifica se a chave está no dicionário e exibe o valor correspondente
if escolha_usuario in meu_dicionario:
    print(f"Você escolheu {escolha_usuario}: {meu_dicionario[escolha_usuario]}")
else:
    print("Chave não encontrada no dicionário.")
