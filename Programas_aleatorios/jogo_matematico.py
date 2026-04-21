import random

# Inicializa as variáveis
numero_tentativas = 0
tentativas_usuario = []
operacao = random.choice(['+', '-', '*', '/'])

# Gera os números aleatórios
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Para evitar divisão por zero
if operacao == '/':
    num1 *= num2  # Faz num1 múltiplo de num2 para que a divisão seja exata

# Mostra a pergunta ao usuário
print(f"Calcule: {num1} {operacao} {num2}")

# Inicializa o estado do jogo
acertou = 0  # 0 representa que ainda não acertou
resultado_correto = 0

# Calcula o resultado correto com base na operação
if operacao == '+':
    resultado_correto = num1 + num2
elif operacao == '-':
    resultado_correto = num1 - num2
elif operacao == '*':
    resultado_correto = num1 * num2
elif operacao == '/':
    resultado_correto = num1 / num2

# Loop do jogo
while acertou == 0:
    # Solicita a resposta do usuário
    resposta_usuario = float(input("Digite sua resposta: "))
    numero_tentativas += 1
    tentativas_usuario.append(resposta_usuario)

    # Verifica a resposta
    if resposta_usuario == resultado_correto:
        acertou = 1  # Muda para 1 quando o usuário acerta
        print(f"Você acertou! O resultado é {resultado_correto}.")
    else:
        print("Errado! Tente novamente.")

# Exibe o número de tentativas e as tentativas do usuário
print(f"Número de tentativas: {numero_tentativas}")
print("Suas tentativas:", tentativas_usuario)
print(f"Resultado correto: {resultado_correto}")
