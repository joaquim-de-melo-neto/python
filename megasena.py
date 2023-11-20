import random as ran

aposta = []

while True:
    try:
        qtd_numeros = int(input("Quantos números deseja sortear? "))
    except Exception as e:
        print(f'Exceção: {e} \nDigite um numero válido!')
        continue
    if qtd_numeros not in range(6,11):
        print("Os valores tem que ser de 6 a 10!")
        continue
    contador = 0
    while contador < qtd_numeros:
        aleatorio = ran.randrange(1,61)
        if aleatorio not in aposta:
            aposta.append(aleatorio)
            contador += 1
        else:
            continue
    break

print(aposta)
