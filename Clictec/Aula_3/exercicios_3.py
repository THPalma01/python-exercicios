import os 
os.system('cls')

#Escreva um programa que leia um número inteiro e informe se o mesmo é positivo, zero ou negativo.

l = int(input("Escreva um valor inteiro: "))

if l == 0:
    print("ZERO")
elif l > 0:
    print("POSITIVO")
elif l > 0:
    print("NEGATIVO")




#Escreva um programa que leia o nome de um lutador e seu peso. Em seguida informe a categoria a que pertence o lutador, conforme a
#tabela ao lado (note que a tabela foi criada para efeito deste exercício e não condiz com qualquer categoria de luta).

nome = input("Digite o nome do lutador: ")
peso = float(input("Digite o peso do lutador: "))

if peso < 65:
    categoria = "PENA"
elif 65 <= peso < 72:
    categoria = "LEVE"
elif 72 <= peso < 79:
    categoria = "LIGEIRO"
elif 79 <= peso < 86:
    categoria = "MEIO-MÉDIO"
elif 86 <= peso < 93:
    categoria = "MÉDIO"
elif 93 <= peso < 100:
    categoria = "MEIO-PESADO"
else:
    categoria = "PESADO"

print(f'O lutador {nome} pesa {peso} e se enquadra na categoria {categoria}')




#Escreva um programa que leia três números reais A, B e C que são os coeficientes de uma equação do 2º grau (A.x2 + B.x + C = 0).
#Calcule e apresente na tela as raízes dessa equação, considerando os três casos possíveis: Delta maior que zero (duas raízes reais), Delta igual a zero (uma raiz) e Delta menor que zero (não há raízes reais).


a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

delta = ((b**2) - 4 * a * c)

if delta < 0 or a == 0:
    print("Impossível calcular")
    print("Delta menor que 0 ou A é igual 0")
    print(delta)

elif delta == 0:
	x1 = (-b + delta ** (1/2))/(2*a)
	x2 = x1
	print(f'X1 = {x1:.5f}')
	print(f'X2 = {x2:.5f}')
    
else:
	x1 = (-b + delta **(1/2))/(2*a)
	x2 = (-b - delta **(1/2))/(2*a)
	print(f'X1 = {x1:.5f}')
	print(f'X2 = {x2:.5f}')
     

#Escreva um programa que leia três números reais e informe se eles constituem os lados de um triângulo. Em caso afirmativo, informe se o triângulo é equilátero, isósceles ou escaleno. Para que três números
#formem um triângulo deve ocorrer que a soma dos dois lados menores deve ser maior que o lado maior. Para resolver essa questão será preciso usar os operadores and e or. Colocar este programa no site do professor.


x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))
z = float(input("Valor de Z: "))

if (x + y > z) and (x + z > y) and (y + z > x):
    if x == y and x == z:
         print("TRIANGULO EQUILÁTERO")
    elif x == y or x == z or y == z:
         print("TRIANGULO ISÓSCELES")
    else:
         print("TRIANGULO ESCALENO")
else:
     print("NAO FORMAM UM TRIANGULO")

	