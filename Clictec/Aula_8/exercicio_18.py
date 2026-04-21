# Lê o valor de Min
Min = int(input("Digite o valor de Min: "))

# Lê o valor de Max e garante que seja maior que Min
Max = int(input("Digite o valor de Max (deve ser maior que Min): "))
while Max <= Min:
    print("O valor de Max deve ser maior que Min. Tente novamente.")
    Max = int(input("Digite o valor de Max (deve ser maior que Min): "))

# Inicializa a lista para armazenar os números divisíveis por 7
lista = []

# Preenche a lista com valores entre Min e Max que são divisíveis por 7
for i in range(Min, Max + 1):  # +1 para incluir Max
    if i % 7 == 0:  # Verifica se o número é divisível por 7
        lista.append(i)  # Adiciona à lista

# Exibe a lista resultante
print("Lista de números entre", Min, "e", Max, "que são divisíveis por 7:", lista)
