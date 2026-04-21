# Lê os limites LMin e LMax
LMin = int(input("Digite o valor de LMin: "))
LMax = int(input("Digite o valor de LMax: "))

# Inverte LMin e LMax se LMax for menor que LMin
if LMax < LMin:
    LMin, LMax = LMax, LMin

# Lê o número N de valores a serem inseridos
N = int(input("Digite o número de valores que deseja inserir: "))

# Inicializa a lista A
A = []

# Lê N valores inteiros
for i in range(N):
    numero = int(input("Digite um número inteiro: "))
    
    # Adiciona o número à lista A se estiver no intervalo [LMin, LMax]
    if LMin <= numero <= LMax:
        A.append(numero)

# Exibe a lista A e seu tamanho
print("Lista A:", A)
print("Tamanho da lista A:", len(A))
