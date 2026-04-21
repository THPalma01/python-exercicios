# Aula 5 - Resolução do Exercício 3 da lista

N = int(input("Digite a quantidade de valores: "))
cont = 0
while cont < N:
    X = float(input("Digite o elemento {}: ".format(cont)))
    if cont == 0 or X < CtrlMenor:
        CtrlMenor = X
    if cont == 0 or X > CtrlMaior:
        CtrlMaior = X
    cont = cont + 1

if N <= 0:
    print("Não há valores")
else:    
    print("Menor valor = {}".format(CtrlMenor))
    print("Maior valor = {}".format(CtrlMaior))

print("\n\nFim do Programa")
