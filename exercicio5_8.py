#s=0
#while True:
   # v=int(input("Digite o númeroa somar ou sair para sair"))
    #if v==0:
        #break
    #s=s=v
    #print(s)

soma = 0 
while True:
    entrada = input("Digite um número para somar ou 'sair' para encerrar: ")
    if entrada.lower() == "sair":
        break
    try:
        v = int(entrada)
        soma += v
    except ValueError:
        print("Entrada inválida. Digite um número ou 'sair'.")
        continue
    print("Soma atual:", soma)