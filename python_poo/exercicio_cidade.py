class cidade:
    def __init__(self,cidade,estado,populacao):
        self.cidade = cidade
        self.estado = estado
        self.populacao = populacao
    
    def exibir_dados_cidade(self):
        print(f" cidade: {self.cidade}\n estado: {self.estado}\n populacao: {self.populacao}")

nome_cidade = input("digite o nome da sua cidade: ")
nome_estado = input("digite o seu estado: ")
numero_populacao = int(input("digite o numero de habitantes: "))

cidade1 = cidade(nome_cidade,nome_estado,numero_populacao)

cidade1.exibir_dados_cidade()



