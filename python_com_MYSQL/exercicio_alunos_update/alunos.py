import sqlite3
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL
);
""")

cursor.execute("""
INSERT INTO Alunos (nome, idade, curso) VALUES
('Ana', 20, 'Engenharia'),
('Pedro', 22, 'Direito'),
('Clara', 19, 'Medicina');
               
""")

cursor.execute("UPDATE alunos SET curso = 'engenharia' WHERE nome = 'Pedro'")
cursor.execute("UPDATE alunos SET idade = 21 WHERE nome = 'Ana'")

conexao.commit()

cursor.execute("SELECT * FROM alunos")
dados = cursor.fetchall()
for alunos in dados:
    print(alunos)

conexao.close()