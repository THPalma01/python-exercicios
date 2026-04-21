# Lê os limites LMin e LMax
LMin = int(input("Digite o valor de LMin: "))
LMax = int(input("Digite o valor de LMax: "))

# Inverte LMin e LMax se LMax for menor que LMin
if LMax < LMin:
    LMin, LMax = LMax, LMin

# Lê o número N de valores a serem inseridos
N = int(input("Digite o número de valores que deseja inserir: "))

# Inicializa as listas A e R
A = []  # Lista de valores aceitos
R = []  # Lista de valores rejeitados

# Lê N valores inteiros
for i in range(N):
    numero = int(input("Digite um número inteiro: "))
    
    # Verifica se o número está dentro do intervalo [LMin, LMax]
    if LMin <= numero <= LMax:
        A.append(numero)  # Adiciona à lista A se for válido
    else:
        R.append(numero)  # Adiciona à lista R se for inválido

# Exibe as listas A e R e o tamanho de cada uma
print("Lista de valores aceitos (A):", A)
print("Tamanho da lista A:", len(A))
print("Lista de valores rejeitados (R):", R)
print("Tamanho da lista R:", len(R))
