import sqlite3;

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )
""")

nome = input("digite o nome do produto:")
preco = float(input("qual o preco do produto:"))
estoque = int(input("qual o estoque do produto:"))

cursor.execute("""
    INSERT INTO produtos (nome,preco,estoque) VALUES (?,?,?) 
""",(nome,preco,estoque))

conexao.commit()
print("produto cadastrado com sucesso")

cursor.execute("SELECT * FROM produtos")
dados = cursor.fetchall()

for produtos in dados:
    print(produtos)

conexao.close()
