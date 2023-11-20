import random as ran

def povoar_lista(qtd:int, lista:list):
    contador = 0
    while contador < qtd:
        aleatorio = ran.randrange(1, 61)
        if aleatorio not in lista:
            lista.append(aleatorio)
            contador += 1
        else:
            continue


aposta = []
numeros_sorteados = []

while True:
    try:
        qtd_numeros = int(input("Quantos números deseja sortear? "))
    except Exception as e:
        print(f'Exceção: {e} \nDigite um numero válido!')
        continue
    if qtd_numeros not in range(6,11):
        print("Os valores tem que ser de 6 a 10!")
        continue

    povoar_lista(qtd_numeros, aposta)
    povoar_lista(qtd_numeros, numeros_sorteados)

    break

acertos = 0
for num in aposta:
    if num in numeros_sorteados:
        acertos += 1
print(aposta)
print(numeros_sorteados)
print(f'Número de acertos: {acertos}')
