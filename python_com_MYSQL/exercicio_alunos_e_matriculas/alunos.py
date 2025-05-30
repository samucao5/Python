import sqlite3 
conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS matriculas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        curso TEXT NOT NULL,
        nota_inicial INTEGER NOT NULL,
        aluno_id INTEGER NOT NULL,FOREIGN KEY(aluno_id) REFERENCES alunos(id)    
    )         
""")

vetor_alunos = [
    ("samuel", 19),
    ("maria",19),
    ("isa",18),
    ("allan",17),
    ("joao",15)
]

for nome,idade in vetor_alunos:
    cursor.execute("""
        INSERT INTO alunos(nome,idade) VALUES (?,?)
        """,(nome,idade))
    
conexao.commit()
print("alunos cadastrados")
i = 1
while i <= 4:
    aluno_id = int(input("digite o id do aluno:"))
    if(aluno_id > 0):
        curso = input("digite o curso deste aluno:")
        nota_inicial = int(input("digite a nota deste aluno:"))
        if(nota_inicial >= 0 and nota_inicial <= 10):
            cursor.execute("""
            INSERT INTO matriculas(aluno_id,curso,nota_inicial) VALUES (?,?,?)
            """,(aluno_id,curso,nota_inicial))
            conexao.commit()
            print("matricula finalizada")
    i += 1
    
cursor.execute("SELECT alunos.nome,matriculas.curso,matriculas.nota_inicial FROM matriculas JOIN alunos ON alunos.id = matriculas.aluno_id ")
dados = cursor.fetchall()

for matriculas in dados:
    print(matriculas)

conexao.close()