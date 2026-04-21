# Aula 7 - Conceito de listas - exemplo 3
L = []
cont = 0
while cont < 10:
    X = int(input('Digite um inteiro: '))
    L.append(X)
    cont += 1

# inverte e exibe
print('\nExibição da lista inteira após usar .reverse()')
L.reverse()
print(L)

# inverte novamente - volta ao original
L.reverse()
#   e exibe usando contagem regressiva
print('\nElementos da Lista - exibição com while em contagem regressiva')
i = 9
while i >= 0:
    print(L[i])
    i -= 1
    
print("\n\nFim do Programa")
