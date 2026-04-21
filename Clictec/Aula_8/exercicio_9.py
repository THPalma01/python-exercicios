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

# Verifica se o valor X está na lista
if X in lista:
    print(f"O valor {X} está presente na lista.")
else:
    print(f"O valor {X} não está presente na lista.")
