class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f"seu nome e:  {self.nome} sua idade e:  {self.idade} ")

    
pessoa1 = pessoa("samuel", 19)

pessoa1.exibir_dados()

nome1 = input("digite seu nome:")
idade1 = int(input("digite sua idade:"))

pessoa2 = pessoa(nome1,idade1)
pessoa2.exibir_dados()