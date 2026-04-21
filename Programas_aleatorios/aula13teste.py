def obtemlimites():
    a = int(input('Digite o menor valor: '))
    b = int(input('Digite o maior valor: '))
    while b < a:
        print('O valor maior deve ser maior que o valor menor.')
        print('Digite novamente.')
        b = int(input('Digite o maior valor: '))
    return a, b

def Eprimo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        raiz = n ** 0.5
        while i <= raiz:
            if n % i == 0:
                return False
            i += 2
        return True    

def carregarlistaprimos(ini, fim):
    lp = []
    candidato = ini
    while candidato <= fim:
        if Eprimo(candidato):
            lp.append(candidato)
        candidato += 1
    return lp

def Exibelista(lista):
    i = 0
    while i < len(lista):
        if i > 0 and i % 10 == 0:
            print()
        print(f'{lista[i]: 7}', end=' ')
        i += 1

def GravarArquivo(lista, arquivo):
    arq = open(arquivo, 'w')
    for valor in lista:
        arq.write(f'{valor}\n')
    arq.close()

# Parte principal do programa
lmin, lmax = obtemlimites()
print(f'\n\nDeterminado números primos entre {lmin} e {lmax}')
if len(primos) > 0:
    primos = carregarlistaprimos(lmin, lmax)
    Exibelista(primos)
    print('\n\Estes dados serão gravados em um arquivo ')
    nomeArq = input(' Digite um nme para o arquivo')
    GravarArquivo(primos, nomeArq)
else:

print("\nFim do programa")
