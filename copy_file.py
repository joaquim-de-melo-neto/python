import string as s

def copy_file(file_copy:str, file:str, str_padrao:str, str_substituta:str):
    fin = open(file)
    fout = open(file_copy,'w')
    for line in fin:
        words = line.split()
        for word in words:
            word = word.strip(s.punctuation + s.whitespace)
            if word == str_padrao:
                fout.write(str_substituta+'\n')
            else:
                fout.write(word)


copy_file('texto_copiado.txt','C:\\Users\\Londres31\\Desktop\\texto.txt','inserido','colocado')