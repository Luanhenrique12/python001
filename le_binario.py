def le_binario():
    try:
        with open("binary.jpg", "rb") as fs1:
            dados = fs1.read()
            print(type(dados))
        with open("copia_1.jpg", "wb") as fs2:
            fs2.write(dados)
        with open("copia_2.jpg", "wb") as fs2:
            fs2.write(dados)
        with open("copia_3.jpg", "wb") as fs2:
            fs2.write(dados)
    except FileNotFoundError as e:
        print('Arquivo não existe! -_-|||', e)
    except IOError as e:
        print('Deu algo errado @_@', e)
    print("OK! ~_~")

le_binario()
