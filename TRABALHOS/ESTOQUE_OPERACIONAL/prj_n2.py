arq = input('\n>> Digite o prefixo desejado: ')

arqProd = open(f'{arq}produtos.txt', 'r')
codigo = []
qtdeCO = []
qtdeMin = []
linha = arqProd.readline().rstrip()
while linha != '':
    linha = linha.split(';')
    codigo.append(int(linha[0]))
    qtdeCO.append(int(linha[1]))
    qtdeMin.append(int(linha[2]))
    linha = arqProd.readline().rstrip()
arqProd.close()

arqVen = open(f'{arq}vendas.txt', 'r')
arqDiv = open(f'{arq}divergencias.txt', 'w')
LL = 1 # linha
tot1 = 0
tot2 = 0
tot3 = 0
tot4 = 0
dados = {}
linha = arqVen.readline().rstrip()
while linha != '':
    linha = linha.split(';')
    if int(linha[0]) not in codigo: # se o código não constar no arquivo de produto
        arqDiv.write(f'Linha {LL} - Código de Produto não encontrado {int(linha[0])}\n')
    else:
        if int(linha[2]) == 135: 
            arqDiv.write(f'Linha {LL} - Venda cancelada\n')
        if int(linha[2]) == 190:
            arqDiv.write(f'Linha {LL} - Venda não finalizada\n')
        if int(linha[2]) == 999:
            arqDiv.write(f'Linha {LL} - Erro desconhecido. Acionar equipe de TI\n')
        if int(linha[2]) == 100: 
            if int(linha[3]) == 1:
                tot1 += int(linha[1])
            elif int(linha[3]) == 2:
                tot2 += int(linha[1])
            elif int(linha[3]) == 3:
                tot3 += int(linha[1])
            elif int(linha[3]) == 4:
                tot4 += int(linha[1])
        if int(linha[2]) == 102:
            if int(linha[3]) == 1:
                tot1 += int(linha[1])
            elif int(linha[3]) == 2:
                tot2 += int(linha[1])
            elif int(linha[3]) == 3:
                tot3 += int(linha[1])
            elif int(linha[3]) == 4:
                tot4 += int(linha[1])
        if int(linha[2]) == 100 or int(linha[2]) == 102:
            for i in codigo: 
                if int(linha[0]) == i:
                    if i in dados.keys(): # se o código já existir no dicionário
                        qtde = dados[i]
                        dados[i] = qtde + int(linha[1])
                    else:
                        dados[i] = int(linha[1])
    LL += 1
    linha = arqVen.readline().rstrip()
arqDiv.close()
arqVen.close()


arqTr = open(f'{arq}transfere.txt', 'w')
arqTr.write('Necessidade de Transferência Armazém para CO\n\n')
arqTr.write('Produto  QtCO  QtMin  QtVendas  Estq.após  Necess.  Transf. de\n')
arqTr.write('                                   Vendas            Arm p/ CO\n')

final = len(codigo)
cont = 0
while cont < final:
    if (qtdeCO[cont]-dados[codigo[cont]]) < qtdeMin[cont]:
        necess = qtdeMin[cont] - (qtdeCO[cont]-dados[codigo[cont]])
    else:
        necess = 0
    if necess > 1 and necess < 10:
        transf = 10
    else:
        transf = necess
    arqTr.write(f'{codigo[cont]}' # produto
                f'{qtdeCO[cont]:8}' # qtCO
                f'{qtdeMin[cont]:7}' # qtMin
                f'{dados[codigo[cont]]:10}' # qtVendas
                f'{qtdeCO[cont]-dados[codigo[cont]]:11}' # estoq
                f'{necess:9}' # necess
                f'{transf:12}\n') # transf de arm
    cont += 1
    
arqTr.close()


arqTot = open(f'{arq}totcanal.txt', 'w')
arqTot.write('Quantidades de Vendas por canal\n\n')
arqTot.write('Canal                  QtVendas\n')
arqTot.write(f'1 - Representantes    {tot1:9}\n')
arqTot.write(f'2 - Website           {tot2:9}\n')
arqTot.write(f'3 - App móvel Android {tot3:9}\n')
arqTot.write(f'4 - App móvel iPhone  {tot4:9}\n')
arqTot.close()
