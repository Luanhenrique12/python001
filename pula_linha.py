def pular_linha_após_ponto(texto):
    novo_texto = texto.replace(" ","\n").replace(".", "").replace(",", "")
    
    return novo_texto
    
with open("word.txt", "r") as fs1:
    texto = fs1.read()  
    texto_formatado = pular_linha_após_ponto(texto)




print(texto_formatado)





