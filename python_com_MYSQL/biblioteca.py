import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao NOT NULL
)
""")

titulo = input("digite o titulo do livro:")
autor = input("digite o nome do autor:")
ano_publicacao = int(input("digite o ano de publicacao do livro:"))

cursor.execute("""
    INSERT INTO livros(titulo,autor,ano_publicacao)
    VALUES (?,?,?)
""", (titulo,autor,ano_publicacao))

conexao.commit()
print("livro cadastrado com sucesso")

cursor.execute("SELECT * FROM livros")
dados = cursor.fetchall()

for livros in dados:
    print(livros)