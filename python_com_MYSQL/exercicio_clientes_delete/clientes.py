import sqlite3 
quasar = sqlite3.connect("loja.db")
cursor = quasar.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cidade TEXT NOT NULL
);
""")

cursor.execute("""
INSERT INTO Clientes (nome, cidade) VALUES
('Carlos', 'São Paulo'),
('Juliana', 'Rio de Janeiro'),
('Rafael', 'Belo Horizonte');
""")

cursor.execute("DELETE FROM clientes WHERE nome = 'Rafael'")
cursor.execute("DELETE FROM clientes WHERE cidade = 'Rio de Janeiro'")

quasar.commit()
print("clientes cadastrados com sucesso")
cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()
for clientes in dados:
    print(clientes)

quasar.close()