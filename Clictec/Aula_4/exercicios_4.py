import os
os.system('cls')


# Escreva um programa que calcule os N primeiros termos de uma progressão geométrica (PG) com razão R e primeiro termo P fornecidos pelo usuário. Também deve ser calculada e apresentada a soma desses N termos.

# Entrada: N = 8 P = 2 e R = 3
# Saída: 2 6 18 54 162 486 1458 4374


n = int(input("Valor de N: "))
p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
cont = 0

while cont < n:
    print(p)
    p = p + r
    cont += 1


# Escreva um programa que leia valores numéricos inteiros e totalize (totalizar é somar todos os números) separadamente os positivos e os negativos até que o usuário digite 0. Ao final mostre na tela esses dois totais.
# Entrada: 12 -3 5 1 -4 -9 6 0

# Saída: Total dos positivos = 24
# Total dos negativos = -16

x = 1
pos = 0
neg = 0
while x != 0:
    x = int(input("Valor de X: "))
    if x % 2 == 0:
        pos = pos + x
    else:
        neg = neg + x

print(f'Total de positivos: {pos}')
print(f'Total de negativos: {neg}')


#Escreva um programa que leia um número inteiro M e em seguida leia M números reais, calculando a soma de todos os valores digitados.

m = int(input("Valor de M: "))
j = 0
soma = 0
while j < m:
    s = float(input("Valor de S: "))
    soma = soma + s
    j += 1
print(f'Resultado: {soma}')


#Escreva um programa que leia um número inteiro C e em seguida leia C números reais, calculando a soma de todos os valores positivos fornecidos, ignorando os negativos.


c = int(input("Valor de C: "))
t = 0
somapos = 0
while t < c:
    y = float(input("Valor de Y: "))
    if y < 0:
        t-=1
    else:
        somapos = somapos + y
    t+=1
   
print(f'Resultado: {somapos}')