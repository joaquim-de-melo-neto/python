nome = input('informe o nome: ')
sobrenome = input('informe o sobrenome: ')
idade = input('informe a idade: ')
email = input('informe o email: ')

aluno = {
    'nome' : nome,
    'sobrenome' : sobrenome,
    'idade' : idade,
    'email' : email,
    'notas' : [],
    'maior_nota' : 0.0,
    'menor_nota' : 0.0,
    'media' : 0,
    'situacao' : 'reprovado'
}

for i in range(4):
    aluno['notas'].append(input(f'Informe a {i+1}º nota: '))


for j in range(4):
    soma = soma + float(aluno['notas'][j])
    if j == 3:
        aluno['media'] = soma / 4.0
        if aluno.get('media') >= 7.0:
            aluno['situacao'] = 'aprovado'

aluno['maior_nota'] = max(aluno.get('notas'))
aluno['menor_nota'] = min(aluno.get('notas'))

print(aluno)