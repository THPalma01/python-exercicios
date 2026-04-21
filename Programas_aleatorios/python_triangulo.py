# Define a altura do triângulo
altura = int(input("Digite o valor da altura: "))

# Percorre cada linha do triângulo
for i in range(altura):
    # Imprime espaços para alinhar o triângulo
    print(" " * (altura - i - 1), end="")
    
    # Imprime os caracteres do triângulo
    print("* " * (i + 1))
