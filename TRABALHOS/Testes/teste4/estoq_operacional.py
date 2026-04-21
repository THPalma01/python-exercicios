arqP = open('c1_produtos.txt', 'r')
arqV = open('c1_vendas.txt', 'r')
arqT = open('TRANSFERE.TXT', 'w')

linhaV = arqV.readline().strip()
linhaP = arqP.readline().strip()



cod = []
qtco = []
qtmin = []
qtvendas = []



while linhaP != 0:
    linha = linha.split(';')
    cod.append(int(linha[0]))
    qtco.append(int(linha[1]))
    qtmin.append(int(linha[2]))
    linhaP = arqP.readline().strip()
arqP.close()  

arqD = open('divergencias.txt', 'w')


    