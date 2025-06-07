class filme:
    def __init__(self,titulo,ano,genero):
        self.titulo = titulo
        self.ano = ano 
        self.genero = genero

    def exibir_dados_filme(self):
        print(f"nome do filme: {self.titulo}\n ano do filme: {self.ano}\n genero do filme: {self.genero}")


titulo_do_filme = input("digite o titulo do filme: ")
ano_filme = int(input("digite o ano do filme: "))
genero_filme = input("digite o genero do filme: ")

filme1 = filme(titulo_do_filme,ano_filme,genero_filme)

filme1.exibir_dados_filme()

