import sqlite3
conexao = sqlite3.connect("cinema.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    diretor TEXT NOT NULL,
    ano INTEGER NOT NULL
);
            
""")

cursor.execute("""
INSERT INTO Filmes (titulo, diretor, ano) VALUES
('Matrix', 'Wachowski', 1999),
('Titanic', 'James Cameron', 1997),
('Inception', 'Christopher Nolan', 2010);
            
""")

cursor.execute("""
UPDATE filmes SET diretor = 'Lana Wachowski' WHERE titulo = 'Matrix';
""")

cursor.execute("""
UPDATE filmes SET ano = 1998 WHERE titulo = 'Titanic';
""")

conexao.commit()

cursor.execute("SELECT * FROM filmes")
dados = cursor.fetchall()

for alunos in dados:
    print(alunos)

conexao.close()