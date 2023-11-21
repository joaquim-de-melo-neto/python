import string
def process_line(dicionario, linha):
    linha.replace('-','')

    for word in linha.split():
        word = word.strip(string.punctuation+string.whitespace)
        word = word.lower()
        dicionario[word] = dicionario.get(word,0) + 1

######################################################

def process_file(file) -> dict:
    dicionario = dict()
    for line in file:
        process_line(dicionario, line)

    return dicionario


file = open('C:\\Users\Londres31\Desktop\\texto.txt')

contador_palavras = process_file(file)

print(contador_palavras)
