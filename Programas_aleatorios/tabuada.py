# Solicita ao usuário para inserir os números
numero = int(input("Digite um número para gerar a tabuada: "))
multiplicador = int(input("Digite o valor do multiplicador: "))

# Exibe a tabuada do número de 1 até o número estabelecido pelo usuário
print(f"Tabuada do {numero}:")
for i in range(1, multiplicador + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
