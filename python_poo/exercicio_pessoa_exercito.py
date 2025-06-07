class pessoa:
    def __init__(self,nome,idade,sexo):
        self.nome = nome 
        self.idade = idade 
        self.sexo = sexo

    def verificar_maioridade(self):
        if(self.idade >= 18):
            print(f"{self.nome} e maior de idade")
        else:
            print(f"{self.nome} e menor de idade")

    def pode_servir_o_exercito(self):
        if(self.sexo == "masculino" and self.idade >= 18):
            print(f"{self.nome} pode servir o exercito")
        elif(self.sexo == "masculino" and self.idade < 18):
            print(f"{self.nome} ainda nao pode servir o exercito")
        else:
            print("nao precisa obrigatoriamente servir o exercito")

nome1 = input("digite o seu nome: ")
idade1 = int(input("digite sua idade: "))
sexo1 = input("digite seu sexo:")

pessoa1 = pessoa(nome1, idade1, sexo1)
pessoa1.verificar_maioridade()
pessoa1.pode_servir_o_exercito()