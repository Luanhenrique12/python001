def le_binario():
    try:
        with open("binary.jpg", "rb") as fs1:
            dados = fs1.read()
            print(type(dados))
        with open("teste01.jpg", "wb") as fs2:
            fs2.write(dados)

    
    except FileNotFoundError as e:
        print('Arquivo não existe! -_-|||', e)
    except IOError as e:
        print('Deu algo errado @_@', e)
        print("OK! ~_~")
    
    import os

    try:
        os.remove("teste02.jpg")
        print(f"Excluido {"teste01.jpg"}")
    except: 
        print("não foi possivel")

le_binario()
