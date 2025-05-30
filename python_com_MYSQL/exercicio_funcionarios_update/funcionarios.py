import sqlite3
conexao = sqlite3.connect("funcionarios.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL
);
""")

cursor.execute("""
    INSERT INTO Funcionarios (nome, cargo, salario) VALUES
    ('Joao', 'Analista', 3000),
    ('Maria', 'Gerente', 5000),
    ('Lucas', 'Estagiario', 1500);
""")

cursor.execute("""
    UPDATE funcionarios SET salario = 5000 WHERE nome = "Maria";
""")

cursor.execute("""
    UPDATE funcionarios SET cargo = "assistente" WHERE nome = "Lucas";
""")

cursor.execute("SELECT * FROM funcionarios")
dados = cursor.fetchall()

for funcionarios in dados:
    print(funcionarios)

conexao.close()