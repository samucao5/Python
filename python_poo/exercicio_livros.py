class livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

    def exibir_dados_livro(self):
        print(f"o livro {self.titulo} tem {self.paginas} paginas")
    
titulo_1 = input("digite o nome do livro: ")
paginas_1 = int(input("digite o numero de paginas do livro: "))

livros_1 = livro(titulo_1, paginas_1)
livros_1.exibir_dados_livro()