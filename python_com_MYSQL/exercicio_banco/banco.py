import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titular TEXT NOT NULL,
        agencia TEXT NOT NULL,
        saldo REAL NOT NULL
                    
    )
""")

i = 1

while i <= 3:
    titular = input("digite seu nome:")
    agencia = input("digite a agencia do banco:")
    saldo = float(input("digite qual seu saldo atual:"))
    if(saldo > 0):
        cursor.execute("""
    INSERT INTO contas(titular,agencia,saldo) VALUES (?,?,?)
    """,(titular,agencia,saldo))
    conexao.commit()
    print("conta criada com sucesso")
    i = i + 1

cursor.execute("SELECT * FROM contas")
dados = cursor.fetchall()

for contas in dados:
    print(contas)

conexao.close()