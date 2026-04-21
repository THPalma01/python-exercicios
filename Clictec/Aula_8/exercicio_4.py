import random  # Importa a biblioteca random

# Lê um número N entre 0 e 50
N = int(input("Digite um número inteiro N (entre 0 e 50): "))

# Verifica se N está no intervalo correto
while N < 0 or N > 50:
    print("Entrada inválida! O número deve estar entre 0 e 50.")
    N = int(input("Digite um número inteiro N (entre 0 e 50): "))

# Inicializa a lista A
A = []

# Preenche a lista com N números aleatórios entre 0 e 1000
for i in range(N):
    numero = random.randint(0, 1000)  # Gera um número aleatório entre 0 e 1000
    A.append(numero)  # Adiciona o número à lista

# Exibe os números da lista A, um por linha
for numero in 
