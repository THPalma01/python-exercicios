# Aula 5 - Resolução do Exercício 5 da lista

A = int(input("Digite A: "))
while A != 0:
    if A % 2 == 0 and A % 3 == 0:    # também é possível usar isto -> if A % 6 == 0:
        print("  {} é divisível por 2 e por 3".format(A))
    A = int(input("Digite A: "))

print("\n\nFim do Programa")
