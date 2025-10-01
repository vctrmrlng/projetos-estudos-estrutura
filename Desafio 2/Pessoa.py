# --- Professor ---
# Nome: Carlos, Idade: 40
# ...
# Disciplina: Matemática

# --- Aluno ---
# Nome: Maria, Idade: 16
# ...
# Matrícula: 2025A01

# --- Funcionário ---
# Nome: João, Idade: 35
# ...
# Cargo: Bibliotecário

class Pessoa:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def mostrar_detalhes(self):
        print(f'Nome: {self.nome}, Idade: {self.idade} ')