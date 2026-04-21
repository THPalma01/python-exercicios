# Inicializa a lista A
A = []

# Solicita um número N entre 0 e 50
N = int(input("Digite um número inteiro N (entre 0 e 50): "))

# Valida a entrada de N
while N < 0 or N > 50:
    print("Entrada inválida! O número deve estar entre 0 e 50.")
    N = int(input("Digite um número inteiro N (entre 0 e 50): "))

# Lê N números reais do teclado
i = 0
while i < N:
    numero = float(input(f"Digite o número real {i + 1}: "))
    A.append(numero)  # Adiciona o número real à lista
    i += 1  # Incrementa o contador

# Exibe os elementos da lista A, um por linha
for numero in A:
    print(numero)
