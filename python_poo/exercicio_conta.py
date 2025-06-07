class conta:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo 
    
    def adicionar_saldo(self):
        self.saldo = int(input("digite o saldo:"))
    
    def exibir_saldo(self):
        print(f"o nome do titular: {self.titular}\nsaldo: {self.saldo}" )

nome_do_titular = input("digite o nome do titular: ")

saldo1 = 0

conta_1 = conta(nome_do_titular,saldo1)
conta_1.adicionar_saldo()
conta_1.exibir_saldo()

