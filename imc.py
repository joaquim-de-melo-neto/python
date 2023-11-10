import math

def calc_imc(peso:float, altura:float):
    return peso / math.pow(altura, 2)

lista = []

for i in range (3):
    h = float(input("Informe a altura: "))
    w = float(input('Informe o peso: '))
    print(calc_imc(w,h))
    lista.append([calc_imc(w,h)])

print(lista)