import sqlite3
conexao = sqlite3.connect("livros.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL
);
""")

cursor.execute("""
INSERT INTO Livros (titulo, autor, ano) VALUES
('Dom Casmurro', 'Machado de Assis', 1899),
('1984', 'George Orwell', 1949),
('O Alquimista', 'Paulo Coelho', 1988);
""")

conexao.commit()
print("livros salvos")

cursor.execute("UPDATE livros SET ano = 1900 WHERE titulo = 'Dom Casmurro'")

cursor.execute("UPDATE livros SET autor = 'ORWELL' WHERE titulo = '1984'")

cursor.execute("SELECT * FROM livros")
dados = cursor.fetchall()

for livros in dados:
    print(livros)

conexao.close()
