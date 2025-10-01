from PizzaPadrao import PizzaPadrao
from PizzaDoce import PizzaDoce
def main():
    pizza_portuguesa = PizzaPadrao('Portuguesa' , 'Grande' , 49.99 , 'Mussarela, Linguiça Calabresa, Cebola, Orégano e Molho de Tomate')
    pizza_marguerita = PizzaPadrao('Marguerita' , 'Pequeno' , 54.99 , 'Tomate, Manjericão, Mussarela, Orégano, Molho de Tomate')
    pizza_calabresa = PizzaPadrao('Calabresa' , 'Família' , 29.90 , 'Tomate, cebola')
    pizza_chocolate = PizzaDoce ('Chocolate com Morango' , 'Pequena' , 31.90 , 'Chocolate, Morango' ,  "Chocolate")

    print(f" --- Pizza Comum ---")
    pizza_portuguesa.mostrar_detalhes()
    pizza_marguerita.mostrar_detalhes()
    pizza_calabresa.mostrar_detalhes()
    print(f" --- Pizza Doce ---")
    pizza_chocolate.mostrar_detalhes()

if __name__ == "__main__":
    main()