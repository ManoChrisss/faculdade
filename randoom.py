import random

print("------------------------------------------------------------------------------")
print('Olá, seja bem-vindo ao jogo de adivinhar! Caso um acerte, escolherá algo para o outro fazer. Caso os dois acertem, ambos poderão escolher algo. Vamos começar?')
print("------------------------------------------------------------------------------")
nome1 = input("Digite seu nome, usuário1: ")
nome2 = input("Digite seu nome, usuário2: ")

num_aleatorio = input(f"{nome1}, Digite um número: ")
num_aleatorio2 = input(f"{nome2}, Digite um número: ")
sorteio = int(num_aleatorio)
sorteio2 = int(num_aleatorio2)

if sorteio and sorteio2 == random.randint(1, 10):
    print(f"Parabéns, {nome1} e {nome2} acertaram")
elif sorteio == random.randint(1, 10):
    print(f"Parabéns,{nome1} acertou!")
elif sorteio == random.randint(1, 10):
    print(f"Parabéns,{nome2} acertou!")
else:
    print("Ninguém acertou, que pena!")
      


