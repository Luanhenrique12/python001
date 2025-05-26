#numero = 3

#def apresentarnumero():
    #global numero
    #print(numero)  # Vai imprimir 3
    #numero = 4
    #print(numero)  # Vai imprimir 4

#apresentarnumero()
#print(numero)

#nome=input("Escreva seu nome!")

#def apresentarNome():
    #global nome
    #print(nome)


#apresentarNome()
#nome=input("Nome completo por favor!")
#print( "Parabéns você foi cadastrado!", nome)




#saldo=int(input("Digite o saldo bancario"))
#saque=int(input("digite o valor do saque"))

#if saldo >= saque:
    #saldo=saldo-saque
    #print("Você realizou um saque com sucesso!")
#else:
    #print("Você não possui saldo bancario pare realizar essa operação!")




saldo = int(input("Digite o saldo bancário: "))
saque = int(input("Digite o valor do saque: "))

def saqueBancario(saldo, saque): 
    if saldo >= saque:
        conta = saldo - saque
        print("Você realizou um saque com sucesso! Saldo da conta:", conta)
    else:
        print("Você não possui saldo suficiente para realizar essa operação! Seu saldo bancário é de:", saldo)





saqueBancario(saldo, saque)