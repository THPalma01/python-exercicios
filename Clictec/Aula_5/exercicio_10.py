# Aula 5 - Resolução do Exercício 10 da lista

N = int(input("Digite N: "))
Prim = int(input("Digite Prim: "))
A = 0
B = 1
i = 0
while i < N:
    if A > Prim:
        print(A)
        i += 1
    C = A + B
    A = B
    B = C

    
print("\n\nFim do Programa")
