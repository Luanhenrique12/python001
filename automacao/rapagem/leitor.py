import csv

nome_do_arquivo = 'automacao\\rapagem\\maneiro.csv'
try:
    arquivo = open(nome_do_arquivo)
    leitor = csv.reader(arquivo, delimiter=';' , dialect='excel')

    for linha in leitor:
        print('Linha #%s <%s>' % (leitor.line_num, linha))

    arquivo.close()
except FileNotFoundError:
    print('Arquivo não encontrado')