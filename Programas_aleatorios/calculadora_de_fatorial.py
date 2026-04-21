# Solicita ao usuário para inserir um número
numero = int(input("Digite um número para calcular o fatorial: "))

# Inicializa a variável que armazenará o fatorial
fatorial = 1

# Calcula o fatorial usando um loop
for i in range(1, numero + 1):
    fatorial *= i

# Exibe o resultado
print(f"O fatorial de {numero} é {fatorial}")
