class produtos:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        valor_total = self.preco * self.quantidade
        print(f"o valor total do produto {self.nome} e: {valor_total}")

    def verificar_disponiblidade(self):
        if(self.quantidade > 0):
            print(f"o produto {self.nome} ainda possui estoque possuindo: {self.quantidade}")
        else:
            print(f"o produto {self.nome} esta esgotado tente outro dia")
    
nome_produto = input("digite o nome do produto: ")
preco_produto = float(input("digite o preco do produto: "))
quantidade_produto = int(input("digite o estoque de produto: "))

produto_1 = produtos(nome_produto,preco_produto,quantidade_produto)
produto_1.calcular_total()
produto_1.verificar_disponiblidade()

