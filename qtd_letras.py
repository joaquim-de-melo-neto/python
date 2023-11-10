def cont_letras(frase:str):
    spaces = 0
    letras = 0
    pont = 0
    for letra in frase:
        if letra.isspace():
            spaces += 1
        elif letra.lower().isalpha():
            letras += 1
        else:
            pont += 1

    list = [letras, spaces, pont]
    return list

string = input("informe a frase: ")

print("letras - espaços - pontuação")
print(cont_letras(string))

