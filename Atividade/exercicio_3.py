codigo_produto_1 = 101
preco_varejo_1 = 10.0
preco_atacado_1 = 8.0
qma_1 = 5

codigo_produto_2 = 102
preco_varejo_2 = 15.0
preco_atacado_2 = 12.0
qma_2 = 3

codigo_produto_3 = 103
preco_varejo_3 = 20.0
preco_atacado_3 = 18.0
qma_3 = 10

codigo_produto_4 = 104
preco_varejo_4 = 25.0
preco_atacado_4 = 22.0
qma_4 = 7

print("Nome do Aluno: Seu Nome Completo")
print("Número da Questão: 19")

NV = int(input("Digite o número de vendas realizadas (maior que zero): "))

total_varejo = 0.0
total_atacado = 0.0

for i in range(NV):
    cod = int(input(f"\nDigite o código do produto para a venda {i + 1}: "))
    qv = int(input("Digite a quantidade da venda: "))

    if cod == codigo_produto_1:
        qma = qma_1
        preco_varejo = preco_varejo_1
        preco_atacado = preco_atacado_1
    elif cod == codigo_produto_2:
        qma = qma_2
        preco_varejo = preco_varejo_2
        preco_atacado = preco_atacado_2
    elif cod == codigo_produto_3:
        qma = qma_3
        preco_varejo = preco_varejo_3
        preco_atacado = preco_atacado_3
    elif cod == codigo_produto_4:
        qma = qma_4
        preco_varejo = preco_varejo_4
        preco_atacado = preco_atacado_4
    else:
        print("Código inválido")
        continue

    if qv < qma:
        valor_venda = preco_varejo * qv
        total_varejo += valor_venda 
    else: 
        valor_venda = preco_atacado * qv
        total_atacado += valor_venda 

print("\nTotais de vendas:")
print("Total Varejo: R$", round(total_varejo, 2))
print("Total Atacado: R$", round(total_atacado, 2))
print("Total Geral: R$", round(total_varejo + total_atacado, 2))
