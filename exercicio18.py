valor1=int(input("Qual o valor do primeiro número?"))
valor2=int(input("Qual o valor do segundo numero?"))

def exibeNumero(valor1, valor2):
    if valor1 == valor2:
        print("diferença do número 1 pro 2 é ", valor1-valor2)
        return abs(valor1-valor2)
    else:
        print("A diferença do numero 1 pro 2 é:",valor1-valor2)
        return abs(valor1-valor2)

exibeNumero (valor1, valor2)