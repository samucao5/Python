import sqlite3
com = sqlite3.connect("loja.db")
cursor = com.cursor()
comp = True

cursor.execute("""
CREATE TABLE IF NOT EXISTS loja(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    estoque INTEGER NOT NULL,
    preco_unitario REAL NOT NULL
                    
    )
""")
print("deseja cadastrar um produto")
escolha_1 = input("digite sim ou nao:")
if(escolha_1 == "sim" or escolha_1 == "SIM"):

    while(comp == True):
        nome = input("digite o nome do produto:")
        estoque = int(input("digite o estoque do produto:"))
        preco_unitario = float(input("digite o preco do produto:"))
        cursor.execute("""
        INSERT INTO loja(nome,estoque,preco_unitario) VALUES(?,?,?)
        """,(nome,estoque,preco_unitario))
        com.commit()
        print("produto cadastrado com sucesso")
        print("deseja sair do cadastro do produto")
        escolha = input("digite sim ou nao")
        if(escolha == "sim" or escolha == "SIM"):
            comp = False
            
print("deseja ver os produtos: ")
escolha_2 = input("digite sim ou nao: ")
if(escolha_2 == "sim" or escolha_2 == "SIM"):
    cursor.execute("SELECT * FROM loja")
    dados = cursor.fetchall()
    for loja in dados:
        print(loja)

print("deseja mudar um valor: ")
escolha_3 = input("digite sim ou nao: ")
if(escolha_3 == "sim" or escolha_3 == "SIM"):
    id_1 = input("digite o id do produto que voce deseja mudar:")
    print("o que voce deseja mudar: ")
    print("1 para nome")
    print("2 para estoque")
    print("3 para preco_unitario")
    escolha_up = int(input("digite o numero: "))
    if(escolha_up == 1):
        mud_nome = input("digite o novo nome do produto: ")
        cursor.execute("UPDATE loja SET nome = ?  WHERE id = ?", (mud_nome,id_1))
        print("nome modificado")
    elif(escolha_up == 2):
        mud_estoque = int(input("digite o novo valor de estoque: "))
        cursor.execute("UPDATE loja SET estoque = ?  WHERE id = ?", (mud_estoque,id_1))
        print("estoque modificado")
    elif(escolha_up == 3):
        mud_preco = float(input("digite o novo preco_unitario: "))
        cursor.execute("UPDATE loja SET preco_unitario = ? WHERE id = ?", (mud_preco,id_1))
        print("preco modificado")
    else:
        print("valor invalido")

print("deseja apagar alguma tabela: ")
escolha_4 = input("digite sim ou nao")
if(escolha_4 == "sim" or escolha_4 == "SIM"):
    id_2 = int(input("digite o id do produto que voce deseja apagar: "))
    cursor.execute("DELETE FROM loja WHERE id = ? ",(id_2,))


print("deseja procurar alguma tabela:")
escolha_5 = input("digite sim ou nao")
if(escolha_5 == "sim" or escolha_5 == "SIM"):
    print("como deseja buscar por id ou nome: ")
    print("1 para id")
    print("2 para nome")
    escolha_min = int(input("digite a escolha: "))
    if(escolha_min == 1):
        id_3 = int(input("digite o id que deverar ser procurado: "))
        cursor.execute("SELECT * FROM loja WHERE id = ?", (id_3,))
        for loja in cursor.fetchall():
            print(loja)

    elif(escolha_min == 2):
        nome_bus = input("digite o nome que devera ser procurado: ")
        cursor.execute("SELECT * FROM loja WHERE nome = ?", (nome_bus,))
        for loja in cursor.fetchall():
            print(loja)

    else:
        print("valor invalido")


print("deseja ver os produtos novamente:")
escolha_2 = input("digite sim ou nao: ")
if(escolha_2 == "sim" or escolha_2 == "SIM"):
    cursor.execute("SELECT * FROM loja")
    dados = cursor.fetchall()
    for loja in dados:
        print(loja)

com.close()