# Lê o número N
N = int(input("Digite um número inteiro N: "))

# Inicializa a lista
lista = []

# Preenche a lista com N elementos digitados pelo usuário
for i in range(N):
    numero = int(input(f"Digite o elemento {i + 1}: "))
    lista.append(numero)  # Adiciona o número à lista

# Exibe a lista preenchida
print("Lista preenchida:", lista)

# Inicializa uma nova lista para armazenar os valores únicos
lista_unica = []

# Procura e elimina os elementos repetidos
for numero in lista:
    if numero not in lista_unica:  # Verifica se o número já está na lista única
        lista_unica.append(numero)  # Adiciona à lista única se não estiver presente

# Exibe a lista resultante sem duplicatas
print("Lista resultante sem duplicatas:", lista_unica)

