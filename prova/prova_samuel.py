import random
valor = True
while valor == True:
    i = 0
    tentativa = 0
    numeros = 0
    print("deseja jogar em qual modo")
    print("1 - facil")
    print("2 - medio")
    print("3 - dificil")
    escolha = int(input("digite sua escolha: "))
    
    if(escolha == 1):
        numero = 40
        tentativa = 20
    elif(escolha == 2):
        numero = 70
        tentativa = 10
    elif(escolha == 3):
        numero = 100
        tentativa = 5
    else:
        print("valor nao encontrado")
    
    num = random.randint(1,numero)

    print ("seu numero de tentativas e:",tentativa)
    print("o valor maximo e: ", numero)
    while(i <= tentativa ):
        print("tentativa",i)
        jogador = int(input("digite o numero:"))
        if(jogador == num):
            print("voce acertou o numero era:", num)
            i = tentativa
        
        elif(jogador < num):
            print("x > ", jogador)
        else:
            print(" x < ", jogador)
    
        i += 1

    print("o valor aleatorio era: ", num)
    
    escolha2 = input("deseja jogar denovo: digite sim ou nao")
    if(escolha2 == "nao" or escolha2 == "NAO"):
        valor = False