arqE = open('numeros.txt', 'r')
arqS = open('resultado.txt', 'w')

par = 0
impar = 0
qtde_par = 0
qtde_impar = 0

# Primeira leitura fora do loop
linha = arqE.readline().strip()

while linha != '':
    numero = int(linha)  # Converte a linha para número
    if numero % 2 == 0:
        par += numero
        qtde_par += 1
    else:
        impar += numero
        qtde_impar += 1
    
    # Lê a próxima linha
    linha = arqE.readline().strip()

# Escrita dos resultados no arquivo de saída
arqS.write(f"Soma dos números pares: {par}\n")
arqS.write(f"Quantidade de números pares: {qtde_par}\n")
arqS.write(f"Soma dos números ímpares: {impar}\n")
arqS.write(f"Quantidade de números ímpares: {qtde_impar}\n")

# Fechamento dos arquivos
arqS.close()
arqE.close()

print("Resultados gravados no arquivo 'resultado.txt'.")
