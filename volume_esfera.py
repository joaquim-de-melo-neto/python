import math
def calc_vol_esfera(raio):
    return (4/3)* math.pi*raio**3

raio = int(input('digite o raio'))
print(calc_vol_esfera(raio))
