arqE = open('produto.txt', 'r')

linha = arqE.readline().strip()

VC = []
VB = []
VT = []
vlr = []
quant = []
tip = []

# Processamento do arquivo de entrada
while linha != '':
    linha = linha.split(';')
    tipo = linha[0]
    tip.append(tipo)

    valor = float(linha[1])
    vlr.append(valor)
    qtde = int(linha[2])
    quant.append(qtde)

    if tipo == 'C':
        vendas_camiseta = valor * qtde
        VC.append(vendas_camiseta)
    elif tipo == 'B':
        vendas_blusa = valor * qtde
        VB.append(vendas_blusa)
    elif tipo == 'T':
        vendas_tenis = valor * qtde
        VT.append(vendas_tenis)

    linha = arqE.readline().strip()

# Escrita no arquivo de saída
arqS = open('resultado.txt', 'w')
arqS.write(f'TIPO   VALOR    QUANTIDADE    FATURAMENTO\n')
arqS.write('\n')

# Corrigindo os loops para gravar os dados
for i in range(len(tip)):  # Itera pelos índices das listas
    faturamento = vlr[i] * quant[i]
    arqS.write(f'{tip[i]:<6} {vlr[i]:<8.2f} {quant[i]:<12} {faturamento:.2f}\n')

arqS.close()
arqE.close()
