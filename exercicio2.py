carros = {
    'marca' : 'ford',
    'modelo' : 'ka',
    'ano' : '2020',
    'coloração' : 'cinza'
}

if 'cor' in list(carros):
    carros['cor'] = 'preto'
else: del carros['ano']

print(carros)