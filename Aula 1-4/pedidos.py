# Crie um programa que aceita pedidos de e-commerce até cliente digite sair
print("Faça o seu pedido ou digite 'sair' para encerrar")
pedido = "" #string porque 'sair' é um texto
lista = ["Smartphone","Smart TV","Geladeira","Fogão","Relogio","SSD","Notebook"]

while pedido.lower() != 'sair':
    pedido = input("Digite um produto da lista:")
    if pedido in lista:
        print(f"{pedido} adicionado ao seu carrinho!")
    elif pedido.lower() == "sair":
        print("Pedido Encerrado")
    else:
        print("Esse produto não está na lista. Escolha outro.")