#digite = input("Digite qualquer coisa: ")
#fim= 0

#for caractere in digite:
    #if caractere.isalpha():
        #fim+= 1
        #media=fim/2

#print("Número de letras digitadas:", fim)
#print("media de letras digitadads:", media)

#digite=input("Digite qualquer coisa:")
#fim=0
#while fim<len(digite):
    #print(digite[fim], fim)
    #fim=fim+1
    #print("Quantidades de letras digitadas:")

lista=[]
soma=0
while True:
    numero= int(input("Digite o número inteiro:"))
    if numero == 0:
        break
    soma+=numero
    lista.append(numero)
    print("O Resultado da soma é:",soma)
    print("A média aritimetica é:",soma/len(lista))

