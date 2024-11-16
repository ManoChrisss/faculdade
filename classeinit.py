# Definindo a classe 'Carro'
class Carro:
    # O método __init__ é o construtor da classe
    def __init__(self, marca, modelo, ano):
        # Inicializa os atributos da instância com os valores fornecidos
        self.marca = marca  # Atributo 'marca' do carro
        self.modelo = modelo  # Atributo 'modelo' do carro
        self.ano = ano  # Atributo 'ano' do carro

    # Método para exibir informações sobre o carro
    def detalhes(self):
        # Retorna uma string com os detalhes do carro
        return f"{self.marca} {self.modelo}, ano {self.ano}"

    # Método para atualizar o ano do carro
    def atualizar_ano(self, novo_ano):
        self.ano = novo_ano  # Atualiza o atributo 'ano' com o novo valor

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022)

# Exibindo os detalhes do carro
print(meu_carro.detalhes())  # Saída: Toyota Corolla, ano 2022

# Atualizando o ano do carro
meu_carro.atualizar_ano(2023)

# Exibindo os detalhes atualizados do carro
print(meu_carro.detalhes())  # Saída: Toyota Corolla, ano 2023

# Criando outra instância da classe Carro
outro_carro = Carro("Honda", "Civic", 2020)

# Exibindo os detalhes do outro carro
print(outro_carro.detalhes())  # Saída: Honda Civic, ano 2020
