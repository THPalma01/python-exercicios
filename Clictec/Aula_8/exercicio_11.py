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
X = int(input("Digite um valor X para eliminar da lista: "))

# Elimina todas as ocorrências de X na lista
i = 0  # Inicializa o índice
while i < len(lista):  # Enquanto o índice for menor que o tamanho da lista
    if lista[i] == X:  # Verifica se o elemento é igual a X
        del lista[i]  # Elimina o elemento
        # Não incrementa o índice, pois os elementos seguintes foram deslocados
    else:
        i += 1  # Somente incrementa o índice se não houve eliminação

# Exibe a lista após a remoção
print("Lista após a remoção de X:", lista)
