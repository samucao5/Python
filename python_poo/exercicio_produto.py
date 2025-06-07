class produto:
    def __init__ (self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_dados_produtos(self):
        print(f" nome do produto: {self.nome}\n preco do produto:R$ {self.preco}\n quantidade de produtos: {self.quantidade}")

nome_do_produto = input("digite o nome do produto: ")
preco_produto = input("digite o preco do produto: ")
quantidade_produto = input("digite o quantidade do produto: ")

produto1 = produto(nome_do_produto,preco_produto,quantidade_produto)
produto1.exibir_dados_produtos()