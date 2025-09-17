class Pizza :
    #Atributos da Classe (construtor padrão)
    def __init__ (self, sabor, tamanho, preco):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco

    # Método nosso criado para descrever
    def descricao (self):
        return f"Pizza de {self.sabor}, Tamanho: {self.tamanho}, Preço: R$ {self.preco:.2f}"

# Criando objetos da classe Pizza

pizza001 = Pizza("Calabresa" , "Familia" , 52.99)
pizza002 = Pizza("Mussarela" , "Média", 49.99)
pizza003 = Pizza("Portuguesa" , "Pequena", 29.99)

print(pizza001.descricao())
print(pizza002.descricao())
print(pizza003.descricao())