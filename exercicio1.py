pessoas = {
    'nome' : ["joao",'alberto'],
    'idade' : [15 , 19],
    'cpf' : ["000.000.000-00", '111.111.111-11'],
    'habilitação' : [False, False]
}

for chave in list(pessoas):
    if chave != 'idade':
        continue
    for i in range(2):
        if pessoas[chave][i] >= 18:
            pessoas['habilitação'][i] = True
        else:
            pessoas['nome'][i] = 'joazinho'

print(pessoas)
