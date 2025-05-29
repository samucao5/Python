import sqlite3
conexao = sqlite3.connect("veiculo.db")
cursor = conexao.cursor()
valor = True
i = 1
cursor.execute("""
    CREATE TABLE IF NOT EXISTS veiculos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT NOT NULL,
        marca TEXT NOT NULL,
        ano INTEGER NOT NULL
    )
""")

while i <= 2:
    modelo = input("digite o modelo do carro:")
    marca = input("digite a marca do carro:")
    ano = int(input("digite o ano do carro:"))
    if ano >= 1886:
        cursor.execute("""
        INSERT INTO veiculos (modelo,marca,ano) VALUES (?,?,?)
        """, (modelo,marca,ano))
        conexao.commit()
        print("carro cadastrado com sucesso")
    i = i + 1

cursor.execute("SELECT * FROM veiculos")
dados = cursor.fetchall()



for veiculos in dados:
    print(veiculos)


conexao.close()
