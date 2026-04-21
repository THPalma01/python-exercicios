# Aula 5 - Resolução do Exercício 2 da lista

Min = int(input("Digite o mínimo: "))
Max = int(input("Digite o máximo: "))
if Max <= Min:
    print("Valores Min e Max inválidos")
else:
    print("Divisíveis por 5 entre {} e {}".format(Min, Max))
    x = Min
    while x <= Max:
        if x % 5 == 0:
            print(x)
        x = x + 1

print("\n\nFim do Programa")
