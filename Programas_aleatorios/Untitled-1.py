print("\nRHIAN OLIVEIRA DANTAS")
print("THIAGO FATIGATI PALMA")
print("EXERCÍCIO 1\n")


erro = []
infantil = []
masculino = []
feminino = []
codigo = 1

while codigo != 0:

    linha = input("Digite o valor da linha: ")
    linha = int(linha)
    modelo = input("Digite o numero do modelo: ")
    modelo = int(modelo)
    codigo = linha + modelo
    if linha < 100 or linha > 999:
        erro.append(linha)
    if linha >= 100 or linha <= 999:

        qtde = 0
        preco = 0

        if linha >= 100 and linha <= 399:
            qtde = int(input("Informe o valor da quantidade: "))
            preco = int(input("Informe o valor do preço: "))
            subtotal = qtde * preco
            infantil.append(subtotal)
        elif linha >= 400 and linha <= 799:
            qtde = int(input("Informe o valor da quantidade: "))
            preco = int(input("Informe o valor do preço: "))
            subtotal = qtde * preco
            masculino.append(subtotal)
        elif linha >= 800 and linha <= 999:
            qtde = int(input("Informe o valor da quantidade: "))
            preco = int(input("Informe o valor do preço: "))
            subtotal = qtde * preco
            feminino.append(subtotal)

linha_infantil = sum(infantil)
print(f'Linha infantil = {linha_infantil}')

linha_masculina = sum(masculino)
print(f'Linha masculina = {linha_masculina}')

linha_feminina = sum(feminino)
print(f'Linha feminina = {linha_feminina}')

print(f'Total geral = {linha_feminina+linha_masculina+linha_infantil:.2f} ')


print(f'Inconsistencias = {erro} ')



        


    
    


