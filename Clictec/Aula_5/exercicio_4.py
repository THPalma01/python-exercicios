# Aula 5 - Resolução do Exercício 4 da lista

QtdeValidos = 0
N = int(input("Digite a quantidade de valores: "))
cont = 0
while cont < N:
    X = float(input("Digite o elemento {}: ".format(cont)))
    if X <= 0:
        print("   valor inválido")
    else:
        if QtdeValidos == 0 or X < CtrlMenor:
            CtrlMenor = X
        if QtdeValidos == 0 or X > CtrlMaior:
            CtrlMaior = X
        QtdeValidos += 1 # é o mesmo que QtdeValidos = QtdeValidos + 1
    cont = cont + 1

if QtdeValidos == 0:
    print("Não foram fornecidos valores válidos")
else:
    print("Foram fornecidos {} valores válidos e".format(QtdeValidos))
    print("  menor valor = {}".format(CtrlMenor))
    print("  maior valor = {}".format(CtrlMaior))

print("\n\nFim do Programa")
