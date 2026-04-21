
import os
import random
os.system('cls')


jogo = True

while jogo == True:
    os.system('cls')
    game = True
    vidas = 0
    palpite = []

    nivel = int(input("Digite o nivel da dificuldade: 1/2/3 "))
    if nivel == 1:
        vidas = 7
    elif nivel == 2:
        vidas = 5
    elif nivel == 3:
        vidas = 3
    else:
        print("Valor inválido")

    x, y = input("Digite o valor mínimo e máximo: ").split()
    x = int(x)
    y = int(y)

    if x > y:
        troca = x
        x = y
        y = troca
    
    numero = random.randint(x, y)
  
    while game == True:
        tentativa = int(input("Informe seu palpite: "))
        if tentativa != numero:
            print("Voce errou!!!")
            if tentativa > numero:
                print("O número é menor")
            else:
                print("O número é maior")
            vidas -= 1
            palpite.append(tentativa)
        else:
            print("Voce acertou!!!")
            game = False
        if vidas == 0:
            print("Suas vidas acabaram ")
            game = False

    print(f"Seus palpites: {palpite}")
    print(f"Número correto: {numero}")

    resp = input("Deseja jogar novamente? (S/N): ")
    if resp == 's' or resp == 'S':
        jogo = True
    else:
        jogo = False

        



