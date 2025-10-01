def fazer_pedido(cardapio):
    pedido=[]  #lista vazia
    while True:
        sabor = input("Digite o sabor da pizza que deseja (ou 'sair') finalizar.")
        if sabor =="sair":
            break
        elif sabor in cardapio:
            pedido.append(sabor)
            print(f'🍕{sabor} adicionado no seu pedido!')
        else:
            print(f'✖️Esse sabor não está disponível. Escolha outro.')
        return pedido
cardapio = ["Mussarela","Calabreza","Pepperoni", "FRango com Catupiry"]
pedido_cliente = fazer_pedido (cardapio)
print(pedido_cliente)
    
