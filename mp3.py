import os

def busca_mp3(lista, dirname):

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path) and path.endswith('.mp3'):
            lista.append(path)
        else:
            busca_mp3(lista, path)

res = []

busca_mp3(res,'C:\\Users\Londres31\\Music\\')
print(res)