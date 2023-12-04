import os

contatos = []
def linha():
    print('\n--------------------------\n\n')
    
def validar_digito(digito):
    if digito.isdigit() and (0 < digito <= len(contatos)):
        return True   
    return False
def adicionar_contato():
    print('--- ADICIONAR CONTATO ---')
    nome = input('Informe o nome: ')
    telefone = input('Informe o numero: ')
    contatos.append(nome,telefone)
    linha()
    
def exibir_contatos():
    contador = 1
    for contato in contatos:
        print('%.2d : %s' % contador, contato)
        contador += 1
        
    linha() 
    
def deletar_contato():
    exibir_contatos()
    index = input('Informe o index do contato que deseja apagar: ')
    validar_digito(index)
    del contatos[int(index) - 1]

while True:
    print('--- CRUD ---')
    print('1 - Adicionar contato\n2 - Exibir lista\n3 - Deletar contato\n4 - Sair\n')
    opcao = int(input('Informe a opção desejada: '))

    match opcao:
        case 1:
            adicionar_contato()
        case 2:
            exibir_contatos()    
        case 3:
            deletar_contato()    
        case 2:
            exibir_contatos()    
            
