#Escreva um programa que preencha com números inteiros duas listas denominadas A e B com diferentes tamanhos nA e nB, respectivamente.
#Em seguida o programa deve juntar as duas listas em uma única lista com o tamanho nA+nB. Exibir na tela a lista resultante.

# Definindo os tamanhos das listas A e B
nA = int(input("Digite o tamanho da lista A: "))
nB = int(input("Digite o tamanho da lista B: "))

# Preenchendo a lista A
A = []
for i in range(nA):
    numero = int(input(f"Digite o número {i + 1} para a lista A: "))
    A.append(numero)

# Preenchendo a lista B
B = []
for i in range(nB):
    numero = int(input(f"Digite o número {i + 1} para a lista B: "))
    B.append(numero)

# Juntando as duas listas
lista_resultante = A + B

# Exibindo a lista resultante
print("A lista resultante é:", lista_resultante)
