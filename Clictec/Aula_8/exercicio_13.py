# Função para verificar se um número é primo
def eh_primo(num):
    if num < 2:  # Números menores que 2 não são primos
        return False
    for i in range(2, int(num**0.5) + 1):  # Verifica divisores até a raiz quadrada do número
        if num % i == 0:  # Se divisível por algum número, não é primo
            return False
    return True

# Lê o número N
N = int(input("Digite um número inteiro N: "))

# Inicializa a lista para armazenar os números primos
primos = []
contador = 0  # Contador de números primos encontrados
numero_atual = 2  # Começa a verificar a partir do primeiro número primo

# Loop para encontrar os N primeiros números primos
while contador < N:
    if eh_primo(numero_atual):  # Verifica se o número atual é primo
        primos.append(numero_atual)  # Adiciona à lista de primos
        contador += 1  # Incrementa o contador
    numero_atual += 1  # Verifica o próximo número

# Exibe a lista de números primos
print("Os primeiros", N, "números primos são:", primos)
