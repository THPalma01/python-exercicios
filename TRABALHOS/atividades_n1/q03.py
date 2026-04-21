Min = int(input("Digite o valor minimo: "))
Max = int(input("Digite o valor maximo: "))

if Min <= 1 or Max <= Min:
    print("Valores inválidos")
else:
    primo = Min
    contagem = 0
    soma = 0

    while primo <= Max:
        if primo == 2:
            print(primo)
            contagem = contagem + 1
            soma = soma + primo
        elif primo > 2:
            divisor = 2
            eh_primo = 1
            while divisor <= primo - 1:
                if primo % divisor == 0:
                    eh_primo = 0
                divisor = divisor + 1
            if eh_primo == 1:
                print(primo)
                contagem = contagem + 1
                soma = soma + primo
        primo = primo + 1

    if contagem > 0:
        print("Quantidade de primos no intervalo [" + str(Min) + ", " + str(Max) + "] = " + str(contagem))
        print("Soma dos primos no intervalo [" + str(Min) + ", " + str(Max) + "] = " + str(soma))
    else:
        print("Não há primos no intervalo [" + str(Min) + ", " + str(Max) + "]")