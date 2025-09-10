# 1. **Crie uma função `exibir_cardapio()`:** Esta função deve criar o dicionário do cardápio e usar um loop `for` para imprimi-lo na tela.
# 2. **Crie uma função `receber_pedido()`:** Esta função deve conter o loop `while` que recebe os sabores do cliente e os armazena em uma lista. Ela deve **retornar** a lista de pedidos.
# 3. **Crie uma função `calcular_total()`:** Esta função deve receber a lista de pedidos e o dicionário do cardápio como **parâmetros**. Ela deve calcular o valor total e **retornar** o resultado.
# 4. **Execute o fluxo:** No código principal, chame as funções na ordem correta para simular o processo de pedido: `exibir_cardapio()`, `receber_pedido()`, `calcular_total()` e, por fim, imprima o total final.

def exibir_cardapio():  
    cardapio = {
        "Mussarela" : 30.00,
        "Calabresa" : 32.00,
        "Pepperone" : 35.00,
        "Quatro Queijos" : 38.00,
        "Frango com Catupiry" : 40.00,
            }
    print('Cardápio da Pizzaria Sabores')
    for pizza, preco in cardapio.items():
        print(f"🍕{pizza} : R${preco:.2f}")
    return cardapio


def receber_pedido(cardapio):
    print("Bem vindo à pizzzaria Sabore!")
    pedido = []
      
    while True:
        sabor_escolhido = input('Digite o nome do sabor para adicionar ao pedido, ou sair para encerrar: ')
        if sabor_escolhido.lower() == "sair":
            break
        elif sabor_escolhido in cardapio:
            pedido.append(sabor_escolhido)
            print(f'🍕 {sabor_escolhido} adicionado ao seu pedido')
        else :
            print('Esse sabor não está no cardapio')
    print(f'Seu pedido é {pedido}')
    return pedido


def calcular_total(pedido, cardapio):
    total = 0
    for sabor in pedido:
        total += cardapio[sabor]
    return total


def main():
    cardapio = exibir_cardapio()
    pedido = receber_pedido(cardapio)
    total = calcular_total(pedido, cardapio)

    print(f'Resumo do pedido')
    for pizza in pedido:
        print(f'{pizza} - R% {cardapio[pizza]:.2f}')
    print(f'💵Total a pagar: R$ {total:.2f}')

main()
