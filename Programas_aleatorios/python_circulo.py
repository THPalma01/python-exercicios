# Define o raio do círculo
raio = int(input("Digite o valor do raio: "))

# Percorre cada linha (y) da grade
for y in range(-raio, raio + 1):
    # Percorre cada coluna (x) da grade
    for x in range(-raio, raio + 1):
        # Verifica se o ponto (x, y) está dentro do círculo
        if x**2 + y**2 <= raio**2:
            print("*", end=" ")  # Desenha o ponto do círculo
        else:
            print(" ", end=" ")  # Desenha um espaço
    print()  # Muda de linha após completar uma linha do círculo
