# Define a largura e a altura do retângulo
largura = int(input("Digite o valor da largura: "))
altura = int(input("Digite o valor da altura: "))

# Percorre cada linha do retângulo
for i in range(altura):
    # Percorre cada coluna do retângulo
    for j in range(largura):
        # Desenha o contorno do retângulo
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            print("*", end=" ")  # Imprime o caractere do retângulo
        else:
            print(" ", end=" ")  # Imprime um espaço para o interior
    print()  # Muda de linha após completar uma linha do retângulo
