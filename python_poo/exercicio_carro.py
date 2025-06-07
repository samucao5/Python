class carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano

    def exibir_dados_completos(self):
        print(f"a marca do carro e: {self.marca}\no modelo do carro e: {self.modelo}\no ano do carro e: {self.ano}")
    
marca_1 = input("a marca do carro: ")
modelo_1 = input("o modelo do carro: ")
ano_1 = int(input("o ano do carro:"))

carro_1 = carro(marca_1,modelo_1,ano_1)
carro_1.exibir_dados_completos()