nome=input("Qual o seu nome?")
print("Seja bem vindo!", nome)
numero=int(input("Qual o seu número para contato? digite com o DDD:"))
email=(input("Qual o seu e-mail para não ficar de fora de promoções inperdíveis:"))


valor1=59.99 #Toscana
valor2=54.99 #Muçarela
valor3=57.99 #Marguerita
valor4=52.99 #Calabresa

cardapio={
1:{"Sabor": "Toscana","preço": 59.99},
2:{"Sabor": "Muçarela","preço": 54.99},
3:{"Sabor": "Marguerita","preço": 57.99},
4:{"Sabor": "Calabresa","preço": 52.99},
}
while True:   
    print("Cardapio do dia:")

    print("01--Pizza toscana--R$ 59.99")
    print("02--Pizza Muçarela --R$ 54.99")
    print("03--Pizza Marguerita --R$ 57.99")
    print("04--Pizza Calabresa --R$ 52.99")

    escolha=input("O que você deseja?")
    if escolha=="1" or escolha=="2"or escolha=="3" or escolha=="4":
        escolha=int(escolha)
        pizza=cardapio[escolha]

    
    else:
        print("Opção invalida, tente novamente:")
        continue

    continuar=input("deseja continuar? Digite Sim/finalizar").lower()
    if continuar =="sim":
        continue
        
    else:
        print("--Comprovante da compra:--")
    print(nome)
    print(numero)
    print(email)
    from datetime import date
    dataAtual=date.today()
    print(dataAtual)
    valor=cardapio[escolha]
    break

        
     

#print("Cardapio:","Pizza Toscana:",valor1,"Pizza Muçarela:",valor2,"Pizza Margueirita:",valor3,"Pizza Calabresa:", valor3)













#l="Felipe"
#2="11944414078"
#3="fgelipesouza@gmail.com"
#4="senhora@yahoo.com"
#valor





