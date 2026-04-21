# Solicita ao usuário o valor inicial, a taxa de juros e o tempo
valor_inicial = float(input("Digite o valor inicial (capital): "))
taxa_juros = float(input("Digite a taxa de juros (em %): ")) / 100  # Converte para decimal
tempo = int(input("Digite o tempo (em anos): "))

# Calcula o montante final usando a fórmula dos juros compostos
montante = valor_inicial * (1 + taxa_juros) ** tempo

# Exibe o resultado
print(f"\nValor inicial: R$ {valor_inicial:.2f}")
print(f"Taxa de juros: {taxa_juros * 100:.2f}%")
print(f"Tempo: {tempo} anos")
print(f"Montante final após {tempo} anos: R$ {montante:.2f}")
