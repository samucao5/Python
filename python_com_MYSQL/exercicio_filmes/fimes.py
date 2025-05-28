import sqlite3
conexao = sqlite3.connect("cinema.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    diretor TEXT NOT NULL,
    ano INTEGER NOT NULL
    )
    """)

titulo = input("digite o titulo do filme: ")
diretor = input("digite o diretor do filme: ")
ano = int(input("digite o ano de lancamento do filme:"))

cursor.execute("""
INSERT INTO filmes(titulo,diretor,ano) VALUES (?,?,?)
""",(titulo,diretor,ano))

conexao.commit()
print("o filme foi cadastrado com sucesso")

cursor.execute("SELECT * FROM filmes")
dados = cursor.fetchall()

for filmes in dados:
    print(filmes)

conexao.close()
