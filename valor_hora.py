import math

def calc_vh(s:float, h:float):
    return s/h


soldo = float(input("Informe o salário "))
horas_trabalhadas = float(input("Informe as horas trabalhadas "))

print(calc_vh(soldo,horas_trabalhadas))