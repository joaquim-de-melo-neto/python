import os

contatos = []
def linha():
    print('\n--------------------------\n\n')
    
def adicionar_contato():
    print('--- ADICIONAR CONTATO ---')
    nome = input('Informe o nome: ')
    telefone = input('Informe o numero: ')
    
while True:
    print('--- CRUD ---')
    print('1 - Adicionar contato\n2 - Exibir lista\n3 - Deletar contato\n4 - Sair\n')
    opcao = int(input('Informe a opção desejada: '))
    
    match opcao:
        case 1:
            adicionar_contato()
    linha()
