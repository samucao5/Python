class produto:
    def __init__(self, nome,preco):
        self.__nome = nome
        self.__preco = preco

    def set_nome(self,novo_nome):
        self.__nome = novo_nome 
    
    def set_preco(self,novo_preco):
        if(novo_preco > 0):
            self.__preco = novo_preco
            print(f"preco do produto {self.__nome} alterado para R$ {self.__preco}")
        else:
            print("valor escolhido menor do que 0, tente novamente")
    def get_produtos(self):
        print(f"nome do produto: {self.__nome} preco do produto: {self.__preco}")


produto1 = produto("vassoura",0)
produto1.get_produtos()
novo_nome = input("digite o novo nome do produto: ")
produto1.set_nome(novo_nome)
novo_preco = float(input("digite o novo preco do produto: "))
produto1.set_preco(novo_preco)
produto1.get_produtos()
