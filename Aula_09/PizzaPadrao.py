#CLasse pai - SuperClass()
class PizzaPadrao:
    def __init__(self, sabor, tamanho, preco, ingredientes):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco
        self.ingredientes = ingredientes

    def mostrar_detalhes (self):
        print(f'''
        "--- 🍕Detalhes da Pizza ---
                Sabor: {self.sabor}
                Tamanho: {self.tamanho}
                Preço: R$ {self.preco}
                Ingredientes: {self.ingredientes}''')
        
# pizza001 = PizzaPadrao('Portuguesa' , 'Grande' , 49.99 , 'Mussarela, Linguiça Calabresa, Cebola, Orégano e Molho de Tomate')
# pizza002 = PizzaPadrao('Marguerita' , 'Pequeno' , 54.99 , 'Tomate, Manjericão, Mussarela, Orégano, Molho de Tomate')

# pizza001.mostrar_detalhes()
# pizza002.mostrar_detalhes()