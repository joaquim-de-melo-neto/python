import os
import wc
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(name)
            print(path)

        else:
            walk(path)

walk('C:\\Users\\Londres31\\Desktop')
print(wc.line_count('C:\\Users\\Londres31\\Desktop\\texto.txt'))
