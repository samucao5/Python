import sqlite3
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        idade INTEGER NOT NULL
)
                             
""")

nome = input("nome do cliente: ")
email = input("email: ")
idade = int(input("qual a sua idade: "))

cursor.execute("""
INSERT INTO clientes(nome,email,idade)
VALUES(?,?,?)
""",(nome,email,idade))

conexao.commit()
print("cliente cadastrado com sucesso")

cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()

for clientes in dados:
    print(clientes)

conexao.close()