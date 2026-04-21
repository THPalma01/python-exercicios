Min = int(input("Digite o valor de Min: "))
Max = int(input("Digite o valor de Max: "))

if Max <= Min + 100:
    print("Intervalo inválido. Max deve ser maior que Min + 100.")
else:
    print("Pense em um número entre", Min, "e", Max, ". O computador vai tentar adivinhar.")
    palpites = []
    tentativas = 0
    menor = Min
    maior = Max
    acertou = 0

    while acertou == 0:
        palpite = (menor + maior) // 2
        print("Palpite", tentativas + 1, ":", palpite)
        palpites.append(palpite)
        tentativas = tentativas + 1
        resposta = int(input("Digite 1 se acertou, 0 se errou: "))
        if resposta == 1:
            print("Acertou!!!")
            acertou = 1
        else:
            dica = int(input("Digite 8 se o número é menor, 9 se o número é maior: "))
            if dica == 8:
                maior = palpite - 1
            elif dica == 9:
                menor = palpite + 1

    print("foram", tentativas, "palpites até acertar")
    print("e os palpites foram esses:", end=" ")
    i = 0
    while i < len(palpites):
        print(palpites[i], end="")
        if i < len(palpites) - 1:
            print(", ", end="")
        i = i + 1
    print()