# Aula 5 - Resolução do Exercício 6 da lista

N = int(input("Digite N: "))
while N <= 100:
    print("Valor de N é inválido")
    N = int(input("Digite N: "))

# Cálculo da somatória - modo 1
Soma = 0
i = 1
while i <= N:
    if i % 2 == 0:
        Soma = Soma + i
    i = i + 1
print("Soma dos pares entre 1 e N (modo 1) = {}".format(Soma))    

# Cálculo da somatória - modo 2
Soma = 0
i = 2
while i <= N:
    Soma = Soma + i
    i = i + 2
print("Soma dos pares entre 1 e N (modo 2) = {}".format(Soma))    
    
print("\n\nFim do Programa")
