import sqlite3
conexao = sqlite3.connect("petshop.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS animais(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especie TEXT NOT NULL,
    idade INTEGER NOT NULL
    )
""")
i = 1
while i <= 3:
    nome = input("digite o nome do animal:")
    especie = input("digite a especie do animal:")
    idade = int(input("digite a idade do animal:"))
    if idade >= 0:
        cursor.execute("""
        INSERT INTO animais (nome,especie,idade) VALUES (?,?,?)
        """, (nome,especie,idade))
        conexao.commit()
        print("animal cadastrado com sucesso")
    i += 1

cursor.execute("SELECT * FROM animais")
dados = cursor.fetchall()

for animais in dados:
    print(animais)

conexao.close()