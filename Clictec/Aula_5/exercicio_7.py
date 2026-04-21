# Aula 5 - Resolução do Exercício 7 da lista

Soma = Qtde = 0
A = int(input("Digite um valor: "))
CtrlMenor = CtrlMaior = A
while A > 0:
    Soma = Soma + A
    Qtde += 1
    if A < CtrlMenor:
        CtrlMenor = A
    if A > CtrlMaior:
        CtrlMaior = A

    A = int(input("Digite um valor: "))

if Qtde > 0:
    print("Soma = {}".format(Soma))
    print("Qtde = {}".format(Qtde))
    print("Média = {}".format(Soma/Qtde))
    print("Menor valor = {}".format(CtrlMenor))
    print("Maior valor = {}".format(CtrlMaior))
    
    Arq = open("saidapgm07.txt", "w")
    Arq.write("Soma = {}\n".format(Soma))
    Arq.write("Qtde = {}\n".format(Qtde))
    Arq.write("Média = {}\n".format(Soma/Qtde))
    Arq.write("Menor valor = {}\n".format(CtrlMenor))
    Arq.write("Maior valor = {}\n".format(CtrlMaior))
    Arq.close()
else:
    print("Não fornecidos valores")

    
print("\n\nFim do Programa")
