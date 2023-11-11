# retorna texto informa se argumento é par ou ímpar
par_impar = lambda num : "par" if num % 2 == 0 else "impar"

# devolve o proprio numero se maior que dez caso contrario retorna o mesmo divido por 2
maior_dez = lambda num : num if num > 10 else num / 2

# informa se é divisivel por 3 e 5
div_3_5 = lambda num : "divisivel" if num % 3 == 0 and num % 5 == 0 else "não divisivel"

# concatena dois textos ou devolve msg de texto
concat = lambda str1, str2 : str1 + str2 if len(str1) > 5 and len(str2) > 5 else "erro"

print(par_impar(2))
print(par_impar(3))

print(maior_dez(10))
print(maior_dez(12))

print(div_3_5(15))
print(div_3_5(10))

print(concat("joaquim ", "melo neto"))
print(concat("joao ", "melo"))