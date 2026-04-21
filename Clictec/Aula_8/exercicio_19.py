# Inicializa a lista vazia
lista = []

while True:  # Laço infinito
    # Lê um valor do usuário
    valor = int(input("Digite um valor positivo (ou um valor menor ou igual a zero para sair): "))
    
    if valor <= 0:  # Condição para sair do laço
        break  # Sai do loop se o valor for menor ou igual a zero
    
    # Encontra a posição onde o valor deve ser inserido
    posicao = 0
    while posicao < len(lista) and lista[posicao] < valor:
        posicao += 1  # Incrementa a posição enquanto o valor na lista for menor que o valor digitado
    
    # Insere o valor na posição encontrada
    lista.insert(posicao, valor)

# Exibe a lista resultante
print("Lista ordenada:", lista)
