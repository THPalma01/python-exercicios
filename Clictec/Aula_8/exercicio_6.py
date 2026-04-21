# Lê os limites LMin e LMax
LMin = int(input("Digite o valor de LMin: "))
LMax = int(input("Digite o valor de LMax: "))

# Inverte LMin e LMax se LMax for menor que LMin
if LMax < LMin:
    LMin, LMax = LMax, LMin

# Inicializa a lista A
A = []

# Lê 10 valores inteiros
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    
    # Adiciona o número à lista A se estiver no intervalo [LMin, LMax]
    if LMin <= numero <= LMax:
        A.append(numero)

# Exibe a lista A e seu tamanho
print("Lista A:", A)
print("Tamanho da lista A:", len(A))
