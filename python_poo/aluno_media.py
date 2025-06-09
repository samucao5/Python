
class aluno:
    def __init__(self,nome,nota_1,nota_2,media):
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.media = media
    def calcular_media(self):
        media = (self.nota_1 + self.nota_2)/2
        print(f"{self.nota_1} + {self.nota_2} / 2 = {self.media}")

    def verificar_aprovacao(self):
        if(self.media >= 7):
            print(f"o {self.nome} esta aprovado")
        else:
            print(f"o {self.nome} esta reprovado")

nome_aluno = input("digite seu nome: ")
nota1 = int(input("digite a primeira nota do aluno: "))
nota2 = int(input("digite a segunda nota do aluno: "))
media_1 = 0

aluno1 = aluno(nome_aluno,nota1,nota2,media_1)
aluno1.calcular_media()
aluno1.verificar_aprovacao()

