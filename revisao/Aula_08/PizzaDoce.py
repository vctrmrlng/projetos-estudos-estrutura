# Classe Filha - subclass()
from PizzaPadrao import PizzaPadrao
class PizzaDoce(PizzaPadrao):
    def __init__ (self, sabor, tamanho, preco, ingredientes, borda_recheada):
        super().__init__(sabor, tamanho, preco, ingredientes)
        self.borda_recheada = borda_recheada

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f'''
        Borda recheada: {self.borda_recheada}
        ''')

#Criando objetos

pizza_comum = PizzaPadrao('Calabresa' , 'Família' , 29.90 , 'Tomate, cebola')
pizza_chocolate = PizzaDoce ('Chocolate com Morango' , 'Pequena' , 31.90 , 'Chocolate, Morango' ,  "Chocolate")

print(f" --- Pizza Comum ---")
pizza_comum.mostrar_detalhes()
print(f" --- Pizza Doce ---")
pizza_chocolate.mostrar_detalhes()