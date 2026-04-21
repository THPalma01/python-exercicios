import random
import os
os.system('cls')

# Exibe as opções do jogo
print("Bem-vindo ao jogo Pedra, Papel, Tesoura!")
print("Escolha sua jogada:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

# Lê a jogada do jogador
jogada_jogador = int(input("Digite o número da sua jogada: "))

# Verifica se a jogada do jogador é válida
if jogada_jogador < 1 or jogada_jogador > 3:
    print("Jogada inválida! Por favor, escolha entre 1 e 3.")
else:
    # Escolha aleatória do computador
    jogada_computador = random.randint(1, 3)

    # Exibe a jogada do jogador
    if jogada_jogador == 1:
        print("Você jogou: Pedra")
    elif jogada_jogador == 2:
        print("Você jogou: Papel")
    elif jogada_jogador == 3:
        print("Você jogou: Tesoura")

    # Exibe a jogada do computador
    if jogada_computador == 1:
        print("O computador jogou: Pedra")
    elif jogada_computador == 2:
        print("O computador jogou: Papel")
    elif jogada_computador == 3:
        print("O computador jogou: Tesoura")

    # Define o resultado do jogo
    if jogada_jogador == jogada_computador:
        print("Empate!")
    elif (jogada_jogador == 1 and jogada_computador == 3) or \
         (jogada_jogador == 2 and jogada_computador == 1) or \
         (jogada_jogador == 3 and jogada_computador == 2):
        print("Você venceu!")
    else:
        print("O computador venceu!")
