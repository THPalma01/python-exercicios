Min = int(input("Digite o valor de Min (maior que 1): "))
if Min <= 1:
    Min = int(input("Min deve ser maior que 1! Digite novamente: "))

Max = int(input(f"Digite o valor de Max (maior que {Min}): "))
if Max <= Min:
    Max = int(input(f"Max deve ser maior que {Min}! Digite novamente: "))

primos = []

for numero in range(Min, Max + 1):
    eh_primo = True
    if numero < 2:
        eh_primo = False
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                eh_primo = False

    if eh_primo:
        primos.append(numero)

if len(primos) == 0:
    print(f"Não há primos no intervalo [{Min}, {Max}]")
else:
    for primo in primos:
        print(primo)
    
    print(f"Quantidade de primos no intervalo [{Min}, {Max}] = {len(primos)}")
    print(f"Soma dos primos no intervalo [{Min}, {Max}] = {sum(primos)}")
