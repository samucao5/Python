import sqlite3
conexao = sqlite3.connect("cursos.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cursos(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL,
    instrutor TEXT NOT NULL,
    duracao TEXT NOT NULL
)
""")

i = 1
while i <= 2:
    nome = input("digite seu nome:")
    instrutor = input("digite o nome do instrutor:")
    duracao = int(input("digite a duracao do curso:"))
    if(duracao >= 1):
        cursor.execute("""
            INSERT INTO cursos(nome,instrutor,duracao) VALUES (?,?,?)            
        """, (nome,instrutor,duracao))
    conexao.commit()
    print("curso encontrado")
    i = i + 1

cursor.execute("SELECT * FROM cursos")
dados = cursor.fetchall()

for cursos in dados:
    print(cursos)

conexao.close()
