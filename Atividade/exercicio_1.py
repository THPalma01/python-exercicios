import os
import random
os.system('cls')

print("EXERCÍCIO 1")
print("RHIAN OLIVEIRA DANTAS")
print()
lmin = int(input())
lmax = int(input())
palpite = []
tentativas = 0
x = 0
if lmin + 100 > lmax:
    print("O valor máximo deve ser maior que o valor mínimo + 100. Tente novamente")
else:
    if lmin == 0:
        lmin += 1
    sorte = random.randint(lmin, lmax)

    while x != sorte:
        x = int(input("DIGITE UM NUMERO:"))
        palpite.append(x)
        tentativas += 1
        if x != sorte:
            print("Errado")
            if x > sorte:
                print("O numero é menor")
            else:
                print("O número é maior")
        if x == sorte:
            print("ACERTOU")
            print(F'SEUS PALPITES FORAM: {palpite}')
            print(f'TENTATIVAS: {tentativas}')