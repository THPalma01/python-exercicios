# Aula 5 - Resolução do Exercício 1 da lista

N = int(input("Digite N: "))
i = 1
while i <= 10:
    print("{} x {} = {}".format(N, i, N*i)) # é o mesmo que print(f"{N} x {i} = {N*i}")
    i = i + 1

print("\n\nFim do Programa")
