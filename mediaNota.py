

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

def exibirMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6:
        print("Aprovado! Sua media final é:", media)
    else:
        print("Reprovado, continue estudando!", media)

exibirMedia(nota1, nota2)