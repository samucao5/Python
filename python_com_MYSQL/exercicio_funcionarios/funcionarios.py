import sqlite3
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL, 
        salario REAL NOT NULL
               
    )
""")
i = 1
while i <= 2:
    nome = input("digite o seu nome:")
    cargo = input("digite seu cargo:")
    salario = float(input("digite seu salario:"))
    if salario > 1412:
        cursor.execute("""
        INSERT INTO funcionarios(nome,cargo,salario) VALUES (?,?,?)
        """,(nome,cargo,salario))
        conexao.commit()
        print("funcionario adicionado com sucesso")
    i += 1
cursor.execute("SELECT * FROM funcionarios")
dados = cursor.fetchall()

for funcionarios in dados:
    print(funcionarios)

conexao.close()