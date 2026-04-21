import os
os.system('cls')

infantil = []
feminina = []
masculina = []
erros = []
cod = 1


while cod != 0:
    
    cod = int(input("Digite o código do produto: "))

    if cod >= 1000000 and cod <= 3990000:
        qtde_infantil = int(input("Digite a quantidade vendida: "))
        vlr_infantil = float(input("Digite o valor do produto: "))
        venda_infantil = qtde_infantil * vlr_infantil
        infantil.append(venda_infantil) 

    if cod >= 4000000 and cod <= 7990000:
            qtde_feminina = int(input("Digite a quantidade vendida: "))
            vlr_feminina = float(input("Digite o valor do produto: "))
            venda_feminina = qtde_feminina * vlr_feminina
            feminina.append(venda_feminina)
    if cod >= 8000000 and cod <= 9990000:
        qtde_masculina = int(input("Digite a quantidade vendida: "))
        vlr_masculina= float(input("Digite o valor do produto: "))
        venda_masculina = qtde_masculina * vlr_masculina
        masculina.append(venda_masculina)
    elif cod <1000000 or cod > 3990000:
         erros.append(cod)


print(f'Linha infantil: {sum(infantil):.2f}\n')
print(f'Linha feminina: {sum(feminina):.2f}\n')
print(f'Linha masculina: {sum(masculina):.2f}\n')
print(f'Total geral: {sum(feminina) + sum(masculina) + sum(infantil):.2f}')

for i in range(len(erros)):
    print(erros[i])
        





