# Aula 7 - Conceito de listas - exemplo 2
L = []
X = int(input('Digite um inteiro: '))
while X > 0:
    L.append(X)
    X = int(input('Digite um inteiro: '))

print('\nElementos da Lista - exibição com while')
i = 0
while i < len(L):
    print(L[i])
    i += 1

print('\nElementos da Lista - exibição com for')
for item in L:
    print(item)
    
print('\nElementos da Lista - exibição com for e uso de índice')
for i in range(len(L)):
    print(L[i])

print("\n\nFim do Programa")
