L = []  # Inicializa uma lista vazia

while True:  # Inicia um loop infinito
    n = int(input('digite um numero: '))  # Solicita ao usuário um número
    if n == 0:  # Se o número digitado for 0
        break  # O loop é interrompido
    L.append(n)  # Adiciona o número digitado à lista L

x = 0  # Inicializa um contador
while x < len(L):  # Enquanto x for menor que o comprimento da lista L
    print(L[x])  # Imprime o elemento na posição x da lista
    x += 1  # Incrementa x em 1
