

import random
import string

def GeraSenha(tipo, tamanho):
    if tipo == 'A':
        senha = ''.join(random.choices(string.digits, k = tamanho))
    elif tipo == 'B':
        senha = ''.join(random.choices(string.ascii_uppercase +
                                       string.ascii_lowercase, k = tamanho))
    elif tipo == 'C':
        senha = ''.join(random.choices(string.ascii_uppercase +
                                       string.digits, k = tamanho))
    elif tipo == 'D':
        senha = ''.join(random.choices(string.ascii_uppercase +
                                       string.ascii_lowercase +
                                       string.digits, k = tamanho))
    elif tipo == 'E':
        especiais = '+-_!?#@*&=$%'
        senha = ''.join(random.choices(string.ascii_uppercase +
                                       string.ascii_lowercase +
                                       string.digits +
                                       especiais, k = tamanho))
    senha = str(senha)
    return senha


i = False
while i != True:
    tipSenha = input('\nIndique o tipo de senha:\n'
                     'A = Numérica\n'
                     'B = Alfabética\n'
                     'C = Alfanumérica 1\n'
                     'D = Alfanumérica 2\n'
                     'E = Geral\n')
    #tipSenha = tipSenha.upper()
    if tipSenha != 'A' and tipSenha != 'B' and tipSenha != 'C' and tipSenha != 'D' and tipSenha != 'E':
        print('Tipo de senha inválido')
    else:
        i = True


tamSenha = int(input('\nInsira o tamanho da senha (entre 6 e 25): '))
while tamSenha < 6 or tamSenha > 25:
    print(' Tamanho inserido inválido.')
    tamSenha = int(input('\nIndique o tamanho da senha (entre 6 e 25): '))


arqE = open('matr.txt', 'r')
arqS = open('senhas.txt', 'w')
linha = arqE.readline().rstrip()
while linha != '':
    givSenha = GeraSenha(tipSenha, tamSenha)
    arqS.write(f'{linha};{givSenha};\n')
    linha = arqE.readline().rstrip()
arqE.close()
arqS.close()
