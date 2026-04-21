# Define o tamanho do quadrado
tamanho = int(input("Digite o valor do tamanho: "))

# Percorre cada linha do quadrado
for i in range(tamanho):
    # Percorre cada coluna do quadrado
    for j in range(tamanho):
        # Desenha o contorno do quadrado
        if i == 0 or i == tamanho - 1 or j == 0 or j == tamanho - 1:
            print("*", end=" ")  # Imprime o caractere do quadrado
        else:
            print(" ", end=" ")  # Imprime um espaço para o interior
    print()  # Muda de linha após completar uma linha do quadrado
