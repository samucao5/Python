import sqlite3 

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    curso TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

nome = input("digite o nome do aluno: ")
curso = input("digite o curso: ")
idade = int(input("digite sua idade: "))

cursor.execute("""
    INSERT INTO alunos(nome,curso,idade) VALUES (?,?,?) 
""",(nome,curso,idade))

conexao.commit()
print("aluno criado com sucesso")

cursor.execute("SELECT * FROM alunos")
dados = cursor.fetchall()

for alunos in dados:
    print(alunos)

conexao.close()