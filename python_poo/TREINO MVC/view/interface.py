from controller.controle_funcionarios import controle_funcionarios

class interface:
    def __init__(self):
        self.controle = controle_funcionarios()

    def menu(self):
        valor = True
        while valor == True:
            print("digite 1 para inserir os dados")
            print("digite 2 para listar os dados")
            print("digite 3 para sair ")
            opcao = int(input("digite a sua opcao: "))

            if(opcao == 1):
                nome = input("digite o nome do funcionario: ")
                cargo = input("digite o cargo do funcionario: ")
                idade = int(input("digite a idade do funcionario: "))
                self.controle.inserir(nome,cargo,idade)

            elif(opcao == 2):
                print(self.controle.lista())
            
            elif(opcao == 3):
                print("fechando programa...")
                valor = False
            else:
                 print("valor ")
