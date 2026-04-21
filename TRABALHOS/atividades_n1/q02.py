entrada = input("Digite N (ímpar, 5 <= N <= 49): ")
n = int(entrada)

if n < 5 or n > 49 or n % 2 == 0:
    print(f"O número {n} é inválido")
else:
    for num_asteriscos in range(1, n + 1, 2):
        espacos_folhas = (n - num_asteriscos) // 2
        print(" " * espacos_folhas + "*" * num_asteriscos)

    espacos_tronco = (n - 1) // 2
    print(" " * espacos_tronco + "|")

    espacos_base = (n - 3) // 2
    print(" " * espacos_base + "---")