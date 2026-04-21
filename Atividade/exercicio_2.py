import os
os.system('cls')

print("EXERCÍCIO 2")
print("RHIAN OLIVEIRA DANTAS")
print()
n = int(input("DIGITE UM NUMERO PAR ENTRE 6 E 32: "))

while n % 2 != 0 or n > 32 or n < 6:
    print(f'O número {n} é inválido')
    n = int(input("DIGITE UM NUMERO PAR ENTRE 6 E 32:"))

print(" "+"*" * (n-2) + " ")
print("*" * n)

for i in range ((n-4)):
    print("**"+" "*(n-4)+"**")

print('*' * n)
print(" "+"*" *(n-2)+" ")