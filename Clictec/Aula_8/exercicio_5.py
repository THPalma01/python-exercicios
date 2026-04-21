# Inicializa as listas
A = []
NEG = []
POS = []

# Lê um número N entre 0 e 50
N = int(input("Digite um número inteiro N (entre 0 e 50): "))

# Verifica se N está no intervalo correto
while N < 0 or N > 50:
    print("Entrada inválida! O número deve estar entre 0 e 50.")
    N = int(input("Digite um número inteiro N (entre 0 e 50): "))

# Lê N números reais e preenche a lista A
for i in range(N):
    numero = float(input("Digite um número real: "))
    A.append(numero)  # Adiciona o número à lista A

    # Separa os números em NEG e POS
    if numero < 0:
        NEG.append(numero)  # Adiciona à lista NEG
    else:
        POS.append(numero)  # Adiciona à lista POS

# Exibe as listas NEG e POS e a quantidade de valores
print("Lista de números negativos (NEG):", NEG)
print("Quantidade de negativos:", len(NEG))
print("Lista de números positivos e zero (POS):", POS)
print("Quantidade de positivos e zeros:", len(POS))
