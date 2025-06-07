class aluno:
    def __init__(self,aluno,curso,matricula):
        self.aluno = aluno
        self.curso = curso
        self.matricula = matricula

    def exibir_dados_alunos(self):
        print(f" nome do aluno: {self.aluno}\n nome do curso: {self.curso}\n numero da matricula: {self.matricula}")
    

nome = input("digite o nome do aluno:")
curso_i = input("digite o nome do curso:")
matricula_i = int(input("digite o numero da matricula:"))

aluno1 = aluno(nome,curso_i,matricula_i)

aluno1.exibir_dados_alunos()