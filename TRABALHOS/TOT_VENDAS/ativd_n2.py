from operator import itemgetter

arqS = open('totvendas.txt', 'w')

# parte 1
arqVen = open('vendas.txt', 'r')
arqS.write('TOTAIS DE VENDAS POR DIA\n')
arqS.write('Dia             Total  Média/Dia\n')
linha = arqVen.readline().rstrip()
ano = ''
diasUteis = 0
while linha != '':
    linha = linha.split(';')
    if ano == '':
        ano = str(linha[0])
        mes = str(linha[1])
        dia = linha[2]
        total = float(linha[5])
        qtde = 1
    else:
        if linha[0] == ano and linha[1] == mes and linha[2] == dia:
            total += float(linha[5])
            qtde += 1
        else:
            if len(dia) == 1:
                dia = '0' + dia
            if len(mes) == 1:
                mes = '0' + mes
            media = total/qtde
            total = f'{total:.2f}'
            media = f'{media:.2f}'
            arqS.write(f'{dia}/{mes}/{ano} {total:>10} {media:>10}\n')
            diasUteis += 1
            ano = ''
    linha = arqVen.readline().rstrip()
    
arqS.write('\n')

arqVen.close()

# parte 2
arqS.write('TOTAIS DE VENDAS POR PRODUTO\n')
arqS.write('Prod.     VlrTot     Qtde  Pç Médio  Lucrat.\n')
arqProd = open('produtos.txt', 'r')
arqVen = open('vendas.txt' , 'r')
codigo = []
tipo = []
preco_custo = []
vlrtotal = {}
qtdes = {}
lucrat = {}
linhaP = arqProd.readline().rstrip()
while linhaP != '':
    linhaP = linhaP.split(';')
    codigo.append(int(linhaP[0]))
    tipo.append(linhaP[1])
    preco_custo.append(float(linhaP[3]))
    linhaP = arqProd.readline().rstrip()
arqProd.close()

linhaV = arqVen.readline().rstrip()
while linhaV != '':
    linhaV = linhaV.split(';')

    for j in codigo:
        if int(linhaV[3]) == j:
            if j in qtdes.keys():
                qtde = qtdes[j]
                qtdes[j] = float(qtde) + float(linhaV[4])
            else:
                qtdes[j] = float(linhaV[4])

    for i in codigo: 
        if int(linhaV[3]) == i:
            if i in vlrtotal.keys(): # se o código já existe no dicionário
                vlr = vlrtotal[i]
                vlrtotal[i] = float(vlr) + float(linhaV[5]) * float(linhaV[4])
            else:
                vlrtotal[i] = float(linhaV[5]) * float(linhaV[4])
    linhaV = arqVen.readline().rstrip()

final = len(codigo)
cont = 0
totalgeral = 0
qtdegeral = 0
lucrgeral = 0
parte5 = {}
while cont < final:
    pcmedio = f'{vlrtotal[codigo[cont]] / qtdes[codigo[cont]]:.2f}'
    valor = f'{vlrtotal[codigo[cont]]:.2f}'
    if tipo[cont] == 'P':
        qtd = f'{qtdes[codigo[cont]]:.2f}'
    else:
        qtd = f'{int(qtdes[codigo[cont]])}'
    lucr = f'{((vlrtotal[codigo[cont]] / qtdes[codigo[cont]]) / preco_custo[cont] - 1) * 100:.1f}'
    totalgeral += vlrtotal[codigo[cont]]
    qtdegeral += qtdes[codigo[cont]]
    lucrat[codigo[cont]] = float(lucr)
    lucrgeral += (float(lucr)/100) * float(qtdes[codigo[cont]])
    parte5[codigo[cont]] = float(valor)
    arqS.write(f'{codigo[cont]} {valor:>10} {qtd:>8} {pcmedio:>9} {lucr:>7}%\n')
    cont += 1
arqVen.close()

arqS.write('\n')

# parte 3
lucrgeral = f'{(  (float(lucrgeral) / float(qtdegeral)) * 100  ):.1f}'
mediaPorDia = f'{(totalgeral / diasUteis):.2f}'
mediaPorQtde = f'{(totalgeral / qtdegeral):.2f}'
total_pt5 = totalgeral
totalgeral = f'{totalgeral:.2f}'
qtdegeral = f'{qtdegeral:.2f}'
arqS.write('TOTAL E ESTATÍSTICAS DO PERÍODO\n')
arqS.write(f'Total Geral de Vendas (R$) {totalgeral:>16}\n')
arqS.write(f'Quantidade de produtos vendidos {qtdegeral:>11}\n')
arqS.write(f'Média de Vendas por dia útil (R$) {mediaPorDia:>9}\n')
arqS.write(f'Média de Vendas por produto (R$) {mediaPorQtde:>10}\n')
arqS.write(f'Lucratividade Média {lucrgeral:>22}%\n')

arqS.write('\n')

# parte 4
arqS.write('PRODUTOS MAIS LUCRATIVOS\n')
arqS.write(f'Lucratividade Média = {lucrgeral}%\n')
arqS.write('\n')
arqS.write('Prod.   Lucrat.\n')

for cod, lucro in sorted(lucrat.items(), key = itemgetter(1), reverse = True):
    arqS.write(f'{cod} {lucro:>8}%\n')

arqS.write('\n')

# parte 5
arqS.write('CONTRIBUIÇÃO DE CADA PRODUTO\n')
arqS.write('Prod.     VlrTot  Contrib.\n')
parte5_2 = {}
cont = 0
for i in codigo:
    vendas = parte5[i]
    parte5_2[i] = (vendas / total_pt5) * 100


for codigo, contr in sorted(parte5_2.items(), key = itemgetter(1), reverse = True):
    contr = f'{contr:.1f}'
    arqS.write(f'{codigo} {parte5[codigo]:>10} {contr:>7}%\n')
arqS.close()

