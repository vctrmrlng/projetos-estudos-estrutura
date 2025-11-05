class Veiculo:
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado)
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado

    def abastecer(self):
        self.qtd_combustivel += 20
    

    # Se o carro já está ligado -> mensagem de que já está ligado
    # Se o carro está desligado -> liga o carro e informa que ligou
    def ligar(self):
        if self.is_ligado:
            print("🚘 O carro já estava ligado")
        else self.is_ligado = True
            print("🚗 O carro foi ligado")

    # def ligar(self):
    #       if self.is_ligado:
    #            print("🚗 O carro já está ligado.")
        
    #     self.is_ligado = True
    #     print("🚘 O carro foi ligado.")

    def desligar(self):
        if self.is_ligado == False:
            print ("🚘 O carro já está desligado!!!")
        else:
            self.is_ligado = False
            print("O carro foi desligado.")