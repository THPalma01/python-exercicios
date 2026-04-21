# Inicializa duas listas vazias
lista1 = []
lista2 = []

# Lê 10 números inteiros para a primeira lista
print("Digite 10 números inteiros para a primeira lista:")
for i in range(10):
    numero = int(input(f"Elemento {i + 1}: "))
    lista1.append(numero)

# Lê 10 números inteiros para a segunda lista
print("Digite 10 números inteiros para a segunda lista:")
for i in range(10):
    numero = int(input(f"Elemento {i + 1}: "))
    lista2.append(numero)

# Junta as duas listas
lista_combinada = lista1 + lista2

# Exibe a lista combinada
print("Lista combinada:", lista_combinada)
