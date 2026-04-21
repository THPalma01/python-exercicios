import random  # Importa a biblioteca random

# Lê o número N
N = int(input("Digite um número inteiro N: "))

# Inicializa a lista com N números aleatórios entre 0 e 1000
lista = []
for i in range(N):
    numero = random.randint(0, 1000)  # Gera um número aleatório
    lista.append(numero)  # Adiciona o número à lista

# Exibe a lista gerada
print("Lista gerada:", lista)

# Lê o valor X
X = int(input("Digite um valor X para verificar se está na lista: "))

# Verifica a presença de X e armazena as posições
posicoes = []  # Lista para armazenar as posições de X
for i in range(N):
    if lista[i] == X:  # Compara cada elemento da lista com X
        posicoes.append(i)  # Adiciona a posição à lista de posições

# Exibe o resultado
if len(posicoes) > 0:
    print(f"O valor {X} está presente na lista nas posições: {posicoes}")
else:
    print(f"O valor {X} não está presente na lista.")
