import csv

nome_do_arquivo = 'csv\\OCORRENCIAS_2025.csv'
try:
    arquivo = open(nome_do_arquivo)
    leitor = csv.reader(arquivo, delimiter=',' , dialect='excel')

    for linha in leitor:
        print('Linha #%s <%s>' % (leitor.line_num, linha))

    arquivo.close()
except FileNotFoundError:
    print('Arquivo não encontrado')
    


while True:

    casos:{
         "Pistola","Revolver","Carabina","Espingarda"
    }
    
    contagem=0 
    pistola="Pistola"
    if "Pitola":
            contagem=contagem=="Pistola"
            print(contagem)



