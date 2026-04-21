#Escreva um programa que leia do teclado dois números inteiros nA e nB e leia também duas listas denominados A e B com os tamanhos nA e nB, respectivamente.
#Na leitura de cada uma das listas é obrigatório que não sejam aceitos valores repetidos.
#Em seguida, o programa deve juntar as duas listas em um única lista R (resultante) tomando o cuidado de que a lista R não deve ter valores duplicados.

# Lendo os tamanhos das listas A e B
nA = int(input("Digite o tamanho da lista A: "))
nB = int(input("Digite o tamanho da lista B: "))

# Preenchendo a lista A sem valores repetidos
A = []
print("Preencha a lista A (sem valores repetidos):")
for i in range(nA):
    numero = int(input(f"Digite o número {i + 1} para a lista A: "))

    # Verifica manualmente se o número já existe na lista A
    repetido = 0
    for j in range(len(A)):
        if A[j] == numero:
            repetido = 1
    
    if repetido == 0:
        A.append(numero)
    else:
        print("Valor repetido! Tente novamente.")
        i -= 1  # Retorna ao índice anterior para pedir um novo valor

# Preenchendo a lista B sem valores repetidos
B = []
print("Preencha a lista B (sem valores repetidos):")
for i in range(nB):
    numero = int(input(f"Digite o número {i + 1} para a lista B: "))

    # Verifica manualmente se o número já existe na lista B
    repetido = 0
    for j in range(len(B)):
        if B[j] == numero:
            repetido = 1
    
    if repetido == 0:
        B.append(numero)
    else:
        print("Valor repetido! Tente novamente.")
        i -= 1  # Retorna ao índice anterior para pedir um novo valor

# Juntando as listas A e B sem valores duplicados
R = []

# Adiciona todos os elementos de A na lista resultante R
for i in range(len(A)):
    R.append(A[i])

# Adiciona elementos de B em R, verificando se já estão em R
for i in range(len(B)):
    repetido = 0
    for j in range(len(R)):
        if R[j] == B[i]:
            repetido = 1
    
    if repetido == 0:
        R.append(B[i])

# Exibindo a lista resultante R
print("A lista resultante (sem valores duplicados) é:", R)
