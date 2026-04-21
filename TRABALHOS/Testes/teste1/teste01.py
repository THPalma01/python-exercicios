a = 0
par = 0
qtde_par = 0
impar = 0
qtde_impar = 0

# Coleta dos dados
while a >= 0:
    a = int(input("Digite o valor de a (negativo para sair): "))
    if a < 0:
        break
    if a % 2 == 0:
        par += a
        qtde_par += 1
    else:
        impar += a
        qtde_impar += 1


arq = open('resultado.txt', 'w')
arq.write(f"Soma dos números pares: {par}\n")
arq.write(f"Quantidade de números pares: {qtde_par}\n")
arq.write(f"Soma dos números ímpares: {impar}\n")
arq.write(f"Quantidade de números ímpares: {qtde_impar}\n")
arq.close()

print("Resultados gravados no arquivo 'resultado.txt'.")
