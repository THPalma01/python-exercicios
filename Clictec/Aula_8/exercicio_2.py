# Inicializa uma lista vazia
lista = []

# Lê 10 elementos do teclado
for i in range(10):
    elemento = input(f"Digite o elemento {i + 1}: ")
    lista.append(elemento)

# Exibe os elementos na ordem inversa, um por linha
for elemento in reversed(lista):
    print(elemento)
