class contaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        print(f"saldo atual: {self.__saldo}")
    
    def depositar(self,valor):
        if(valor > 0):
            self.__saldo =+ valor
        else:
            print("valor tem que ser positivo")
    
    def sacar(self,valor):
        if(valor <= self.__saldo):
            self.__saldo =- valor
        else:
            print("voce nao possui saldo")
    
titular_1 = input("digite o nome do titular desta conta: ")
teste = True

conta_1 = contaBancaria (titular_1,0)
print("digite o que deseja fazer: ")
teste = True

while(teste == True):
    print("1 - olhar o saldo \n 2 - depositar \n 3 - sacar \n 4 - para sair do programa")
    escolha = int(input("digite sua escolha: "))
    if(escolha == 1):
        conta_1.get_saldo()

    if(escolha == 2):
        valor = int(input("digite o quanto voce quer depositar: "))
        conta_1.depositar(valor)

    if(escolha == 3):
        valor = int(input("digite o quanto voce quer depositar: "))
        conta_1.sacar(valor)

    if(escolha == 4):
        teste = False
    
    else:
        print("o valor invalido")