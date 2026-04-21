# Aula 5 - Resolução do Exercício 9 da lista

Arquivo = open("saidapgm09.txt", "w")

N = int(input("Digite N: "))
Arquivo.write("Sequência de Fibonacci\n")
Arquivo.write("Estes são os {} primeiros termos\n".format(N))
A = 0
B = 1
i = 0
while i < N:
    print(A)
    Arquivo.write("{}\n".format(A))
    C = A + B
    A = B
    B = C
    i += 1

Arquivo.close()


    
print("\n\nFim do Programa")
