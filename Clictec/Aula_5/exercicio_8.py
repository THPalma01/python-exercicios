# Aula 5 - Resolução do Exercício 8 da lista

N = int(input("Digite um valor: "))
cont = 0
i = 2
while i < N:
    if N % i == 0:
        cont += 1
    i += 1

if cont > 0:
    print("{} não é primo".format(N))
else:
    print("{} é primo".format(N))

    
print("\n\nFim do Programa")
