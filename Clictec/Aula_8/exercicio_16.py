# Lê o número N
N = int(input("Digite um número inteiro N: "))

# Inicializa a lista vazia
lista = []

# Loop para ler N números inteiros
for i in range(N):
    numero = int(input(f"Digite o elemento {i + 1}: "))
    # Verifica se o número já está na lista
    if numero in lista:
        print("Número já inserido, tente novamente.")  # Mensagem de aviso
    else:
        lista.append(numero)  # Adiciona o número à lista

# Exibe a lista resultante
print("Lista resultante:", lista)
