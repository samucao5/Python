class aluno:
    def __init__(self,nome,nota):
        self.__nome = nome
        self.__nota = nota
    
    def get_nome(self):
       print(f"{self.__nome}")

    def get_nota(self):
       print(f"{self.__nota}")

    def set_nome(self,novo_nome):
       self.__nome = novo_nome

    def set_nota(self,nova_nota):
       if(nova_nota >= 0 and nova_nota <= 10):
        self.__nota = nova_nota
        print(f"nota modificado {self.__nota}")
    
    def aprovado(self):
       if(self.__nota >= 6):
          print(f"o aluno {self.__nome} esta aprovado com {self.__nota}")
       else:
          print(f"o aluno {self.__nome} esta reprovado com {self.__nota}")


aluno1 = aluno("samuel", 0)
novo_nome = input("digite o nome do aluno: ")
aluno1.set_nome(novo_nome)
nova_nota = int(input("digite a nota do aluno: "))
aluno1.set_nota(nova_nota)
aluno1.get_nome()
aluno1.get_nota()
aluno1.aprovado()


