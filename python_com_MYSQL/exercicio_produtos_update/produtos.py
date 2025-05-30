import sqlite3 
conexao = sqlite3.connect("produto.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
);
""")

cursor.execute("""
INSERT INTO Produtos (nome, preco) VALUES
('Camiseta', 50.0),
('Tenis', 200.0),
('Bone', 30.0);

""")

cursor.execute( """
UPDATE produtos SET preco = 180 WHERE nome = "tenis";
""")

cursor.execute("""
UPDATE produtos SET preco = 60 WHERE nome = "camiseta";
""")

cursor.execute("SELECT * FROM produtos")
dados = cursor.fetchall()

for produtos in dados:
    print(produtos)