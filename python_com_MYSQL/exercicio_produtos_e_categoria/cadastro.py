import sqlite3
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()
i = 1
cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL           
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL,
        categoria_id INTEGER NOT NULL, FOREIGN KEY(categoria_id) REFERENCES categoria(id)                      
    )
""")
#caso queira mudar a categoria


cursor.execute("""
    INSERT INTO categorias(nome) VALUES ("eletronico")
""")

cursor.execute("""
    INSERT INTO categorias(nome) VALUES ("limpeza")
""")

conexao.commit()
print("categorias salvas")

while i <= 4:
    nome = input("digite o nome do produto:")
    preco = float(input("digite o preco do produto:"))
    if(preco > 0):
        estoque = int(input("qual o estoque do produto:"))
        if estoque > 0:
            categoria_id = int(input("digite entre 1 ou 2:"))
            if categoria_id == 1 or categoria_id == 2:
                cursor.execute("""
                INSERT INTO produtos(nome,preco,estoque,categoria_id) VALUES (?,?,?,?)
                """,(nome,preco,estoque,categoria_id))

                conexao.commit()
                print("produto salvo")
    i += 1
        
cursor.execute("SELECT * FROM produtos")
dados = cursor.fetchall()

for produtos in dados:
    print(produtos)

conexao.close()
