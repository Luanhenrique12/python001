#fim=int(input("Digite o último número a imprimir:"))
#if fim % 2 == 1:#
    #print(fim, "É número impar")
#else:
    #print(fim, "É número par")
n=int(input("Qual multiplicação quer saber? "))
multiplicacao=int(input("Qual o valor da multiplicação? "))
x=1
while x<=multiplicacao:
    print(n,"X",x,"=",n*x)
    x=x+1