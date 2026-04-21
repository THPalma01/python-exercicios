# Exibe o menu de operações
print("Bem-vindo à calculadora simples!")
print("Escolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Lê a operação escolhida pelo usuário
operacao = int(input("Digite o número da operação desejada: "))

# Lê os dois números para realizar a operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação escolhida
if operacao == 1:
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
    
elif operacao == 2:
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
    
elif operacao == 3:
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
    
elif operacao == 4:
    # Verifica se o segundo número é diferente de zero para evitar divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida!")
else:
    print("Operação inválida! Escolha entre 1 e 4.")
